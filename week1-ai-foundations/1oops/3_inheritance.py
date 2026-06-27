#write a program for multilevel inheritance 
class A:
    def __init__(self):
        print("I am A class Constructor");
    def display(self):
        print("I am A class Display Method");
class B(A):
    def __init__(self):
        print("I am B class Constructor");
    def show(self):
        print("I am B class show method");
class C(B):
    def __init__(self):
        print("I am c Class Constructor");
    def output(self):
        print("I am C class output method");
c1=C();
c1.display();
c1.show();
c1.output();