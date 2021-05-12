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
        

# I think it would also be good to show how well known manipulations like Grayscale or Inversion/Negateive
#affect color channels 

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
        self.wait(3)

        t1 = Text("71")
        t2 = Text("209")
        t3 = Text("189")
        self.play(
                Write(t1.move_to(c1.get_center())),
                Write(t2.move_to(c2.get_center())),
                Write(t3.move_to(c3.get_center()))
        ) 
        pink = Circle(color=PINK, fill_opacity=1)

        self.play(FadeOut(t1),FadeOut(t2),FadeOut(t3),FadeOut(num_values),ReplacementTransform(display,pink))
        self.wait(3)
        self.play(FadeOut(pink),FadeOut(pix_label),FadeOut(channel_title))
        self.wait(3)
        

        grayscale = Text("Grayscaling").shift(UP*2)

        self.play(Write(grayscale))

        g1 = Circle(color=RED,fill_opacity=1)
        g2 = Circle(color=GREEN, fill_opacity=1)
        g3 = Circle(color=BLUE, fill_opacity=1)

        gray_container = VGroup(g1,g2,g3).arrange()
        inv_container = gray_container.copy()

        self.play(Create(gray_container))

        gt1 = Text("100")
        gt2 = Text("100")
        gt3 = Text("100")
        self.play(
                Write(gt1.move_to(g1.get_center())),
                Write(gt2.move_to(g2.get_center())),
                Write(gt3.move_to(g3.get_center()))
        ) 
        self.wait(3)

        self.play(FadeOut(gt1),FadeOut(gt2),FadeOut(gt3),ReplacementTransform(gray_container, Circle(color=GRAY, fill_opacity=1)))

         
        avg_text = Text("We often grayscale using the average of the RGB color channels").scale(.75).shift(DOWN*2)
        self.play(Write(avg_text))

        self.clear()

        #Inversion / Negative
        inv_title = Text("Negative / Inversion").shift(UP*2)
        self.play(Write(inv_title))
        
        self.play(Create(inv_container))

        n = 256
        imageArray = np.uint8(
            [[i * 256 / n for i in range(0, n)] for _ in range(0, 30)]
        )
        image = ImageMobject(imageArray).scale(5).shift(DOWN*2)

        self.add(image)
        
        self.wait()  
        



#Show the X and Y coordinates on a picture
class Locations(Scene):
    def construct(self): 
        picture = ImageMobject(Image.open(requests.get("https://i.natgeofe.com/n/8c395689-5233-434c-8a1e-bd34af03b59f/84731.jpg?w=1024&h=767", stream=True).raw)).scale(.75) 
        title = Text("Locations on pictures")
        
        rect = Rectangle(height=picture.get_height(), width=picture.get_width(), color=BLUE)

        self.add(picture)
        self.add(title.next_to(picture, UP))
        self.wait(3)

        #Creating the rectangle, fading out picture, and moving title
        self.play(Create(rect))
        self.play(FadeOut(picture))
        self.play(title.animate.shift(DOWN*5.5 + LEFT*3))

        #Creating braces that show width and height
        b1 = BraceBetweenPoints(rect.get_corner(LEFT+ UP), rect.get_corner(RIGHT+ UP), direction=[0,1,0])
        b1text = b1.get_text("Width of Picture").scale(.5)
        b2 = BraceBetweenPoints(rect.get_corner(DOWN+LEFT), rect.get_corner(UP + LEFT), direction=[-1,0,0])
        b2text = b2.get_text("Height of Picture").scale(.5)
    
        self.play(Create(b1),Write(b1text), Create(b2), Write(b2text))
        self.wait()

        #Fade out height and width braces
        self.play(FadeOut(b1),FadeOut( b1text),FadeOut( b2),FadeOut( b2text))
        dot = Dot(color=RED).move_to(rect.get_corner(UP + LEFT))
        dot2 = dot.copy().move_to(rect.get_center())                    # <------- Example of moving dot to location
        dot3 = dot.copy().move_to(rect.get_corner(DOWN + RIGHT))
        self.play(Create(dot))
        dot_label = Text("(0, 0)",size=.75).move_to(rect.get_corner(UL)*1.2)
        self.play(Write(dot_label))
        self.wait(2) 

        #Next for dot2 
        self.play(Create(dot2))
        dot2_label = Text("(w/2, h/2)",size=.75).move_to(rect.get_center()+UP)
        self.play(Write(dot2_label))
        
        #Dot 3
        self.play(Create(dot3))
        dot3_label = Text("(w, h)",size=.75).move_to(rect.get_corner(DOWN + RIGHT)*1.2)
        self.play(Write(dot3_label))
        self.wait()

#Indexing at locations

class ManipulateLocations(Scene):
    def construct(self):
        picture = ImageMobject(Image.open(requests.get("https://i.natgeofe.com/n/8c395689-5233-434c-8a1e-bd34af03b59f/84731.jpg?w=1024&h=767", stream=True).raw)).scale(.75) 
        title = Text("Manipulations at specific locations")
        
        rect = Rectangle(height=picture.get_height(), width=picture.get_width(), color=BLUE)
        display = VGroup()
        display.add(rect)   #<---- Adding rect to VGroup to be able to slide them both over


        self.add(picture)
        self.wait(3)

        rect2 = Rectangle(height=picture.get_height(), width=picture.get_width()/2,color=YELLOW,fill_opacity=.6)
        rect2.align_to(rect,LEFT)
        display.add(rect2)
        self.play(Create(rect2))

        self.add(title.next_to(picture, UP))
        self.wait(3)

        #Creating the rectangle, fading out picture, and moving title
        self.play(Create(rect))
        self.play(FadeOut(picture))
        self.play(title.animate.shift(DOWN*5.5 + LEFT*2))
        
        self.play(display.animate.shift(LEFT*3)) #<---- Shifts the display of rects left
        
        nested_x = Text("for x in range(pic.getWidth()):",size=.5)    #<----- Maybe it would 
        nested_y = Text("for y in range(pic.getHeight()):",size=.5).next_to(nested_x,DOWN).shift(RIGHT)
        get_pixel = Text("pix = getPixel(pic,x,y)",size=.5).next_to(nested_y,DOWN).shift(RIGHT*.5)
        nested = VGroup(nested_x,nested_y,get_pixel).shift(RIGHT*3)
        self.play(Write(nested))


        self.wait()

        #Unfinished! Needs to be done


#Unzipping of images using for loops

#Do I want to any manipulations:

# I think that doing a mirror could be pretty easy / cool
#Show just like picture locations and then use the Tau function to rotate it over its y axis for example


#We could show a blend function using the plane thing I think


class Blend(ThreeDScene):
    def construct(self):
        resolution_fa = 22
        self.set_camera_orientation(phi=75 * DEGREES, theta=-30 * DEGREES)

        text3d = Text("Blend Effect").to_corner(UL)
        self.add_fixed_in_frame_mobjects(text3d) #<----- Add this

        def param_plane(u, v):
            x = u
            y = v
            z = 0
            return np.array([x, y, z])

        pic = ParametricSurface(
            param_plane,
            resolution=(resolution_fa, resolution_fa),
            v_min=-2,
            v_max=+2,
            u_min=-2,
            u_max=+2,
        )
        def second_plane(u, v):
            x = u
            y = v
            z = 2 
            return np.array([x, y, z])

        pic2 = ParametricSurface(
            second_plane,
            resolution=(resolution_fa, resolution_fa),
            v_min=-2,
            v_max=+2,
            u_min=-2,
            u_max=+2,
            checkerboard_colors=['#E9D700','#F8ED62'], # Update colors of yellow checkerboard
        )
        
        pic2.generate_target()
        pic2.target.move_to(pic.get_center())
        #Adding axes
        axes = ThreeDAxes()
        
        self.add(axes)

        self.play(Write(pic))

        self.play(Write(pic2))

        pic3 = pic.copy().set_fill_by_checkerboard(['#4AE54A','#A4FBA6'])

        label2 = Text("Picture 2").next_to(text3d, DOWN).shift(DOWN).scale(.75)
        label1 = Text("Picture 1").next_to(label2,DOWN).shift(DOWN).scale(.75)
        
        self.add_fixed_in_frame_mobjects(label1)
        self.add_fixed_in_frame_mobjects(label2)
        self.play(Write(label1), Write(label2))

        self.play(FadeOut(label2),FadeOut(label1))
        
        self.play((MoveToTarget(pic2))) 

        label3 = Text("Blended Picture").next_to(text3d,DOWN).shift(DOWN*2).scale(.75)
        self.add_fixed_in_frame_mobjects(label3) 
        self.play(Write(label3))
         
        self.play(FadeOut(pic2),ReplacementTransform(pic,pic3))

        self.wait()


#this might have to be a 3d scene to achieve the desired effect
class Mirror(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=80 * DEGREES, theta=-60 * DEGREES)

        #picture = ImageMobject(Image.open(requests.get("https://i.natgeofe.com/n/8c395689-5233-434c-8a1e-bd34af03b59f/84731.jpg?w=1024&h=767", stream=True).raw)).scale(.75)
        #self.add(picture)
        #
        #picture2 = picture.copy()

        def update_curve(d,dt):                 #<---- This doesn't work actually so bit of an issues
            d.rotate_about_origin(dt,RIGHT)

#        picture2.add_updater(update_curve)
        axes = ThreeDAxes()
#        self.add(picture,picture2)
        self.add(axes)
        self.wait(PI)
        self.add(Rectangle())

        #self.play(             #<---- This is closer to the flipping motion but then it warps it
        #    Rotating(
        #        picture,
        #        radians=PI,
        #        run_time=2,
        #        axis=[1,0,0]
        #    )
        #)
        self.wait(2)


