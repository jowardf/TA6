class Item:
    # Class representing an item with ID, name, description, and price
    def __init__(self, item_id: int, name: str, description: str, price: float):
        if not isinstance(item_id, int) or item_id <= 0:
            raise ValueError("Item ID must be a positive integer.")
        if not name or not isinstance(name, str):
            raise ValueError("Item name must be a non-empty string.")
        if not isinstance(description, str):
            raise ValueError("Description must be a string.")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a non-negative number.")

        self.id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        # Returns a string representation of the item
        return f"ID: {self.id}, Name: {self.name}, Description: {self.description}, Price: ${self.price:.2f}"


class ItemManager:
    # Class to manage CRUD operations for items
    def __init__(self):
        self.items = {}  # Dictionary to store items with item_id as key

    def create_item(self, item_id, name, description, price):
        # Creates a new item and adds it to the dictionary
        try:
            if item_id in self.items:
                raise ValueError("Item ID already exists.")
            item = Item(item_id, name, description, price)
            self.items[item_id] = item
            print("Item added successfully!")
        except ValueError as e:
            print(f"Error: {e}")

    def read_item(self, item_id):
        # Retrieves an item by ID and returns its details
        try:
            if item_id not in self.items:
                raise KeyError("Item not found.")
            return str(self.items[item_id])
        except KeyError as e:
            return f"Error: {e}"

    def update_item(self, item_id, name=None, description=None, price=None):
        # Updates an existing item with new values
        try:
            if item_id not in self.items:
                raise KeyError("Item not found.")
            if name:
                self.items[item_id].name = name
            if description:
                self.items[item_id].description = description
            if price is not None:
                if not isinstance(price, (int, float)) or price < 0:
                    raise ValueError("Price must be a non-negative number.")
                self.items[item_id].price = price
            print("Item updated successfully!")
        except (KeyError, ValueError) as e:
            print(f"Error: {e}")

    def delete_item(self, item_id):
        # Deletes an item by ID
        try:
            if item_id not in self.items:
                raise KeyError("Item not found.")
            del self.items[item_id]
            print("Item deleted successfully!")
        except KeyError as e:
            print(f"Error: {e}")

    def list_items(self):
        # Returns a list of all items or a message if no items exist
        if not self.items:
            return "No items available."
        return "\n".join(str(item) for item in self.items.values())


# User Interaction
if __name__ == "__main__":
    manager = ItemManager()

    while True:
        print("\nItem Management System")
        print("1. Add Item")
        print("2. View Item")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. List Items")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                item_id = int(input("Enter item ID: "))
                name = input("Enter item name: ")
                description = input("Enter item description: ")
                price = float(input("Enter item price: "))
                manager.create_item(item_id, name, description, price)
            except ValueError:
                print("Invalid input. Please enter correct values.")

        elif choice == "2":
            try:
                item_id = int(input("Enter item ID to view: "))
                print(manager.read_item(item_id))
            except ValueError:
                print("Invalid input. Please enter a valid item ID.")

        elif choice == "3":
            try:
                item_id = int(input("Enter item ID to update: "))
                name = input("Enter new name (leave blank to keep current): ") or None
                description = input("Enter new description (leave blank to keep current): ") or None
                price_input = input("Enter new price (leave blank to keep current): ")
                price = float(price_input) if price_input else None
                manager.update_item(item_id, name, description, price)
            except ValueError:
                print("Invalid input. Please enter correct values.")

        elif choice == "4":
            try:
                item_id = int(input("Enter item ID to delete: "))
                manager.delete_item(item_id)
            except ValueError:
                print("Invalid input. Please enter a valid item ID.")

        elif choice == "5":
            print(manager.list_items())

        elif choice == "6":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")
