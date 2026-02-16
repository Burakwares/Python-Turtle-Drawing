import turtle

drawing_Board = turtle.Screen()
drawing_Board.bgcolor("black")
drawing_Board.title("Python Turtle")
turtle_instance = turtle.Turtle()

'''
 # Triangle
 
for i in range(3):
    turtle_instance.forward(100)
    turtle_instance.left(120)
'''

'''
 # Square
 
for i in range(4):
    turtle_instance.forward(100)
    turtle_instance.right(90)

'''

''' 
 # Star
 
for i in range(5):
    turtle_instance.forward(100)
    turtle_instance.right(144)
'''

'''
 # ShrinkingSquare
 
for i in range(4):
    turtle_instance.forward(200)
    turtle_instance.right(90)
for i in range(4):
    turtle_instance.forward(100)
    turtle_instance.right(90)
for i in range(4):
    turtle_instance.forward(50)
    turtle_instance.right(90)
for i in range(4):
    turtle_instance.forward(25)
    turtle_instance.right(90)
'''

'''
 # Circles
turtle.speed(0)
turtle_colors = ["red","blue","orange","magenta","yellow"]

for i in range(10):
    turtle_instance.color(turtle_colors[i % 5])
    turtle_instance.circle(10 * i)
    turtle_instance.circle(-10 * i)
    turtle_instance.left(i)
'''

turtle.mainloop()
#turtle.done()
