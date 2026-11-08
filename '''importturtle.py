'''import turtle
t = turtle.Turtle()
mycolors = ['red', 'yellow','red', 'yellow','red', 'yellow','red', 'yellow',]
r = 10
n = 10
for i in range(n+1, 0, -1):
    t.color('white', mycolors[i%5])
    t.begin_fill()
    t.circle(r*i)
    t.end_fill()'''


import turtle
t = turtle.Turtle()
mycolors = ['red', 'yellow','red', 'yellow','red', 'yellow','red', 'yellow',]
r = 7
n = 100