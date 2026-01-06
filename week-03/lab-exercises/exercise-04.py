
### Exercise 4: Employee Directory Search

""" 
Implement an employee search for a company. Employees are a list of tuples (id (int), name (str), department (str), salary (float)). The program should take a department name, loop through employees, use conditionals to filter by salary > 50000, handle errors if no employees in department, store high-salary ids in a set, and return a dictionary of {department: high_salary_count}. 
"""



def search_employees(employees, target_dept):
    # Loop through employees
    # Error handling for no employees in dept
    # Conditional for salary filter
    # Use set for high-salary ids
    # Return dict of {department: high_salary_count}
    pass


# Example usage
employees = [
    (1, "Alice", "HR", 60000.0),
    (2, "Bob", "IT", 45000.0),
    (3, "Charlie", "HR", 55000.0)
]
print(search_employees(employees, "HR"))  # Example call

