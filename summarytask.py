length=float(input("Enter length: "))
width=float(input("Enter width: "))
height=float(input("Enter height: "))
def surface_area(length,width,height):
    return 2 * (length * width + length * height + width * height)
def volume(length,width,height):
    return length * width * height
SA=surface_area(length,width,height)
Vol=volume(length,width,height)
print("The surface area of the cuboid is",SA )
print("The volume of the cuboid is", Vol)
