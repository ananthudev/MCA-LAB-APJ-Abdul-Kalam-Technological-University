from graphics.rectangle import *
from graphics.circle import *
from graphics.tdgraphics.sphere import *
from graphics.tdgraphics.cuboid import *

print("Select operation.")
print("1.Rectangle")
print("2.Circle")
print("3.Sphere")
print("4.Cuboid")
print("5.Exit")

while True:
    choice = input("Enter choice(1/2/3/4/5): ")
    if choice in ('1', '2', '3', '4', '5'):
        if choice == '1':
            l = int(input("Enter the length of rectangle:"))
            b = int(input("Enter the breadth of rectangle:"))
            print("Area of rectangle=", rectarea(l, b))
            print("Perimeter of rectangle=", rectperi(l, b))
        elif choice == '2':
            r = int(input("Enter the radius of circle:"))
            print("Area of circle=", circlearea(r))
            print("Perimeter of circle=", circleperi(r))
        elif choice == '3':
            sr = int(input("Enter the radius of sphere:"))
            print("Area of sphere=", spherearea(sr))
            print("Perimeter of sphere=", sphereperi(sr))
        elif choice == '4':
            cl = int(input("Enter the length of cuboid:"))
            w = int(input("Enter the width of cuboid:"))
            h = int(input("Enter the height of cuboid:"))
            print("Area of cuboid=", cuboidarea(cl, w, h))
            print("Perimeter of cuboid=", cuboidperi(cl, w, h))
        elif choice == '5':
            exit(0)
        else:
            print("Invalid Input")
    else:
        print("Invalid Input")
