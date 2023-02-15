class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        
    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return 2 * (self.length + self.breadth)
    
    
r1 = Rectangle(int(input("Enter the length of rectangle 1: ")), int(input("Enter the breadth of rectangle 1: ")))
r2 = Rectangle(int(input("Enter the length of rectangle 2: ")), int(input("Enter the breadth of rectangle 2: ")))

print("Area of Rectangle 1 = ", r1.area())
print("Perimeter of Rectangle 1 = ", r1.perimeter())

print("Area of Rectangle 2 = ", r2.area())
print("Perimeter of Rectangle 2 = ", r2.perimeter())

if r1.area() == r2.area():
    print("Areas are the same")
else:
    print("Areas are different")
