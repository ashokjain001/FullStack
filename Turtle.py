import turtle

def drawsqaure():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("blue")
    brad.speed(4)
    for i in range(40):
        for i in range(4):
            brad.forward(100)
            brad.right(90)
        brad.right(10)
    window.exitonclick()
print drawsqaure()
