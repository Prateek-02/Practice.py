class Person:
    name = "Harry"
    occu = "Software engg"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occu} having net worth {self.networth}")

a = Person()
b = Person()
a.name = "Shubham"
a.occu = "Accountant"

b.name = "Nikita"
b.occu = "HR"

# print(a.name,a.occu)
a.info()
b.info()