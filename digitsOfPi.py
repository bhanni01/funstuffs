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

        for point in range(numPoints):
            point = circle.point_at_angle(point*(PI/5))
            dot = Circle(radius=0.05, color=WHITE).move_to(point)
            self.add(circle, dot)



