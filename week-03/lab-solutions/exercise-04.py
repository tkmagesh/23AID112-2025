
### Exercise 4: Employee Directory Search

""" 
Implement an employee search for a company. Employees are a list of tuples (id (int), name (str), department (str), salary (float)). The program should take a department name, loop through employees, use conditionals to filter by salary > 50000, handle errors if no employees in department, store high-salary ids in a set, and return a dictionary of {department: high_salary_count}. 
"""

def search_employees(employees, target_dept):
    """
    Searches employees by department and filters high-salary ones.
    
    :param employees: list of tuples - (id, name, dept, salary)
    :param target_dept: str - Department to search
    :return: dict - {department: high_salary_count}
    """
    # Initialize variables
    high_salary_ids = set()  # Set for unique high-salary employee ids
    dept_count = {target_dept: 0}  # Dict for count
    
    # Flag for error handling
    found_in_dept = False
    
    # Loop through each employee
    for emp in employees:
        emp_id, name, dept, salary = emp  # Unpack tuple
        
        # Conditional: Only process if dept matches
        if dept == target_dept:
            found_in_dept = True
            # Conditional: Check salary > 50000
            if salary > 50000:
                high_salary_ids.add(emp_id)  # Add to set
                dept_count[target_dept] += 1  # Increment count
    
    # Error handling: If no employees in dept
    try:
        if not found_in_dept:
            raise ValueError(f"No employees in department '{target_dept}'.")
    except ValueError as e:
        print(e)  # Log error
        return {}  # Return empty dict on error
    
    # Return the dict
    return dept_count


# Example usage
employees = [
    (1, "Alice", "HR", 60000.0),
    (2, "Bob", "IT", 45000.0),
    (3, "Charlie", "HR", 55000.0)
]
print(search_employees(employees, "HR"))  # Example call

