#in this project i will be representing all digits of pi using a manim library you will be able to see a beautiful visualization at the end
from manim import *
# lets create a circle and have 10 points 0-9 marked with different color
class piArt(Scene):
    def construct(self):
        circle = Circle(radius = 2.0)
        # total number of points that we want to have
        numPoints = 10
        # lets try to create point in the circle 
        # each point should be created 36 degrees apart to each other , pi/10
        points ={}
        for point in range(numPoints):
            points["point{0}".format(point)]= circle.point_at_angle(point*(PI/5)) 
            
            # point = circle.point_at_angle(point*(PI/5))
            dot = Circle(radius=0.05, color=WHITE).move_to("point{0}".format(point))
            self.add(circle, dot)
        print(points)
# need to label those points in the circles from 0-9
# best way might be to create a dictionary and store all those commands in a dictionary
        

# ask for user how many pi decimals input they want
# get the value and store it and start connecting dots
