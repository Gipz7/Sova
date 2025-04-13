import turtle
import random

# Налаштування екрану
screen = turtle.Screen()
screen.bgcolor("skyblue")
screen.title("Малюнок лісу")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

def draw_tree(x, y, trunk_height=60, foliage_radius=30):
    """Малює одне дерево на координатах x, y"""
    pen.penup()
    pen.goto(x, y)
    pen.setheading(90)
    pen.color("saddlebrown")
    pen.pendown()
    
    # Стовбур
    pen.begin_fill()
    for _ in range(2):
        pen.forward(trunk_height)
        pen.right(90)
        pen.forward(10)
        pen.right(90)
    pen.end_fill()

    # Крона
    pen.penup()
    pen.goto(x + 5, y + trunk_height)
    pen.setheading(0)
    pen.color("forestgreen")
    pen.begin_fill()
    pen.circle(foliage_radius)
    pen.end_fill()

# Намалюємо багато дерев
for _ in range(10):
    x = random.randint(-300, 300)
    y = random.randint(-200, 0)
    trunk = random.randint(40, 80)
    foliage = random.randint(20, 40)
    draw_tree(x, y, trunk, foliage)

# Затримка, щоб побачити результат
screen.mainloop()
