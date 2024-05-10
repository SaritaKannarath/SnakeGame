from turtle import Turtle, Screen  # Importing necessary modules
from Snake import Snake  # Importing the Snake class
from food import Food  # Importing the Food class
from scoreboard import Scoreboard  # Importing the Scoreboard class
import time  # Importing the time module

# Setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)  # Turning off automatic screen updates

# Creating the snake object
snake = Snake()

# Listening for keyboard input
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Creating the food object and the scoreboard object
food = Food()
score = Scoreboard()

game_is_on = True  # Variable to control the game loop
while game_is_on:
    screen.update()  # Updating the screen manually
    time.sleep(0.5)  # Delay to control the speed of the game

    snake.move()  # Moving the snake

    # Checking for collision with food and updating score
    if snake.head.distance(food) < 15:
        food.refresh()
        score.update_score()
        snake.extend()

    # Checking for collision with wall and ending the game if collided
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    # Checking for collision with itself and ending the game if collided
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

# Allowing the user to exit the game by clicking on the screen
screen.exitonclick()
