# Finding area and perimeter of a triangle (all sides are given) also find all 3 angles of that triangle

import math
a = float(input("Enter the length of side a : "))
b = float(input("Enter the length of side b : "))
c = float(input("Enter the length of side c : "))

# Perimeter
perimeter = a + b + c
print("Perimeter of the triangle is : ", perimeter)

# Area
s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print("Area of the triangle is : ", area)

# Angles

angle_a = math.degrees(math.acos(((c * c) + (b * b) - (a * a)) / (2 * b * c)))
angle_b = math.degrees(math.acos(((a * a) + (c * c) - (b * b)) / (2 * a * c)))
angle_c = math.degrees(math.acos(((b * b) + (a * a) - (c * c)) / (2 * b * a)))

print("Angles of the triangle are : ", angle_a, angle_b, angle_c)