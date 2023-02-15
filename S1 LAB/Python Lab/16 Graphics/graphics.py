from graphics.rectangle import rectarea, rectperi
from graphics.circle import circlearea, circleperi
from graphics.tdgraphics.sphere import spherearea, sphereperi
from graphics.tdgraphics.cuboid import cuboidarea, cuboidperi

print("Select operation.")
print("1. Rectangle")
print("2. Circle")
print("3. Sphere")
print("4. Cuboid")
print("5. Exit")

while True:
    choice = input("Enter choice (1/2/3/4/5): ")
    if choice in ('1', '2', '3', '4', '5'):
        if choice == '1':
            length = int(input("Enter the length of rectangle: "))
            breadth = int(input("Enter the breadth of rectangle: "))
            print("Area of rectangle: ", rectarea(length, breadth))
            print("Perimeter of rectangle: ", rectperi(length, breadth))
        elif choice == '2':
            radius = int(input("Enter the radius of circle: "))
            print("Area of circle: ", circlearea(radius))
            print("Circumference of circle: ", circleperi(radius))
        elif choice == '3':
            radius = int(input("Enter the radius of sphere: "))
            print("Surface area of sphere: ", spherearea(radius))
            print("Volume of sphere: ", sphereperi(radius))
        elif choice == '4':
            length = int(input("Enter the length of cuboid: "))
            width = int(input("Enter the width of cuboid: "))
            height = int(input("Enter the height of cuboid: "))
            print("Surface area of cuboid: ", cuboidarea(length, width, height))
            print("Volume of cuboid: ", cuboidperi(length, width, height))
        elif choice == '5':
            exit(0)
    else:
        print("Invalid input. Please enter a valid choice.")  
