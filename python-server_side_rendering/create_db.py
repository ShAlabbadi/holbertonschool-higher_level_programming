import sqlite3

def create_database():
    """Create and populate the SQLite database"""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    
    # Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    # Insert sample data
    cursor.execute('''
        INSERT OR IGNORE INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99),
        (3, 'Wireless Headphones', 'Electronics', 149.99),
        (4, 'Notebook', 'Office Supplies', 4.99)
    ''')
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
