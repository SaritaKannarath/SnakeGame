from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')

class Scoreboard(Turtle):
    """A class to represent the scoreboard in the Snake game."""

    def __init__(self):
        """Initialize the Scoreboard object."""
        super().__init__()
        self.score = 0  # Initial score
        self.penup()
        self.goto(0, 280)  # Position the scoreboard at the top center
        self.hideturtle()  # Hide the turtle icon
        self.color('white')  # Set the text color to white
        self.write(f'Score={self.score}', align=ALIGNMENT, font=FONT)  # Display initial score

    def update_score(self):
        """Update the score when the snake eats food."""
        self.score += 1  # Increment the score
        self.clear()  # Clear the previous score
        self.write(f'Score={self.score}', align=ALIGNMENT, font=FONT)  # Display the updated score

    def game_over(self):
        """Display 'GAME OVER' message."""
        self.goto(0, 0)  # Position the 'GAME OVER' message at the center
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)  # Display 'GAME OVER'
