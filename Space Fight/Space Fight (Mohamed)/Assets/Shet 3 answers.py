
#Q1


print(type(int(3.6)))
print(type(float(4)))
print(type(float(int(3.3))))
print(type(int(float(3))))
print((round(3.8)))
print(round(6.1))
print(int("32"))
print(float("32"))
print(float("32.5"))
print(type(eval("3.2")))
print(type(eval("3")))
print(eval("3 + 2"))

#Q2

a = 3
b = 4
c = a + b
print(c)
a=5
print(c) 


#Q3 Programming Exercises

#1)
x = eval(input("Enter The First Angle Here "))
y = eval(input("Enter The Second Angle Here "))
z = eval(input("Enter The Third Angle Here "))

if x + y + z == 180:
    print("Valid")
elif x == 0 or y == 0 or z == 0:
    print("Enter valid angles")
elif x < 0 or y < 0 or z < 0:
     print("Enter valid angles")
else:
    print("Invalid")

#2)
from math import *
k = eval(input("Enter the first side here "))
l = eval(input("Enter the second side here "))
m = eval(input("Enter the third side here "))

if k+l>m and k+m>l and l+m>k:
    print("Valid")
    halfP = (k+l+m)/2
    A = sqrt(halfP * (halfP-k) * (halfP-l) * (halfP-m))
    print("The Area is " + str(A))
elif k or l or m < 0:
    print("Enter Positive values")
elif k or l or m == 0:
    print("Do not enter zero")

#3)
from math import *
x = eval(input("Enter a number here "))
if type(x) == float:
    if x>0 and x <1:
        print("This number is float with",str(x) +" frational part")
    else:
        print("A float with ",str(floor(x)), "integer part" + " and " + str(x%floor(x)) + " Fractional part")
elif x == 0:
    print("This number is zero")

elif type(x) == int:
    if x % 2 == 0:
        print("This number is integer and even")
    else:
        print("This number is integer and odd")

#4)
x= eval(input("Enter your grade here "))

if x < 0 or x > 100:
    print("Write a valid number")
elif x > 90 and x < 100:
    print("You got an A")
elif x > 80 and x < 89:
    print("You got an B")
elif x > 70 and x < 79:
    print("You got an C")
elif x > 60 and x < 69:
    print("You got an B")
elif x < 60:
    print("You got an F")

    