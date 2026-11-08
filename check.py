7 
sides=int(input("enter the sides of the shape"))
len1=int(input("enter the length of the side"))
angle=360/sides
from turtle import*
for i in range(0,sides):
    forward(len1)
    left(angle)