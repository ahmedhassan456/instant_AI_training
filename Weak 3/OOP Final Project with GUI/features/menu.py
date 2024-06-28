<<<<<<< HEAD
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
=======
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
>>>>>>> b64c73be611407c03eaf6647be6f36ba75be5d14
        return f"{self.name}: ${self.price:.2f}"