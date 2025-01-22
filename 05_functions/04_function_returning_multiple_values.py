# Problem: Create a function that returns both the area and circumference of a circle given its radius.
import math

def circle(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius

    return area,circumference

radius = float(input("Enter the radius of the circle: "))
area,circumference=circle(radius)

print(f"The area of circle having radius  {radius} is {area:.3f} and it's curcumference is {circumference:.3f}")

    