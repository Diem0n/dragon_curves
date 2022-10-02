R = "R"
L = "L"

sequence = ''


def iterate(sequence: str) -> str:
    sequence = sequence + R + swapLetters(sequence[::-1])
    return sequence


def swapLetters(sequence: str) -> str:
    newSequence = ""
    for letter in sequence:
        if letter == R:
            newSequence = newSequence + L
        else:
            newSequence = newSequence + R
    return newSequence


def dragon(n_iterations: int) -> str:
    """Takes in a number n, an return the dragon curve sequence i.e.:
    When n=2, returns "RRL"

    Args:
        n_iterations (int): number of iterations of the dragon curve

    Returns:
        str: The dragon curve Sequence
    """
    initial_sequence = R
    for i in range(0, n_iterations):
        initial_sequence = iterate(initial_sequence)
    return initial_sequence


sequence = sequence + R + swapLetters(sequence[::-1])

from turtle import Turtle, Screen

turtle = Turtle("turtle")
turtle.hideturtle()
turtle.speed("fast")
turtle.color("#ff69aa")

# Screen Setup
screen = Screen()
screen.title("Dragon Curve")
screen.bgcolor("white")
screen.screensize(720, 720)
screen.setup( startx=None, starty=None)

# Draw
LENGTH = 10
turtle.forward(LENGTH)
for element in dragon(17):
    if element == R:
        turtle.right(90)
        turtle.forward(LENGTH)
    else:
        turtle.left(90)
        turtle.forward(LENGTH)

turtle.color("red")
turtle.write("click to exit", font=("Calibri", 16, "bold"))
screen.exitonclick()

