from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)

def load_json_products():
    """Load products from JSON file"""
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

def load_csv_products():
    """Load products from CSV file"""
    try:
        products = []
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert price to float and id to int
                row['price'] = float(row['price'])
                row['id'] = int(row['id'])
                products.append(row)
        return products
    except (FileNotFoundError, KeyError, ValueError):
        return None

def load_sql_products():
    """Load products from SQLite database"""
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        products = []
        for row in cursor.fetchall():
            products.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            })
        conn.close()
        return products
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None

@app.route('/products')
def display_products():
    """Route to display products with optional filtering"""
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id')
    
    # Validate source parameter
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', 
                            error="Wrong source. Please use 'json', 'csv', or 'sql'")
    
    # Load data based on source
    if source == 'json':
        products = load_json_products()
    elif source == 'csv':
        products = load_csv_products()
    else:  # sql
        products = load_sql_products()
    
    if products is None:
        return render_template('product_display.html', 
                            error=f"Error loading {source} data")
    
    # Filter by ID if provided
    if product_id:
        try:
            product_id = int(product_id)
            filtered_products = [p for p in products if p['id'] == product_id]
            if not filtered_products:
                return render_template('product_display.html',
                                    error="Product not found",
                                    products=[])
            products = filtered_products
        except ValueError:
            return render_template('product_display.html',
                                error="Invalid product ID",
                                products=[])
    
    return render_template('product_display.html', 
                         products=products,
                         error=None)

if __name__ == '__main__':
    # Create database if it doesn't exist
    if not os.path.exists('products.db'):
        import create_db  # Assuming you have this script from the instructions
        create_db.create_database()
    
    app.run(debug=True, port=5000)
