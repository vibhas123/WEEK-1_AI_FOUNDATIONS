#write a program to demonstrate the use of constructor in python
class Employee:
    
    def __init__(self,name,id,salary):
        self.name=name;
        self.id=id;
        self.salary=salary;
    def display(self):
        print("the name of the employee is : ",self.name);
        print("the id of the employee is ",self.id);
        print("the salary of the employee is ",self.salary);
employee1=Employee("b vibhas",2025012,10000010);
employee1.display();

