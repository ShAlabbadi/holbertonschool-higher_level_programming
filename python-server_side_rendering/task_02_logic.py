from flask import Flask, render_template
import json
import os

app = Flask(__name__)

def load_items():
    """Load items from JSON file"""
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            return data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        return []

@app.route('/items')
def show_items():
    """Route to display items from JSON file"""
    items = load_items()
    return render_template('items.html', items=items)

# Keep your existing routes from previous task
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
