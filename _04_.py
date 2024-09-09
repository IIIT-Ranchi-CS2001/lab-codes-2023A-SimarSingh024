# Finding Roots of Quadratic Equation
import math
a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))   
c = int(input("Enter the value of c : "))
d = (b*b) - (4*a*c)
if d==0:
    r = (-b)/(2*a)
    print("Roots are real and equal")
    print("Roots are : ",r)
elif d>0:
    r1 = ((-b) + (d**0.5))/(2*a)
    r2 = ((-b) - (d**0.5))/(2*a)
    print("Roots are real and distinct")
    print("Roots are : ",r1,r2)
else:
    print("Roots are imaginary")
    real = -b/(2*a)
    imag = (d**0.5)/(2*a)
    r1 = complex(real,imag)
    r2 = complex(real,-imag)
    print("Roots are : ",r1,"and",r2)