length=float(input("Enter length: "))
width=float(input("Enter width: "))
height=float(input("Enter height: "))
def surface_area():
    surfacearea=2 * (length * width + length * height + width * height)
    print("The surface area is:", surfacearea)
surface_area()
def volume():
    volume=length * width * height
    print("The volume is:", volume)
volume()
