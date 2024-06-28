class Order:
    def __init__(self, table_number):
        self.table_number = table_number
        self.items = []
        self.completed = False

    def add_item(self, menu_item):
        self.items.append(menu_item)

    def get_total(self):
        return sum(item.price for item in self.items)

    def mark_completed(self):
        self.completed = True

    def generate_bill(self):
        bill = f"Bill for Table {self.table_number}\n"
        bill += "--------------------------------\n"
        for item in self.items:
            bill += f"{item.name}: ${item.price:.2f}\n"
        bill += "--------------------------------\n"
        bill += f"Total: ${self.get_total():.2f}\n"
        return bill

    def __str__(self):
        items_str = ', '.join(f"{item.name} (${item.price:.2f})" for item in self.items)
        return f"Table {self.table_number} - Items: {items_str} - Total: ${self.get_total():.2f} - {'Completed' if self.completed else 'Pending'}"
