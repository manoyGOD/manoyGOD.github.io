class Item: 

    def __init__(self, id, name, description, price): 
        self.id = id 
        self.name = name 
        self.description = description 
        self.price = price 

    def __str__(self): 
        return f"=========================\nID: {self.id}\nName: {self.name}\nDescription: {self.description}\nPrice: {self.price}\n=========================" 

class ItemManager: 

    def __init__(self): 
        self.items = [] 

    # Create a new item 
    def create_item(self, id, name, description, price): 
        # Validate input 
        if not isinstance(id, int) or id <= 0: 
            raise ValueError("ID must be a positive integer.") 
        if not isinstance(price, (int, float)) or price < 0: 
            raise ValueError("Price must be a non-negative number.") 
        
        # Check if the item with the same ID already exists 
        for item in self.items: 
            if item.id == id: 
                raise ValueError("Item with this ID already exists.") 
        
        # Create and add the new item 
        new_item = Item(id, name, description, price) 
        self.items.append(new_item) 

    # Read an item by ID 
    def read_item(self, id): 
        for item in self.items: 
            if item.id == id: 
                return item 
        raise ValueError("Item not found.") 

    def update_item(self, id, name=None, description=None, price=None): 
        for item in self.items: 
            if item.id == id: 
                if name is not None: 
                    item.name = name 
                if description is not None: 
                    item.description = description 
                if price is not None: 
                    if not isinstance(price, (int, float)) or price < 0: 
                        raise ValueError("Price must be a non-negative number.") 
                    item.price = price 
                return 
        raise ValueError("Item not found.") 

    # Delete an item by ID 
    def delete_item(self, id): 
        for item in self.items: 
            if item.id == id: 
                self.items.remove(item) 
                return 
        raise ValueError("Item not found.") 

# Sample usage 
item_manager = ItemManager() 

# Create a Yamaha NMAX 2025 item 
item_manager.create_item(20250001, "Yamaha NMAX 2025", "The 2025 Yamaha NMAX is a premium maxi-scooter with a powerful Blue Core engine, ABS, traction control, and a modern digital dashboard.", 185000) # Valid 

# Read item 
try: 
    print(item_manager.read_item(20250001)) 
except ValueError as e: 
    print(e)
