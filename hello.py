class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name: object, salary: object) -> object:
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)

emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)

if(hasattr(emp1, 'age')):    # Returns true if 'age' attribute exists
    a = getattr(emp1, 'age') # Returns value of 'age' attribute
    print("Age of employee 1 : ", a)
else:
    num = input("Enter the age of Employee 1: ")
    setattr(emp1, 'age', num) # Set attribute 'age' at 8
    print("Employee 1's age is set to the: ", emp1.age)

print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)




class Point:
   def __init( self, x=0, y=0):
      self.x = x
      self.y = y
   def __del__(self):
      class_name = self.__class__.__name__
      print(class_name, "destroyed")

pt1 = Point()
pt2 = pt1
pt3 = [pt1]
print(id(pt1), id(pt2), id(pt3)) # prints the ids of the obejcts
del pt1
del pt2
del pt3



# delattr(empl, 'age')    # Delete attribute 'age'
