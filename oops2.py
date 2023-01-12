class Employee:
    no_of_leaves = 8
    pass

harry = Employee()
rohan = Employee()

harry.name = "Harry"
harry.salary = 455
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 45
rohan.role = "Student"

print(rohan.name,harry.salary,harry.no_of_leaves)
