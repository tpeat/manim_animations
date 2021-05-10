from manim import *
import requests
from PIL import Image


class helloWorld(Scene):
    def construct(self):
        title = Text("Welcome to pictures!")
        self.play(Write(title))
        self.wait(3)
        self.play(FadeOut(title))
      
        screen = ScreenRectangle(height=6)
        screen.set_fill(BLACK, 1)
        screen.set_stroke(BLUE,3)
        screen.to_edge(DOWN)

        picture = ImageMobject(Image.open(requests.get("https://i.natgeofe.com/n/8c395689-5233-434c-8a1e-bd34af03b59f/84731.jpg?w=1024&h=767", stream=True).raw)).scale(.75)
        self.add(FullScreenRectangle())

        self.play(Write(Text("The Breakdown").to_corner(DOWN + LEFT)))
        self.add(picture)

        dots = dict()
        var_index = 3
        for x in np.arange(-2.75,3,.25):
            for y in np.arange(-2.0,2.2,.25):
                dots[f"{var_index}"] = Dot(np.array([x, y, 0]),radius=.05)
                var_index = var_index + 1
        for dot in dots.values():
            self.add(dot)
            self.wait(0.02)

        
        self.wait()
        
class DotMap(Scene):
    def construct(self):

        dots = dict()
        var_index = 2 
        for x in np.arange(-3.0,4.0,.5):
            for y in np.arange(-2.0,2.0,.5):
                dots[f"{var_index}"] = Dot(np.array([x, y, 0]),radius=.05)
                var_index = var_index + 1
        for dot in dots.values():
            self.add(dot)
            self.wait(0.05)
        
        self.wait()
        

class ZoomedOnPixel(ZoomedScene):
    def __init__(self, **kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.1,
            zoomed_display_height=5,
            zoomed_display_width=6,
            image_frame_stroke_width=20,
            zoomed_camera_config={
                "default_frame_stroke_width": 3,
                },
            **kwargs
        )
    def construct(self):
        frame_text=Text("Pixel",color=PURPLE).scale(1.4)
        zoomed_camera_text=Text("Pixel",color=RED).scale(1.4)
        
        dotmap =  VGroup(
                *[
                    VGroup(
                        *[
                            Dot()
                            for x in np.arange(-3.0,4.0,.5)
                        ]
                    ).arrange_submobjects(RIGHT)
                    for y in np.arange(-2.0,2.0,.5)
                ]
            ).arrange_submobjects(DOWN)


        self.add(dotmap)
        self.wait()

        #set cameara
        zoomed_camera = self.zoomed_camera
        zoomed_display = self.zoomed_display
        frame = zoomed_camera.frame
        zoomed_display_frame = zoomed_display.display_frame

        frame.move_to(dotmap.get_corner(UP+LEFT)*.985)
        frame.set_color(PURPLE)

        zoomed_display_frame.set_color(RED)
        zoomed_display.shift(DOWN)


        # brackground zoomed_display
        zd_rect = BackgroundRectangle(
            zoomed_display,
            fill_opacity=0,
            buff=3,
        )

        self.add_foreground_mobject(zd_rect)
        unfold_camera = UpdateFromFunc(
            zd_rect,
            lambda rect: rect.replace(zoomed_display)
        )

        frame_text.next_to(frame,DOWN)

        self.play(
            ShowCreation(frame),
            FadeIn(frame_text)
        )

        # Activate zooming
        self.activate_zooming()

        self.play(
            # You have to add this line
            self.get_zoomed_display_pop_out_animation(),
            unfold_camera
            )

        zoomed_camera_text.next_to(zoomed_display_frame, DOWN)
        self.play(Write(zoomed_camera_text))

        self.wait()
        

class ColorChannels(Scene):
    def construct(self):
        channel_title = Text("Color Channels").shift(UP*2)
        pix_label = Text("Pixel", color=RED).scale(1.4)
        c1 = Circle(color=WHITE,fill_opacity=1)
        c2 = Circle(color=WHITE, fill_opacity=1)
        c3 = Circle(color=WHITE, fill_opacity=1)
        self.play(Write(channel_title))
        display = VGroup()
        self.add(display)
        display.add(c1,c2,c3)
        self.play(Write(pix_label.next_to(c1,DOWN)))
        self.wait(4)
        self.play(FadeOut(pix_label))
        
        self.play(c2.animate.shift(LEFT*2), c3.animate.shift(RIGHT*2))
        self.play(FadeToColor(c2,RED), FadeToColor(c1,GREEN), FadeToColor(c3,BLUE))
        num_values = Text("Color channel values are ints ranging from 0-255").scale(.6)
        self.play(FadeIn(num_values.next_to(c1,DOWN)))
        self.wait()

        t1 = Text("71")
        t2 = Text("209")
        t3 = Text("189")
        self.play(
                Write(t1.move_to(c1.center())),
                Write(t2.move_to(c2.get_center())),
                Write(t3.move_to(c3.get_center()))
        ) 
        pink = Circle(color=PINK, fill_opacity=1)

        self.play(FadeOut(t1),FadeOut(t2),FadeOut(t3),ReplacementTransform(display,pink))
        self.wait()  

class Locations(Scene):
    def construct(self):
        title = Text("Locations on pictures")




#Unzipping of images using for loops

#Do I want to any manipulations:








