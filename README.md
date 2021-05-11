# Manim Animations

```
Goal: desigin clean animations that will help illustrate CS topics in the context of picture manipulations
Using Manim: mathematical animation engine

```
## Installation

```

Install Dependencies: 
1) FFmpeg
2) LaTex (or minimal version)
3) Manim (this repo uses community edition)

```


## Usage

```
>>> manim -p scene.py [className]

className should be whatever animation you would like to see

```
## Structure

```
Once you run the command listed above, movies will be generated in the Media folder

creating modular classes helps with production time

```

## Key methods

* Put all animations in the construct(self): function
* Group and VGroup object are useful in grouping submbjects together: you can then transform and change atrributes of the Group that will apply to all submojects 
* the .next_to(objectName, direction) is helpful for aligning unrelated objects* the .next_to(objectName, direction) is helpful for aligning unrelated objects* the .next_to(objectName, direction) is helpful for aligning unrelated objects* the .next_to(objectName, direction) is helpful for aligning unrelated objects* the .next_to(objectName, direction) is helpful for aligning unrelated objects* the .next_to(objectName, direction) is helpful for aligning unrelated objects* the .next_to(objectName, direction) is helpful for aligning unrelated objects* the .next_to(objectName, direction) is helpful for aligning unrelated objects* the .next_to(objectName, direction) is helpful for aligning unrelated objects


## To Do:

* Add class on getPixels method that generates a list of all pixels in a picture
* Show how manipulations like grayscale or negative manipulate color channels
* Illustrate manipulations at a specific location => nested for loops
* Show a mirror using rotate TAU function


