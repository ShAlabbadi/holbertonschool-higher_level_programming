from flask import Flask, render_template, request
import json
import csv
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

@app.route('/products')
def display_products():
    """Route to display products with optional filtering"""
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id')
    
    # Load data based on source
    if source == 'json':
        products = load_json_products()
    elif source == 'csv':
        products = load_csv_products()
    else:
        return render_template('product_display.html', 
                            error="Wrong source. Please use 'json' or 'csv'")
    
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
                                    error=f"Product with ID {product_id} not found")
            products = filtered_products
        except ValueError:
            return render_template('product_display.html',
                                error="Invalid product ID")
    
    return render_template('product_display.html', products=products)

# Keep existing routes from previous tasks
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
