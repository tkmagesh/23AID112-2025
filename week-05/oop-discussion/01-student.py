""" 
Object - encapsulates state (attributes) + behavior (methods)
Class - Template for creating an object
"""
class Student:
    """ 
    __init__ function will automatically execute whenever a new object is created using this class
    
    """
    def __init__(self):
        print("a new student object is created")
        self.id = 123
        self.name = "Magesh"
        self.location = "Bangalore"
        
    def whoAmI(self):
        print(self.id, self.name, self.location)


s1 = Student() # creating a new Student object
s1.whoAmI()

s2 = Student() # creating another new Student object
s2.whoAmI()

s3 = Student() # creating another new Student object
s3.whoAmI()