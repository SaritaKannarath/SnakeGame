from turtle import Turtle

# Constants defining starting position and movement settings
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """A class to represent the snake in the Snake game."""

    def __init__(self):
        """Initialize the Snake object."""
        self.segments = []  # List to hold the segments of the snake
        self.create_snake()  # Create the initial snake
        self.head = self.segments[0]  # Reference to the head segment of the snake

    def create_snake(self):
        """Create the snake with initial segments."""
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        """Add a new segment to the snake."""
        body_part = Turtle(shape="square")
        body_part.color('white')
        body_part.penup()
        body_part.goto(position)
        self.segments.append(body_part)

    def extend(self):
        """Extend the length of the snake by adding a new segment."""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Move the snake forward."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg_num - 1].xcor()
            y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x, y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Change the snake's direction to up."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Change the snake's direction to down."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Change the snake's direction to left."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Change the snake's direction to right."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
