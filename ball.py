from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        
        self.x_speed = 5 
        self.y_speed = 5  

    def move(self):
        new_x = self.xcor() + self.x_speed
        new_y = self.ycor() + self.y_speed
        self.goto(new_x, new_y)
        
        self.x_speed *= 1.001  
        self.y_speed *= 1.001  

    def bounce_y(self):
        self.y_speed *= -1  

    def bounce_x(self):
        self.x_speed *= -1  

    def reset_position(self):
        self.goto(0, 0)
        self.x_speed *= -1  
