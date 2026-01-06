### Exercise 2: Student Grading System
""" 
Create a system for a school to process student grades. Students are stored in a list of dictionaries, each with keys 'name' (str), 'grades' (list of ints), 'attendance' (int). The program should loop through students, use conditionals to determine pass/fail (average grade >= 70 and attendance >= 80), handle errors if grades list is empty, store failing students in a set, and return a tuple of (passing_count, failing_names_set). 
"""

def process_grades(students):
    """
    Processes student grades and attendance to determine pass/fail status.
    
    :param students: list of dicts - [{'name': str, 'grades': [int], 'attendance': int}]
    :return: tuple - (passing_count, failing_names_set)
    """
    # Initialize variables
    passing_count = 0  # Int counter for passing students
    failing_names = set()  # Set for unique failing student names
    
    # Loop through each student
    for student in students:
        name = student['name']
        grades = student['grades']
        attendance = student['attendance']
        
        # Error handling: Check if grades list is empty
        try:
            if not grades:
                raise ValueError(f"Student '{name}' has no grades.")
        except ValueError as e:
            # Skip this student and log error (in real scenario, could handle differently)
            print(e)  # For demonstration
            continue
        
        # Calculate average grade
        avg_grade = sum(grades) / len(grades)  # Float division
        
        # Conditional branching: Check pass/fail criteria
        if avg_grade >= 70 and attendance >= 80:
            passing_count += 1  # Increment counter
        else:
            failing_names.add(name)  # Add to set
    
    # Return results as tuple
    return passing_count, failing_names


# Example usage
students = [
    {'name': 'Alice', 'grades': [85, 90, 78], 'attendance': 90},
    {'name': 'Bob', 'grades': [65, 70, 60], 'attendance': 75},
    {'name': 'Charlie', 'grades': [], 'attendance': 85}  # Will trigger error
]
print(process_grades(students))  # Example call
