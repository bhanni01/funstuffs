import turtle 
color =["red","blue","purple","white","yellow","orange"]
cursor = turtle.Pen()
turtle.bgcolor("black")
for c in range(360):
    cursor.pencolor(color[c % 6])
    cursor.width(c/100 + 1)
    cursor.forward(c)
    cursor.left(59)