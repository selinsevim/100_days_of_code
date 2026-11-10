from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self, num_of_segments):
        self.num_of_segments = num_of_segments
        self.all_segments = []
        self.create_snake()
        self.head = self.all_segments[0]

    def create_snake(self):
        for turtle_index in range(0, self.num_of_segments):
            segment = Turtle(shape="square")
            segment.pen(fillcolor="black", pencolor="white")
            segment.penup()
            segment.goto(STARTING_POSITIONS[turtle_index])
            self.all_segments.append(segment)

    def add_segments(self):
        self.num_of_segments = self.num_of_segments + 1
        return self.num_of_segments

    def extend_snake(self):
        last_segment_position = self.all_segments[-1].position()
        segment = Turtle(shape="square")
        segment.pen(fillcolor="black", pencolor="white")
        segment.penup()
        segment.goto(last_segment_position)
        self.all_segments.append(segment)

    def move(self):
        for seg_num in range(len(self.all_segments) - 1, 0, -1):
            # last segment will go to the position of the former segment
            former_x_pos = self.all_segments[seg_num - 1].xcor()
            former_y_pos = self.all_segments[seg_num - 1].ycor()
            self.all_segments[seg_num].goto(former_x_pos, former_y_pos)

        self.head.forward(MOVE_DISTANCE)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
