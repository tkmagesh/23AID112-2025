""" 
Exercise 1: Inventory Management System
Design a program for a retail store to manage inventory. 
The inventory is stored as a dictionary where keys are item names (strings) and values are lists containing [price (float), quantity (int), category (string)]. 
The program should take user input for an item name, check if it exists (error handling if not), loop through the inventory to calculate total value of stock in a given category, use conditional branching to apply a 10% discount if quantity > 50, and store unique categories in a set. Output the discounted total value and list of categories as a tuple.
"""

def manage_inventory(inventory, item_name, target_category):
    """
    Manages retail inventory by calculating discounted total value for a category
    and collecting unique categories.
    
    :param inventory: dict - {item: [price, quantity, category]}
    :param item_name: str - Item to check existence
    :param target_category: str - Category to calculate total for
    :return: tuple - (discounted_total, categories_tuple)
    """
    # Error handling: Check if item_name exists in inventory
    try:
        if item_name not in inventory:
            raise ValueError(f"Item '{item_name}' not found in inventory.")
    except ValueError as e:
        # Handle the error by returning a message
        return str(e), ()
    
    # Initialize variables
    total_value = 0.0  # Float for total stock value
    categories = set()  # Set to store unique categories
    
    # Loop through inventory items
    for item, details in inventory.items():
        price, quantity, category = details  # Unpack list into variables
        categories.add(category)  # Add to set for uniqueness
        
        # Conditional branching: Only process if category matches
        if category == target_category:
            item_value = price * quantity
            # Conditional: Apply 10% discount if quantity > 50
            if quantity > 50:
                item_value *= 0.9  # 10% discount
            total_value += item_value  # Accumulate total
    
    # Convert set to tuple for output
    categories_tuple = tuple(categories)
    
    # Return results
    return total_value, categories_tuple

# Example usage (for testing)
inventory = {
    "Laptop": [999.99, 30, "Electronics"],
    "Shirt": [19.99, 60, "Clothing"],
    "Phone": [499.99, 45, "Electronics"]
}
print(manage_inventory(inventory, "Shirt", "Electronics"))  # Example call