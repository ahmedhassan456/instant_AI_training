import tkinter as tk
from tkinter import messagebox
from features.server import Database
from features.menu import MenuItem
from features.order import Order
from features.user import User

# Database connection
db_config = {
    'user': 'ahmed',
    'host': 'localhost',
    'password': '21-12-2004',
    'database': 'restaurant_project'
}
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management System")
        self.root.geometry("800x600")
        self.root.config(bg="#2c3e50")

        self.db = Database(db_config)

        self.main_frame = tk.Frame(self.root, bg="#2c3e50")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.create_login_screen()

    def create_login_screen(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="Login", font=("Helvetica", 20), fg="#ecf0f1", bg="#2c3e50").pack(pady=20)

        tk.Label(self.main_frame, text="Username:", fg="#ecf0f1", bg="#2c3e50").pack(pady=5)
        self.username_entry = tk.Entry(self.main_frame)
        self.username_entry.pack(pady=5)

        tk.Label(self.main_frame, text="Password:", fg="#ecf0f1", bg="#2c3e50").pack(pady=5)
        self.password_entry = tk.Entry(self.main_frame, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self.main_frame, text="Login", command=self.login, bg="#3498db", fg="#ecf0f1").pack(pady=10)
        tk.Button(self.main_frame, text="Register", command=self.create_register_screen, bg="#3498db", fg="#ecf0f1").pack(pady=10)

    def create_register_screen(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="Register", font=("Helvetica", 20), fg="#ecf0f1", bg="#2c3e50").pack(pady=20)

        tk.Label(self.main_frame, text="Username:", fg="#ecf0f1", bg="#2c3e50").pack(pady=5)
        self.reg_username_entry = tk.Entry(self.main_frame)
        self.reg_username_entry.pack(pady=5)

        tk.Label(self.main_frame, text="Password:", fg="#ecf0f1", bg="#2c3e50").pack(pady=5)
        self.reg_password_entry = tk.Entry(self.main_frame, show="*")
        self.reg_password_entry.pack(pady=5)

        tk.Label(self.main_frame, text="Confirm Password:", fg="#ecf0f1", bg="#2c3e50").pack(pady=5)
        self.reg_confirm_password_entry = tk.Entry(self.main_frame, show="*")
        self.reg_confirm_password_entry.pack(pady=5)

        tk.Button(self.main_frame, text="Register", command=self.register_user, bg="#3498db", fg="#ecf0f1").pack(pady=20)
        tk.Button(self.main_frame, text="Back to Login", command=self.create_login_screen, bg="#3498db", fg="#ecf0f1").pack(pady=10)

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.db.check_user_credentials(username, password):
            self.create_main_screen()
        else:
            messagebox.showerror("Error", "Invalid credentials")

    def register_user(self):
        username = self.reg_username_entry.get()
        password = self.reg_password_entry.get()
        confirm_password = self.reg_confirm_password_entry.get()

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
            return

        if self.db.register_user(username, password):
            messagebox.showinfo("Success", "User registered successfully!")
            self.create_login_screen()
        else:
            messagebox.showerror("Error", "Username already exists")

    def create_main_screen(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="Restaurant Management System", font=("Helvetica", 20), fg="#ecf0f1", bg="#2c3e50").pack(pady=20)

        tk.Button(self.main_frame, text="Manage Menu", command=self.create_menu_screen, bg="#3498db", fg="#ecf0f1").pack(pady=10)
        tk.Button(self.main_frame, text="Take Order", command=self.create_order_screen, bg="#3498db", fg="#ecf0f1").pack(pady=10)
        tk.Button(self.main_frame, text="View Orders", command=self.view_orders_screen, bg="#3498db", fg="#ecf0f1").pack(pady=10)
        tk.Button(self.main_frame, text="Generate Bill", command=self.create_generate_bill_screen, bg="#3498db", fg="#ecf0f1").pack(pady=10)
        tk.Button(self.main_frame, text="Logout", command=self.create_login_screen, bg="#3498db", fg="#ecf0f1").pack(pady=10)

    def create_menu_screen(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="Manage Menu", font=("Helvetica", 20), fg="#ecf0f1", bg="#2c3e50").pack(pady=20)

        tk.Button(self.main_frame, text="Add Menu Item", command=self.create_add_menu_item_screen, bg="#3498db", fg="#ecf0f1").pack(pady=10)
        tk.Button(self.main_frame, text="Update Menu Item", command=self.create_update_menu_item_screen, bg="#3498db", fg="#ecf0f1").pack(pady=10)
        tk.Button(self.main_frame, text="Delete Menu Item", command=self.create_delete_menu_item_screen, bg="#3498db", fg="#ecf0f1").pack(pady=10)
        tk.Button(self.main_frame, text="Back to Main Menu", command=self.create_main_screen, bg="#3498db", fg="#ecf0f1").pack(pady=10)

    def create_add_menu_item_screen(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="Add Menu Item", font=("Helvetica", 20), fg="#ecf0f1", bg="#2c3e50").pack(pady=20)

        tk.Label(self.main_frame, text="Item Name:", fg="#ecf0f1", bg="#2c3e50").pack(pady=5)
        self.item_name_entry = tk.Entry(self.main_frame)
        self.item_name_entry.pack(pady=5)

        tk.Label(self.main_frame, text="Price:", fg="#ecf0f1", bg="#2c3e50").pack(pady=5)
        self.item_price_entry = tk.Entry(self.main_frame)
        self.item_price_entry.pack(pady=5)

        tk.Button(self.main_frame, text="Add Item", command=self.add_menu_item, bg="#3498db", fg="#ecf0f1").pack(pady=20)

    def add_menu_item(self):
        name = self.item_name_entry.get()
        try:
            price = float(self.item_price_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Price must be a number")
            return

        self.db.add_menu_item(name, price)
        messagebox.showinfo("Success", f"Menu item '{name}' added successfully!")
        self.create_menu_screen()

    def create_update_menu_item_screen(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="Update Menu Item", font=("Helvetica", 20), fg="#ecf0f1", bg="#2c3e50").pack(pady=20)

        tk.Label(self.main_frame, text="Select Item to Update:", fg="#ecf0f1", bg="#2c3e50").pack(pady=5)
        menu_items = self.db.get_menu_items()
        if menu_items:
            self.update_item_var = tk.StringVar(self.main_frame)
            self.update_item_var.set(menu_items[0][0])
            self.update_item_menu = tk.OptionMenu(self.main_frame, self.update_item_var, *[item[0] for item in menu_items])
            self.update_item_menu.pack(pady=5)
        else:
            tk.Label(self.main_frame, text="No menu items available", fg="#e74c3c", bg="#2c3e50").pack(pady=5)
            return

        tk.Label(self.main_frame, text="New Item Name:", fg="#ecf0f1", bg="#2c3e50").pack(pady=5)
        self.new_item_name_entry = tk.Entry(self.main_frame)
        self.new_item_name_entry.pack(pady=5)

        tk.Label(self.main_frame, text="New Price:", fg="#ecf0f1", bg="#2c3e50").pack(pady=5)
        self.new_item_price_entry = tk.Entry(self.main_frame)
        self.new_item_price_entry.pack(pady=5)

        tk.Button(self.main_frame, text="Update Item", command=self.update_menu_item, bg="#3498db", fg="#ecf0f1").pack(pady=20)

    def update_menu_item(self):
        old_name = self.update_item_var.get()
        new_name = self.new_item_name_entry.get()
        try:
            new_price = float(self.new_item_price_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Price must be a number")
            return

        self.db.update_menu_item(old_name, new_name, new_price)
        messagebox.showinfo("Success", f"Menu item '{new_name}' updated successfully!")
        self.create_menu_screen()

    def create_delete_menu_item_screen(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="Delete Menu Item", font=("Helvetica", 20), fg="#ecf0f1", bg="#2c3e50").pack(pady=20)

        tk.Label(self.main_frame, text="Select Item to Delete:", fg="#ecf0f1", bg="#2c3e50").pack(pady=5)
        menu_items = self.db.get_menu_items()
        if menu_items:
            self.delete_item_var = tk.StringVar(self.main_frame)
            self.delete_item_var.set(menu_items[0][0])
            self.delete_item_menu = tk.OptionMenu(self.main_frame, self.delete_item_var, *[item[0] for item in menu_items])
            self.delete_item_menu.pack(pady=5)
        else:
            tk.Label(self.main_frame, text="No menu items available", fg="#e74c3c", bg="#2c3e50").pack(pady=5)
            return

        tk.Button(self.main_frame, text="Delete Item", command=self.delete_menu_item, bg="#3498db", fg="#ecf0f1").pack(pady=20)

    def delete_menu_item(self):
        name = self.delete_item_var.get()
        self.db.delete_menu_item(name)
        messagebox.showinfo("Success", f"Menu item '{name}' deleted successfully!")
        self.create_menu_screen()

    def create_order_screen(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="Take Order", font=("Helvetica", 20), fg="#ecf0f1", bg="#2c3e50").pack(pady=20)

        tk.Label(self.main_frame, text="Table Number:", fg="#ecf0f1", bg="#2c3e50").pack(pady=5)
        self.table_number_entry = tk.Entry(self.main_frame)
        self.table_number_entry.pack(pady=5)

        tk.Label(self.main_frame, text="Select Item:", fg="#ecf0f1", bg="#2c3e50").pack(pady=5)
        menu_items = self.db.get_menu_items()
        if menu_items:
            self.order_item_var = tk.StringVar(self.main_frame)
            self.order_item_var.set(menu_items[0][0])
            self.order_item_menu = tk.OptionMenu(self.main_frame, self.order_item_var, *[item[0] for item in menu_items])
            self.order_item_menu.pack(pady=5)
        else:
            tk.Label(self.main_frame, text="No menu items available", fg="#e74c3c", bg="#2c3e50").pack(pady=5)
            return

        tk.Button(self.main_frame, text="Add Item to Order", command=self.add_item_to_order, bg="#3498db", fg="#ecf0f1").pack(pady=10)
        tk.Button(self.main_frame, text="Complete Order", command=self.complete_order, bg="#3498db", fg="#ecf0f1").pack(pady=20)

        self.current_order_items = []

    def add_item_to_order(self):
        table_number = self.table_number_entry.get()
        if not table_number:
            messagebox.showerror("Error", "Please enter a table number")
            return

        selected_item_name = self.order_item_var.get()
        menu_items = self.db.get_menu_items()
        for item in menu_items:
            if item[0] == selected_item_name:
                menu_item = MenuItem(item[0], item[1])
                self.current_order_items.append(menu_item)
                messagebox.showinfo("Success", f"Item '{menu_item.name}' added to the order")
                return

    def complete_order(self):
        table_number = self.table_number_entry.get()
        if not table_number:
            messagebox.showerror("Error", "Please enter a table number")
            return

        if not self.current_order_items:
            messagebox.showerror("Error", "No items in the order")
            return

        order = Order(table_number)
        for item in self.current_order_items:
            order.add_item(item)
        self.db.add_order(table_number, self.current_order_items)
        messagebox.showinfo("Success", "Order completed successfully!")
        self.create_main_screen()

    def view_orders_screen(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="View Orders", font=("Helvetica", 20), fg="#ecf0f1", bg="#2c3e50").pack(pady=20)

        orders = self.db.get_orders()
        for order in orders:
            order_label = tk.Label(self.main_frame, text=str(order), fg="#ecf0f1", bg="#2c3e50")
            order_label.pack(pady=5)

        tk.Button(self.main_frame, text="Back to Main Menu", command=self.create_main_screen, bg="#3498db", fg="#ecf0f1").pack(pady=10)

    def create_generate_bill_screen(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="Generate Bill", font=("Helvetica", 20), fg="#ecf0f1", bg="#2c3e50").pack(pady=20)

        tk.Label(self.main_frame, text="Enter Table Number:", fg="#ecf0f1", bg="#2c3e50").pack(pady=5)
        self.bill_table_number_entry = tk.Entry(self.main_frame)
        self.bill_table_number_entry.pack(pady=5)

        tk.Button(self.main_frame, text="Generate Bill", command=self.generate_bill, bg="#3498db", fg="#ecf0f1").pack(pady=20)
        tk.Button(self.main_frame, text="Back to Main Menu", command=self.create_main_screen, bg="#3498db", fg="#ecf0f1").pack(pady=10)


    def generate_bill(self):
        table_number = self.bill_table_number_entry.get()
        if not table_number:
            messagebox.showerror("Error", "Please enter a table number")
            return

        orders = self.db.get_orders()
        for order in orders:
            if order.table_number == table_number:
                bill = order.generate_bill()
                self.show_bill_window(bill)
                return

        messagebox.showerror("Error", "No orders found for the given table number")

    def show_bill_window(self, bill):
        bill_window = tk.Toplevel(self.root)
        bill_window.title("Bill")
        bill_window.geometry("400x300")
        bill_window.config(bg="#2c3e50")

        tk.Label(bill_window, text="Bill", font=("Helvetica", 20), fg="#ecf0f1", bg="#2c3e50").pack(pady=20)
        tk.Label(bill_window, text=bill, fg="#ecf0f1", bg="#2c3e50").pack(pady=10)

        tk.Button(bill_window, text="Close", command=bill_window.destroy, bg="#3498db", fg="#ecf0f1").pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
