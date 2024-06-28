<<<<<<< HEAD
import tkinter as tk
from tkinter import messagebox
from features.user import User
from features.menu import MenuItem
from features.order import Order

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management System")
        self.root.geometry("800x600")

        self.user = User("admin", "password")
        self.menu_items = []
        self.orders = []

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.create_login_screen()

    def create_login_screen(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="Login", font=("Helvetica", 16)).pack(pady=20)

        tk.Label(self.main_frame, text="Username:").pack(pady=5)
        self.username_entry = tk.Entry(self.main_frame)
        self.username_entry.pack(pady=5)

        tk.Label(self.main_frame, text="Password:").pack(pady=5)
        self.password_entry = tk.Entry(self.main_frame, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self.main_frame, text="Login", command=self.login).pack(pady=20)

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.user.check_credentials(username, password):
            self.create_main_screen()
        else:
            messagebox.showerror("Error", "Invalid credentials")

    def create_main_screen(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Welcome to the Restaurant Management System", font=("Helvetica", 16)).pack(pady=20)
        tk.Button(self.main_frame, text="Manage Menu", command=self.create_menu_screen).pack(pady=10)
        tk.Button(self.main_frame, text="Take Order", command=self.create_order_screen).pack(pady=10)
        tk.Button(self.main_frame, text="View Orders", command=self.view_orders_screen).pack(pady=10)
        tk.Button(self.main_frame, text="Generate Bills", command=self.create_generate_bill_screen).pack(pady=10)

    def create_menu_screen(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Menu Management", font=("Helvetica", 16)).pack(pady=20)
        tk.Button(self.main_frame, text="Add Menu Item", command=self.create_add_menu_item_screen).pack(pady=10)
        tk.Button(self.main_frame, text="Update Menu Item", command=self.create_update_menu_item_screen).pack(pady=10)
        tk.Button(self.main_frame, text="Delete Menu Item", command=self.create_delete_menu_item_screen).pack(pady=10)
        tk.Button(self.main_frame, text="Back to Main Menu", command=self.create_main_screen).pack(pady=10)

    def create_add_menu_item_screen(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Add Menu Item", font=("Helvetica", 16)).pack(pady=20)
        tk.Label(self.main_frame, text="Item Name:").pack(pady=5)
        self.item_name_entry = tk.Entry(self.main_frame)
        self.item_name_entry.pack(pady=5)
        tk.Label(self.main_frame, text="Price:").pack(pady=5)
        self.item_price_entry = tk.Entry(self.main_frame)
        self.item_price_entry.pack(pady=5)
        tk.Button(self.main_frame, text="Add Item", command=self.add_menu_item).pack(pady=20)

    def add_menu_item(self):
        item_name = self.item_name_entry.get()
        item_price = self.item_price_entry.get()

        try:
            item_price = float(item_price)
        except ValueError:
            messagebox.showerror("Error", "Price must be a number")
            return

        new_item = MenuItem(item_name, item_price)
        self.menu_items.append(new_item)
        messagebox.showinfo("Success", f"Menu item '{item_name}' added successfully!")
        self.create_menu_screen()

    def create_update_menu_item_screen(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Update Menu Item", font=("Helvetica", 16)).pack(pady=20)
        
        tk.Label(self.main_frame, text="Select Item:").pack(pady=5)
        self.update_item_var = tk.StringVar(self.main_frame)
        self.update_item_var.set("Select an item")
        self.update_item_menu = tk.OptionMenu(self.main_frame, self.update_item_var, *[str(item) for item in self.menu_items])
        self.update_item_menu.pack(pady=5)
        
        tk.Label(self.main_frame, text="New Price:").pack(pady=5)
        self.new_price_entry = tk.Entry(self.main_frame)
        self.new_price_entry.pack(pady=5)
        
        tk.Button(self.main_frame, text="Update Item", command=self.update_menu_item).pack(pady=20)

    def update_menu_item(self):
        selected_item_str = self.update_item_var.get()
        new_price = self.new_price_entry.get()

        try:
            new_price = float(new_price)
        except ValueError:
            messagebox.showerror("Error", "Price must be a number")
            return

        for item in self.menu_items:
            if str(item) == selected_item_str:
                item.price = new_price
                messagebox.showinfo("Success", f"Menu item '{item.name}' updated successfully!")
                break

        self.create_menu_screen()

    def create_delete_menu_item_screen(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Delete Menu Item", font=("Helvetica", 16)).pack(pady=20)
        
        tk.Label(self.main_frame, text="Select Item:").pack(pady=5)
        self.delete_item_var = tk.StringVar(self.main_frame)
        self.delete_item_var.set("Select an item")
        self.delete_item_menu = tk.OptionMenu(self.main_frame, self.delete_item_var, *[str(item) for item in self.menu_items])
        self.delete_item_menu.pack(pady=5)
        
        tk.Button(self.main_frame, text="Delete Item", command=self.delete_menu_item).pack(pady=20)

    def delete_menu_item(self):
        selected_item_str = self.delete_item_var.get()

        for item in self.menu_items:
            if str(item) == selected_item_str:
                self.menu_items.remove(item)
                messagebox.showinfo("Success", f"Menu item '{item.name}' deleted successfully!")
                break

        self.create_menu_screen()

    def create_order_screen(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Take Order", font=("Helvetica", 16)).pack(pady=20)
        
        tk.Label(self.main_frame, text="Table Number:").pack(pady=5)
        self.table_number_entry = tk.Entry(self.main_frame)
        self.table_number_entry.pack(pady=5)
        
        tk.Label(self.main_frame, text="Select Item:").pack(pady=5)
        
        if self.menu_items:
            self.order_item_var = tk.StringVar(self.main_frame)
            self.order_item_var.set(str(self.menu_items[0]))  # Set default value to the first item in the list
            self.order_item_menu = tk.OptionMenu(self.main_frame, self.order_item_var, *[str(item) for item in self.menu_items])
            self.order_item_menu.pack(pady=5)
        else:
            tk.Label(self.main_frame, text="No menu items available").pack(pady=5)
        
        tk.Button(self.main_frame, text="Add Item to Order", command=self.add_item_to_order).pack(pady=10)
        tk.Button(self.main_frame, text="Complete Order", command=self.complete_order).pack(pady=20)
        
        self.current_order = None

    def add_item_to_order(self):
        table_number = self.table_number_entry.get()
        if not table_number:
            messagebox.showerror("Error", "Please enter a table number")
            return
        
        if self.current_order is None:
            self.current_order = Order(table_number)
        
        selected_item_str = self.order_item_var.get()
        for item in self.menu_items:
            if str(item) == selected_item_str:
                self.current_order.add_item(item)
                messagebox.showinfo("Success", f"Item '{item.name}' added to order for table {table_number}")
                break

    def complete_order(self):
        if self.current_order is None or not self.current_order.items:
            messagebox.showerror("Error", "No items in the current order")
            return
        
        self.current_order.mark_completed()
        self.orders.append(self.current_order)
        messagebox.showinfo("Success", f"Order for table {self.current_order.table_number} completed successfully!")
        self.current_order = None
        self.create_main_screen()

    def view_orders_screen(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Current Orders", font=("Helvetica", 16)).pack(pady=20)
        
        for order in self.orders:
            tk.Label(self.main_frame, text=str(order)).pack(pady=5)
        
        tk.Button(self.main_frame, text="Back to Main Menu", command=self.create_main_screen).pack(pady=20)

    def create_generate_bill_screen(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Generate Bills", font=("Helvetica", 16)).pack(pady=20)
        
        tk.Label(self.main_frame, text="Select Order:").pack(pady=5)
        self.bill_order_var = tk.StringVar(self.main_frame)
        self.bill_order_var.set("Select an order")
        self.bill_order_menu = tk.OptionMenu(self.main_frame, self.bill_order_var, *[str(order) for order in self.orders if order.completed])
        self.bill_order_menu.pack(pady=5)
        
        tk.Button(self.main_frame, text="Generate Bill", command=self.generate_bill).pack(pady=20)
        tk.Button(self.main_frame, text="Back to Main Menu", command=self.create_main_screen).pack(pady=10)

    def generate_bill(self):
        selected_order_str = self.bill_order_var.get()
        for order in self.orders:
            if str(order) == selected_order_str:
                bill = order.generate_bill()
                messagebox.showinfo("Bill", bill)
                break

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
=======
import tkinter as tk
from tkinter import messagebox
from features.user import User
from features.menu import MenuItem
from features.order import Order

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management System")
        self.root.geometry("800x600")

        self.user = User("admin", "password")
        self.menu_items = []
        self.orders = []

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.create_login_screen()

    def create_login_screen(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="Login", font=("Helvetica", 16)).pack(pady=20)

        tk.Label(self.main_frame, text="Username:").pack(pady=5)
        self.username_entry = tk.Entry(self.main_frame)
        self.username_entry.pack(pady=5)

        tk.Label(self.main_frame, text="Password:").pack(pady=5)
        self.password_entry = tk.Entry(self.main_frame, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self.main_frame, text="Login", command=self.login).pack(pady=20)

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.user.check_credentials(username, password):
            self.create_main_screen()
        else:
            messagebox.showerror("Error", "Invalid credentials")

    def create_main_screen(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Welcome to the Restaurant Management System", font=("Helvetica", 16)).pack(pady=20)
        tk.Button(self.main_frame, text="Manage Menu", command=self.create_menu_screen).pack(pady=10)
        tk.Button(self.main_frame, text="Take Order", command=self.create_order_screen).pack(pady=10)
        tk.Button(self.main_frame, text="View Orders", command=self.view_orders_screen).pack(pady=10)
        tk.Button(self.main_frame, text="Generate Bills", command=self.create_generate_bill_screen).pack(pady=10)

    def create_menu_screen(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Menu Management", font=("Helvetica", 16)).pack(pady=20)
        tk.Button(self.main_frame, text="Add Menu Item", command=self.create_add_menu_item_screen).pack(pady=10)
        tk.Button(self.main_frame, text="Update Menu Item", command=self.create_update_menu_item_screen).pack(pady=10)
        tk.Button(self.main_frame, text="Delete Menu Item", command=self.create_delete_menu_item_screen).pack(pady=10)
        tk.Button(self.main_frame, text="Back to Main Menu", command=self.create_main_screen).pack(pady=10)

    def create_add_menu_item_screen(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Add Menu Item", font=("Helvetica", 16)).pack(pady=20)
        tk.Label(self.main_frame, text="Item Name:").pack(pady=5)
        self.item_name_entry = tk.Entry(self.main_frame)
        self.item_name_entry.pack(pady=5)
        tk.Label(self.main_frame, text="Price:").pack(pady=5)
        self.item_price_entry = tk.Entry(self.main_frame)
        self.item_price_entry.pack(pady=5)
        tk.Button(self.main_frame, text="Add Item", command=self.add_menu_item).pack(pady=20)

    def add_menu_item(self):
        item_name = self.item_name_entry.get()
        item_price = self.item_price_entry.get()

        try:
            item_price = float(item_price)
        except ValueError:
            messagebox.showerror("Error", "Price must be a number")
            return

        new_item = MenuItem(item_name, item_price)
        self.menu_items.append(new_item)
        messagebox.showinfo("Success", f"Menu item '{item_name}' added successfully!")
        self.create_menu_screen()

    def create_update_menu_item_screen(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Update Menu Item", font=("Helvetica", 16)).pack(pady=20)
        
        tk.Label(self.main_frame, text="Select Item:").pack(pady=5)
        self.update_item_var = tk.StringVar(self.main_frame)
        self.update_item_var.set("Select an item")
        self.update_item_menu = tk.OptionMenu(self.main_frame, self.update_item_var, *[str(item) for item in self.menu_items])
        self.update_item_menu.pack(pady=5)
        
        tk.Label(self.main_frame, text="New Price:").pack(pady=5)
        self.new_price_entry = tk.Entry(self.main_frame)
        self.new_price_entry.pack(pady=5)
        
        tk.Button(self.main_frame, text="Update Item", command=self.update_menu_item).pack(pady=20)

    def update_menu_item(self):
        selected_item_str = self.update_item_var.get()
        new_price = self.new_price_entry.get()

        try:
            new_price = float(new_price)
        except ValueError:
            messagebox.showerror("Error", "Price must be a number")
            return

        for item in self.menu_items:
            if str(item) == selected_item_str:
                item.price = new_price
                messagebox.showinfo("Success", f"Menu item '{item.name}' updated successfully!")
                break

        self.create_menu_screen()

    def create_delete_menu_item_screen(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Delete Menu Item", font=("Helvetica", 16)).pack(pady=20)
        
        tk.Label(self.main_frame, text="Select Item:").pack(pady=5)
        self.delete_item_var = tk.StringVar(self.main_frame)
        self.delete_item_var.set("Select an item")
        self.delete_item_menu = tk.OptionMenu(self.main_frame, self.delete_item_var, *[str(item) for item in self.menu_items])
        self.delete_item_menu.pack(pady=5)
        
        tk.Button(self.main_frame, text="Delete Item", command=self.delete_menu_item).pack(pady=20)

    def delete_menu_item(self):
        selected_item_str = self.delete_item_var.get()

        for item in self.menu_items:
            if str(item) == selected_item_str:
                self.menu_items.remove(item)
                messagebox.showinfo("Success", f"Menu item '{item.name}' deleted successfully!")
                break

        self.create_menu_screen()

    def create_order_screen(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Take Order", font=("Helvetica", 16)).pack(pady=20)
        
        tk.Label(self.main_frame, text="Table Number:").pack(pady=5)
        self.table_number_entry = tk.Entry(self.main_frame)
        self.table_number_entry.pack(pady=5)
        
        tk.Label(self.main_frame, text="Select Item:").pack(pady=5)
        
        if self.menu_items:
            self.order_item_var = tk.StringVar(self.main_frame)
            self.order_item_var.set(str(self.menu_items[0]))  # Set default value to the first item in the list
            self.order_item_menu = tk.OptionMenu(self.main_frame, self.order_item_var, *[str(item) for item in self.menu_items])
            self.order_item_menu.pack(pady=5)
        else:
            tk.Label(self.main_frame, text="No menu items available").pack(pady=5)
        
        tk.Button(self.main_frame, text="Add Item to Order", command=self.add_item_to_order).pack(pady=10)
        tk.Button(self.main_frame, text="Complete Order", command=self.complete_order).pack(pady=20)
        
        self.current_order = None

    def add_item_to_order(self):
        table_number = self.table_number_entry.get()
        if not table_number:
            messagebox.showerror("Error", "Please enter a table number")
            return
        
        if self.current_order is None:
            self.current_order = Order(table_number)
        
        selected_item_str = self.order_item_var.get()
        for item in self.menu_items:
            if str(item) == selected_item_str:
                self.current_order.add_item(item)
                messagebox.showinfo("Success", f"Item '{item.name}' added to order for table {table_number}")
                break

    def complete_order(self):
        if self.current_order is None or not self.current_order.items:
            messagebox.showerror("Error", "No items in the current order")
            return
        
        self.current_order.mark_completed()
        self.orders.append(self.current_order)
        messagebox.showinfo("Success", f"Order for table {self.current_order.table_number} completed successfully!")
        self.current_order = None
        self.create_main_screen()

    def view_orders_screen(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Current Orders", font=("Helvetica", 16)).pack(pady=20)
        
        for order in self.orders:
            tk.Label(self.main_frame, text=str(order)).pack(pady=5)
        
        tk.Button(self.main_frame, text="Back to Main Menu", command=self.create_main_screen).pack(pady=20)

    def create_generate_bill_screen(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Generate Bills", font=("Helvetica", 16)).pack(pady=20)
        
        tk.Label(self.main_frame, text="Select Order:").pack(pady=5)
        self.bill_order_var = tk.StringVar(self.main_frame)
        self.bill_order_var.set("Select an order")
        self.bill_order_menu = tk.OptionMenu(self.main_frame, self.bill_order_var, *[str(order) for order in self.orders if order.completed])
        self.bill_order_menu.pack(pady=5)
        
        tk.Button(self.main_frame, text="Generate Bill", command=self.generate_bill).pack(pady=20)
        tk.Button(self.main_frame, text="Back to Main Menu", command=self.create_main_screen).pack(pady=10)

    def generate_bill(self):
        selected_order_str = self.bill_order_var.get()
        for order in self.orders:
            if str(order) == selected_order_str:
                bill = order.generate_bill()
                messagebox.showinfo("Bill", bill)
                break

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
>>>>>>> b64c73be611407c03eaf6647be6f36ba75be5d14
    root.mainloop()