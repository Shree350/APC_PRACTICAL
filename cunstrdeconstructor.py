
# class Student:
#     def __init__(self, name):
#         self.name = name
#         print("Constructor called")

#     def display(self):
#         print("Student Name:", self.name)

#     def __del__(self):
#         print("Destructor called")


# s1 = Student("Rahul")
# s1.display()
# del s1


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(self.name, self.salary)

    def __del__(self):
        print("Employee object deleted")


e1 = Employee("Amit", 25000)
e1.display()
del e1
