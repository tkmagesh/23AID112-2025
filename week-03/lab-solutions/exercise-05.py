### Exercise 5: Travel Itinerary Planner

""" 
Plan travel itineraries. Destinations are a dict {city (str): list of attractions (str)}. Take a city, loop through destinations, use conditionals to select attractions starting with 'M' (e.g., museums), handle errors if city not found, store selected attractions in a set (unique), and return a tuple of (selected_attractions_set, all_cities_list). 
"""




def plan_itinerary(destinations, target_city):
    """
    Plans travel itinerary by selecting specific attractions.
    
    :param destinations: dict - {city: [attractions]}
    :param target_city: str - City to plan for
    :return: tuple - (selected_attractions_set, all_cities_list)
    """
    # Error handling: Check if target_city exists
    try:
        if target_city not in destinations:
            raise ValueError(f"City '{target_city}' not found.")
    except ValueError as e:
        return set(), []  # Return empty on error
    
    # Initialize variables
    selected_attractions = set()  # Set for unique selected
    all_cities = list(destinations.keys())  # List of all cities
    
    # Loop through destinations (though focus on target)
    for city, attractions in destinations.items():
        if city == target_city:
            # Loop through attractions
            for attr in attractions:
                # Conditional: Select if starts with 'M'
                if attr.startswith('M'):
                    selected_attractions.add(attr)  # Add to set
    
    # Return results as tuple
    return selected_attractions, all_cities

# Example usage
destinations = {
    "Paris": ["Eiffel Tower", "Museum Louvre"],
    "New York": ["Statue of Liberty", "Museum of Modern Art"]
}


print(plan_itinerary(destinations, "Paris"))  # Example call
