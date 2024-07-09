import turtle
import sys

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        size /= 3.0
        koch_curve(t, order-1, size)
        t.left(60)
        koch_curve(t, order-1, size)
        t.right(120)
        koch_curve(t, order-1, size)
        t.left(60)
        koch_curve(t, order-1, size)

def koch_snowflake(t, order, size):
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

def main():
    if len(sys.argv) != 2:
        print("Usage: python koch_snowflake.py <recursion_level>")
        sys.exit(1)

    try:
        order = int(sys.argv[1])
        if order < 1 or order > 5:
            raise ValueError("Recursion level must be between 1 and 5.")
    except ValueError as e:
        print(e)
        sys.exit(1)

    size = 300  # Size of the snowflake

    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-150, 100)
    t.pendown()

    koch_snowflake(t, order, size)

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()
