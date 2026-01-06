""" 
Exercise 1: Inventory Management System
Design a program for a retail store to manage inventory. 
The inventory is stored as a dictionary where keys are item names (strings) and values are lists containing [price (float), quantity (int), category (string)]. 
The program should take user input for an item name, check if it exists (error handling if not), loop through the inventory to calculate total value of stock in a given category, use conditional branching to apply a 10% discount if quantity > 50, and store unique categories in a set. Output the discounted total value and list of categories as a tuple.
"""

def manage_inventory(inventory, item_name, target_category):
    # Error handling for item not found
    # Loop through inventory
    # Conditional for discount
    # Use set for unique categories
    # Return tuple of (discounted_total, categories_tuple)
    pass

# Example usage (for testing)
inventory = {
    "Laptop": [999.99, 30, "Electronics"],
    "Shirt": [19.99, 60, "Clothing"],
    "Phone": [499.99, 45, "Electronics"]
}
print(manage_inventory(inventory, "Shirt", "Electronics"))  # Example call