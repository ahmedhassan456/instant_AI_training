import mysql.connector
from features.menu import MenuItem
from features.order import Order
from features.user import User

class Database:
    def __init__(self, config):
        self.conn = mysql.connector.connect(**config)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) UNIQUE,
            password VARCHAR(255)
        )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS menu_items (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            price DECIMAL(10, 2)
        )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INT AUTO_INCREMENT PRIMARY KEY,
            table_number VARCHAR(255),
            completed BOOLEAN
        )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS order_items (
            id INT AUTO_INCREMENT PRIMARY KEY,
            order_id INT,
            menu_item_id INT,
            FOREIGN KEY (order_id) REFERENCES orders(id),
            FOREIGN KEY (menu_item_id) REFERENCES menu_items(id)
        )
        """)
        self.conn.commit()

    def register_user(self, username, password):
        try:
            self.cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            self.conn.commit()
            return True
        except mysql.connector.IntegrityError:
            return False

    def check_user_credentials(self, username, password):
        self.cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        return self.cursor.fetchone() is not None

    def add_menu_item(self, name, price):
        self.cursor.execute("INSERT INTO menu_items (name, price) VALUES (%s, %s)", (name, price))
        self.conn.commit()

    def update_menu_item(self, old_name, new_name, new_price):
        self.cursor.execute("UPDATE menu_items SET name = %s, price = %s WHERE name = %s", (new_name, new_price, old_name))
        self.conn.commit()

    def delete_menu_item(self, name):
        self.cursor.execute("DELETE FROM menu_items WHERE name = %s", (name,))
        self.conn.commit()

    def get_menu_items(self):
        self.cursor.execute("SELECT name, price FROM menu_items")
        return self.cursor.fetchall()

    def add_order(self, table_number, items):
        self.cursor.execute("INSERT INTO orders (table_number, completed) VALUES (%s, %s)", (table_number, False))
        order_id = self.cursor.lastrowid
        for item in items:
            self.cursor.execute("SELECT id FROM menu_items WHERE name = %s", (item.name,))
            menu_item_id = self.cursor.fetchone()[0]
            self.cursor.execute("INSERT INTO order_items (order_id, menu_item_id) VALUES (%s, %s)", (order_id, menu_item_id))
        self.conn.commit()

    def complete_order(self, order_id):
        self.cursor.execute("UPDATE orders SET completed = %s WHERE id = %s", (True, order_id))
        self.conn.commit()

    def get_orders(self):
        self.cursor.execute("SELECT o.id, o.table_number, o.completed, m.name, m.price FROM orders o JOIN order_items oi ON o.id = oi.order_id JOIN menu_items m ON oi.menu_item_id = m.id")
        orders = {}
        for row in self.cursor.fetchall():
            order_id, table_number, completed, item_name, item_price = row
            if order_id not in orders:
                orders[order_id] = Order(table_number)
                orders[order_id].completed = completed
            orders[order_id].add_item(MenuItem(item_name, item_price))
        return list(orders.values())