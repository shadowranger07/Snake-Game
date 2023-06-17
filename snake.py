from turtle import Turtle, Screen
import time
position = 0,0

class Snake:

    def __init__(self):
        self.dd = []
        self.a = 0
        self.make()

    def make(self):
        self.add_segment(position)
    def add_segment(self, position):
        for _ in range(3):
            new_turtle = Turtle(shape="square")
            new_turtle.pu()
            new_turtle.color("white")
            new_turtle.goto(self.a, 0)
            self.dd.append(new_turtle)
            self.a -= 20

    def create(self):
        self.dd.clear()
        self.add_segment()
        self.head = self.dd[0]

    def extend(self):
        self.add_segment(self.dd[-1].position())
    def move(self):
        for seg_num in range(len(self.dd) - 1, 0, -1):
            new_x = self.dd[seg_num - 1].xcor()
            new_y = self.dd[seg_num - 1].ycor()
            self.dd[seg_num].goto(new_x, new_y)
        self.dd[0].forward(20)

    def up(self):
        if self.dd[0].heading() == 0:
            for seg_num in range(len(self.dd) - 1, 0, -1):
                new_x = self.dd[seg_num - 1].xcor()
                new_y = self.dd[seg_num - 1].ycor()
                self.dd[seg_num].goto(new_x, new_y)
            self.dd[0].left(90)
        else:
            for seg_num in range(len(self.dd) - 1, 0, -1):
                new_x = self.dd[seg_num - 1].xcor()
                new_y = self.dd[seg_num - 1].ycor()
                self.dd[seg_num].goto(new_x, new_y)
            self.dd[0].right(90)

    def down(self):
        if self.dd[0].heading() == 0:
            for seg_num in range(len(self.dd) - 1, 0, -1):
                new_x = self.dd[seg_num - 1].xcor()
                new_y = self.dd[seg_num - 1].ycor()
                self.dd[seg_num].goto(new_x, new_y)
            self.dd[0].right(90)
        elif self.dd[0].heading() == 180:
            for seg_num in range(len(self.dd) - 1, 0, -1):
                new_x = self.dd[seg_num - 1].xcor()
                new_y = self.dd[seg_num - 1].ycor()
                self.dd[seg_num].goto(new_x, new_y)
            self.dd[0].left(90)

    def left(self):
        if self.dd[0].heading() == 90:
            for seg_num in range(len(self.dd) - 1, 0, -1):
                new_x = self.dd[seg_num - 1].xcor()
                new_y = self.dd[seg_num - 1].ycor()
                self.dd[seg_num].goto(new_x, new_y)
            self.dd[0].left(90)
        elif self.dd[0].heading() == 270:
            for seg_num in range(len(self.dd) - 1, 0, -1):
                new_x = self.dd[seg_num - 1].xcor()
                new_y = self.dd[seg_num - 1].ycor()
                self.dd[seg_num].goto(new_x, new_y)
            self.dd[0].right(90)

    def right(self):
        if self.dd[0].heading() == 90:
            for seg_num in range(len(self.dd) - 1, 0, -1):
                new_x = self.dd[seg_num - 1].xcor()
                new_y = self.dd[seg_num - 1].ycor()
                self.dd[seg_num].goto(new_x, new_y)
            self.dd[0].right(90)
        elif self.dd[0].heading() == 270:
            for seg_num in range(len(self.dd) - 1, 0, -1):
                new_x = self.dd[seg_num - 1].xcor()
                new_y = self.dd[seg_num - 1].ycor()
                self.dd[seg_num].goto(new_x, new_y)
            self.dd[0].left(90)
    def head(self, funcx):
        s = int(self.dd[0].distance(funcx))
        return s

