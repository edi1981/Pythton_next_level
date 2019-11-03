import turtle
def draw_triangle(some_turtle):
    # creating a triangle
    for i in range(1,4):
        some_turtle.forward(100)
        some_turtle.right(120)

def draw_circle(some_circle):
    # creating a cicrcle raduis 100
        some_circle.circle(110)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("#000000")
    # Creting a brad turtle
    brad = turtle.Turtle()
    brad.color("white")
    brad.shape("classic")
    brad.speed(20)
    for i in range(1,37):
        brad.right(10)
        draw_triangle(brad)

    # creating an angie Turtle
    angie = turtle.Turtle()
    angie.color("green")
    angie.speed(20)
    for i in range(1,37):
        angie.right(10)
        draw_circle(angie)

    window.exitonclick()
draw_art()