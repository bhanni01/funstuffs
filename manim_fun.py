from manim import *

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle=Triangle()
        
        three= ThreeDAxes()

        self.add(circle)
        self.wait()
        for figures in [square,triangle,three]:
            self.play(Transform(circle,figures))
        self.play(FadeOut(three))
