class Person:
    def __init__(self,name,occ):
        self.name = name
        self.occ = occ
    def info(self):
        print(f"{self.name} is a {self.occ}")
       
a = Person("Harry","Developer")
b = Person("Divya","HR")

# a.name = "Divya"
# a.occ = "HR"
a.info() 
b.info()