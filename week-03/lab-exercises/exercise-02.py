### Exercise 2: Student Grading System
""" 
Create a system for a school to process student grades. Students are stored in a list of dictionaries, each with keys 'name' (str), 'grades' (list of ints), 'attendance' (int). The program should loop through students, use conditionals to determine pass/fail (average grade >= 70 and attendance >= 80), handle errors if grades list is empty, store failing students in a set, and return a tuple of (passing_count, failing_names_set). 
"""



def process_grades(students):
    # Loop through students
    # Error handling for empty grades
    # Conditional for pass/fail
    # Use set for failing students
    # Return tuple of (passing_count, failing_names_set)
    pass


# Example usage
students = [
    {'name': 'Alice', 'grades': [85, 90, 78], 'attendance': 90},
    {'name': 'Bob', 'grades': [65, 70, 60], 'attendance': 75},
    {'name': 'Charlie', 'grades': [], 'attendance': 85}  # Will trigger error
]
print(process_grades(students))  # Example call

