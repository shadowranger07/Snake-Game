from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)



snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up" )
screen.onkey(snake.down,"Down" )
screen.onkey(snake.left,"Left" )
screen.onkey(snake.right,"Right" )



game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head(food) < 15 :
        food.refresh()
        snake.extend()
        score.score_increase()

    if snake.dd[0].xcor() > 290 or snake.dd[0].xcor() < -290 or snake.dd[0].ycor() > 290 or snake.dd[0].ycor() < -290:
        score.reset()
        snake.create()


    for segment in snake.dd[1:]:
        # if segment == snake.dd[0]:
        #     pass
        if snake.head(segment) < 10:
            score.reset()
            snake.create()

screen.exitonclick()