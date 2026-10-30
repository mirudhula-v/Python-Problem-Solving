#Personalized Greeting
a=str(input())
print(f"Hi {a}, welcome to the programming class!")
#Calculate Total and Average Marks
name=input()
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
total=a+b+c+d+e
average=total/5
print("Student Name:", name)
print("Total Marks:", total)
print("Average Marks:", f"{average:.2f}")
#Shape Area Calculation
a = int(input())
l = int(input())
b = int(input())
r = int(input())
B = int(input())
h = int(input())
square = a * a
rectangle = l * b
circle = 3.14 * r * r
triangle = 0.5 * B * h
print("Area of Square=", square, sep="")
print("Area of Rectangle=", rectangle, sep="")
print(f"Area of Circle={circle:.2f}")
print("Area of Triangle=", int(triangle) if triangle.is_integer() else triangle, sep="")
#Shape Perimeter Calculation Program
a=int(input())
l=int(input())
w=int(input())
r=int(input())
s1=int(input())
s2=int(input())
B=int(input())
square=4*a
rectangle=2*(l+w)
circle=2*3.14*r
triangle=s1+B+s2
print(square)
print(rectangle)
print(f"{circle:.2f}")
print(triangle)
#Handling Mixed Inputs
a=int(input())
b=input()
print(a)
print(b)
