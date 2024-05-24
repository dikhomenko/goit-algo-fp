import turtle

def draw_tree(branch_length, depth):
    if depth > 0:
        turtle.forward(branch_length)
        turtle.left(45)
        draw_tree(branch_length * 0.6, depth - 1)
        turtle.right(90)
        draw_tree(branch_length * 0.6, depth - 1)
        turtle.left(45)
        turtle.backward(branch_length)

def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.title("Pythagoras Tree Fractal")

    turtle.speed(0)
    turtle.left(90)
    turtle.up()
    turtle.goto(0, -300)
    turtle.down()
    turtle.color("red", "yellow")

    # Prompt user for depth level
    depth = screen.numinput("Input", "Enter recursion depth:", minval=1, maxval=10)

    draw_tree(200, int(depth))
    
    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
