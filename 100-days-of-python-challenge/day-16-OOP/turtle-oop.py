import turtle

tom = turtle.Turtle()
tom.color("blue")
tom.pensize(5)
tom.shape("turtle")
for _ in range(4):
    tom.forward(100)
    tom.right(90)
    tom.backward(50)
    tom.left(90)
print(tom)

screen = turtle.Screen()
screen.exitonclick()
print(screen)