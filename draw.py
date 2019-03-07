import turtle

def draw_shape(object,shape):
    if (shape == "square"):
        side = 0
        while (side < 4):
            object.forward(100)
            object.right(90)
            side += 1
    elif (shape == "circle"):
        object.circle(50)

window = turtle.Screen()
window.bgcolor("yellow")
brad = turtle.Turtle()
brad.shape("turtle")
brad.color("blue")

for i in range(0,36):
    draw_shape(brad,"square")
    brad.right(10)
