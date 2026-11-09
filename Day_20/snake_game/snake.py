from turtle import Turtle

MOVE_DISTANCE = 20


class Snake:
    def __init__(self, coordinates, color, num_of_segments):
        self.coordinates = coordinates
        self.color = color
        self.num_of_segments = num_of_segments
        self.all_segments = []

    def create_snake(self):
        for turtle_index in range(0, self.num_of_segments):
            segment = Turtle(shape="square")
            segment.color(self.color)
            segment.penup()
            segment.goto(self.coordinates[turtle_index])
            self.all_segments.append(segment)

    def move(self):
        for seg_num in range(len(self.all_segments) - 1, 0, -1):
            # last segment will go to the position of the former segment
            former_x_pos = self.all_segments[seg_num - 1].xcor()
            former_y_pos = self.all_segments[seg_num - 1].ycor()
            self.all_segments[seg_num].goto(former_x_pos, former_y_pos)

        self.all_segments[0].forward(MOVE_DISTANCE)
