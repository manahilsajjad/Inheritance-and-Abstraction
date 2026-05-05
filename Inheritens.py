class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print("Name:", self.name)
        print("ID:", self.id)

class Employee(Person):
    def __init__(self, job, salary , name, id):
        self.job= job
        self.salary = salary
        Person.__init__(self, name, id)
obj=Employee("Doctor", 10000, "John", 101)
obj.display()


