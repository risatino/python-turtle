import turtle

s = turtle.Screen()
s.bgcolor('#7EC0EE')
turtle.color('#FF3366')

pizza = turtle.Turtle()
pizza.color('#FF3366')

def drawSquares(john, size, num, angle):

    for i in range(num):
        for x in range(4):
            pizza.forward(size)
            pizza.left(90)
        pizza.right(angle)

drawSquares(pizza, 125, 36, -10)

s.exitonclick()

# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.right(-10)

# sun = turtle.Turtle()
# sun.color('#FFCC00')
# sun.circle(15)
