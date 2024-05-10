from turtle import Turtle
import random

class Food(Turtle):
    """A class to represent the food in the Snake game."""

    def __init__(self):
        """Initialize the Food object."""
        super().__init__()
        self.shape('circle')  # Set the shape of the food
        self.color('blue')  # Set the color of the food
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Set the size of the food
        self.penup()  # Lift the pen to prevent drawing lines
        self.speed('fastest')  # Set the speed of the food creation
        self.refresh()  # Place the food at a random position

    def refresh(self):
        """Move the food to a random position on the screen."""
        random_x = random.randint(-250, 250)  # Generate a random x-coordinate
        random_y = random.randint(-250, 250)  # Generate a random y-coordinate
        self.goto(random_x, random_y)  # Move the food to the random position
