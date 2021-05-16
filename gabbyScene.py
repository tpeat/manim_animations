from manim import*
import requests
from PIL import Image
import manim.utils.color as C
from manimlib.mobject.svg.tex_mobject import TexMobject


#works better but is a simplier "cheat" code, not a real array
class PixelArray(Scene):
    def construct(self):
        row1 = dict()
        row2 = dict()
        row3 = dict()
        var_index=2
        for x in np.arange(-1.5, 1.5, 1.0):
            row1[f"{var_index}"] = Dot(np.array([x,0,0]),radius=.20)
            var_index = var_index+1
        for x in np.arange(-1.5, 1.5, 1.0):
            row2[f"{var_index}"] = Dot(np.array([x,1,0]),radius=.20)
            var_index = var_index+1
        for x in np.arange(-1.5, 1.5, 1.0):
            row3[f"{var_index}"] = Dot(np.array([x,2,0]),radius=.20)
            var_index = var_index+1
        for dot in row3.values():
            dot.set_color(C.GREEN_C)
            print(x)
            self.add(dot)
            self.wait(0.5)
        for dot in row2.values():
            dot.set_color(C.BLUE_A)
            self.add(dot)
            self.wait(0.5)
        for dot in row1.values():
            dot.set_color(C.GOLD_C)
            self.add(dot)
            self.wait(0.5)
        self.wait()
        self.clear()
        col1 = dict()
        text1 = dict()
        col2 = dict()
        text2 = dict()
        col3 = dict()
        text3 = dict()
        for x in np.arange(-1.5, 1.5, 1.0):
            col1[f"{var_index}"] = Dot(np.array([x,0,0]),radius=.20)
            text1[f"{var_index}"] = TexMobject("{x},0,0", size = .25)
            var_index = var_index+1
        for x in np.arange(1.5, 4.5, 1.0):
            col2[f"{var_index}"] = Dot(np.array([x,0,0]),radius=.20)
            var_index = var_index+1
        for x in np.arange(4.5, 7.5, 1.0):
            col3[f"{var_index}"] = Dot(np.array([x,0,0]),radius=.20)
            var_index = var_index+1
        y_val = 0
        for dot,text in zip(col1.values(), text1):
            dot.set_color(C.GREEN_C)
            dotLabel = Text(f"(0,{y_val})",size = .25)
            self.add(dot.shift(3*LEFT))
            self.add(dotLabel.move_to(dot.get_center()))
            y_val = y_val+1
            self.wait()
        y_val = 0
        for dot in col2.values():
            dot.set_color(C.BLUE_C)
            dotLabel = Text(f"(1,{y_val})",size = .25)
            self.add(dot.shift(3*LEFT))
            self.add(dotLabel.move_to(dot.get_center()))
            y_val = y_val+1
            self.wait()
        y_val = 0
        for dot in col3.values():
            dot.set_color(C.GOLD_C)
            dotLabel = Text(f"(2,{y_val})",size = .25)
            self.add(dot.shift(3*LEFT))
            self.add(dotLabel.move_to(dot.get_center()))
            y_val = y_val+1
            self.wait()
        self.wait()
        
