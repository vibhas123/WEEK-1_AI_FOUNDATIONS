#write a program using methods for Addition & multiplication of two numbers
class Addition:
    def input_values(self,a,b):
        self.a=a;
        self.b=b;
    def output(self):
        c=self.a + self.b;
        print("the sum of a and  b is : ",c);
        print("the mul of a and b is : ",(self.a*self.b));
add=Addition();
a=int(input("Enter the value of a is : "));
b=int(input("Enter the value of b is :"));
add.input_values(a,b);
add.output();