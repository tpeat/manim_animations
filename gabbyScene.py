from manim import*
import requests
from PIL import Image
import manim.utils.color as C
from manimlib.mobject.svg.tex_mobject import TexMobject


#works better but is a simplier "cheat" code, not a real array
class PixelArray(Scene):
    def construct(self):
        #creates basic images of stacked rectangles with unique colors
        rect1 = Rectangle(height = 1, width = 3, fill_opacity = 1, fill_color = GREEN_C, color= GREEN_C)
        rect2 = Rectangle(height = 1, width = 3, fill_opacity = 1, fill_color = BLUE_C, color= BLUE_C)
        rect3 = Rectangle(height = 1, width = 3, fill_opacity = 1, fill_color = GOLD_C, color= GOLD_C)
        self.add(rect1.shift(UP).shift(LEFT))
        self.add(rect2.shift(LEFT))
        self.add(rect3.shift(DOWN).shift(LEFT))
        self.wait(1.5)
        row1 = dict()
        row2 = dict()
        row3 = dict()
        var_index=2
        
        #creates dots for 3x3 
        for x in np.arange(-1.5, 1.5, 1.0):
            row1[f"{var_index}"] = Dot(np.array([x,0,0]),radius=.20)
            var_index = var_index+1
        for x in np.arange(-1.5, 1.5, 1.0):
            row2[f"{var_index}"] = Dot(np.array([x,1,0]),radius=.20)
            var_index = var_index+1
        for x in np.arange(-1.5, 1.5, 1.0):
            row3[f"{var_index}"] = Dot(np.array([x,2,0]),radius=.20)
            var_index = var_index+1
        
        #fades each ractangle and replaces them with dots of corresponding color
        self.play(FadeOut(rect1))
        y_val = 0
        for dot in row3.values():
            dot.set_color(C.GREEN_C)
            dotLabel = Text(f"(0,{y_val})",size = .25)
            self.add(dot.shift(DOWN))
            self.add(dotLabel.move_to(dot.get_center()))
            y_val = y_val+1
            self.wait(0.5)
        self.play(FadeOut(rect2))
        y_val = 0
        for dot in row2.values():
            dot.set_color(C.BLUE_C)
            dotLabel = Text(f"(1,{y_val})",size = .25)
            self.add(dot.shift(DOWN))
            self.add(dotLabel.move_to(dot.get_center()))
            y_val = y_val+1
            self.wait(0.5)
        self.play(FadeOut(rect3))
        y_val = 0
        for dot in row1.values():
            dot.set_color(C.GOLD_C)
            dotLabel = Text(f"(2,{y_val})",size = .25)
            self.add(dot.shift(DOWN))
            self.add(dotLabel.move_to(dot.get_center()))
            y_val = y_val+1
            self.wait(0.5)
        self.wait()
        
        #could maybe split class here if this class is too long (top half shows pcture as array; bottom half shows iterations through pixels)

        #creates dots for 1x9
        col1 = dict()
        col2 = dict()
        col3 = dict()
        for x in np.arange(-1.5, 1.5, 1.0):
            col1[f"{var_index}"] = Dot(np.array([x,0,0]),radius=.20)
            var_index = var_index+1
        for x in np.arange(1.5, 4.5, 1.0):
            col2[f"{var_index}"] = Dot(np.array([x,0,0]),radius=.20)
            var_index = var_index+1
        for x in np.arange(4.5, 7.5, 1.0):
            col3[f"{var_index}"] = Dot(np.array([x,0,0]),radius=.20)
            var_index = var_index+1
            
        #adds dots in line
        y_val = 0
        for dot in col1.values():
            dot.set_color(C.GREEN_C)
            dotLabel = Text(f"(0,{y_val})",size = .25)
            self.add(dot.shift(3*LEFT).shift(3*DOWN))
            self.add(dotLabel.move_to(dot.get_center()))
            y_val = y_val+1
            self.wait(0.5)
        y_val = 0
        for dot in col2.values():
            dot.set_color(C.BLUE_C)
            dotLabel = Text(f"(1,{y_val})",size = .25)
            self.add(dot.shift(3*LEFT).shift(3*DOWN))
            self.add(dotLabel.move_to(dot.get_center()))
            y_val = y_val+1
            self.wait(0.5)
        y_val = 0
        for dot in col3.values():
            dot.set_color(C.GOLD_C)
            dotLabel = Text(f"(2,{y_val})",size = .25)
            self.add(dot.shift(3*LEFT).shift(3*DOWN))
            self.add(dotLabel.move_to(dot.get_center()))
            y_val = y_val+1
            self.wait(0.5)
        self.wait()
        
        #explains the pixel coordinates (maybe wanna add a method name["(getX,getY)"]
        array = Text(f"pixel  coordinates -> [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]",size = .35)
        self.add(array.shift(2*DOWN))
        self.wait()
        
