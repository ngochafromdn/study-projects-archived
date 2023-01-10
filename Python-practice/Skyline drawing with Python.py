"""
This program draws a city skyline.
Authors: Nguyen Hoang Ngoc Ha, Le Thi Hong Ha
Time spent on homework: 1 day
"""
import turtle
t = turtle.Turtle()


def help1(length1,angle1,length2,angle2):
    #helper function 1 to draw the building ( mostly the left part of a building)
    t.forward(length1)
    t.left(angle1)
    t.forward(length2)
    t.right(angle2)

def help2(angle1,length1, angle2, length2):
    #helper function 2 to draw the building ( mostly the left part of a building)
    t.right(angle1)
    t.forward(length1)
    t.left(angle2)
    t.forward(length2)
def first_building():
    #function to draw the first building
    t.begin_fill()
    t.color("blue")
    help1(20,90,80,90)
    help1(13,90,20,90)
    help1(13,90,40,90)
    help1(13,90,20,90)
    t.forward(20)
    help2(90,20,90,13)
    help2(90,20,90,13)
    help2(90,40,90,13)
    help2(90,80,90,20)
    t.end_fill()

def second_building():
    #function to draw the second building
    t.begin_fill()
    t.color("blue violet")
    help1(20,90,180,90)
    help1(10,90,100,90)
    t.forward(40)
    help2(90,100,90,10)
    help2(90,180,90,20)
    t.end_fill()
def third_building():
  #function to draw the third building
    t.color("Chocolate")
    t.begin_fill()
    help1(5,90,270,90)
    t.left(45)
    t.forward(50)
    t.right(100)
    t.forward(50)
    t.right(35)
    help1(265,90,20,0)
    t.end_fill()

def fourth_building():
  #function to draw the fourth building
    t.color("orchid")
    t.begin_fill()
    t.forward(50)
    help1(90,-90,20,-95)
    help1(90,-190,89,-95)
    help1(20,-90,10,-90)
    help1(10,-90,10,-90)
    help1(4,-90,12,-90)
    help1(4,-90,107,-90)
    t.end_fill()

def fifth_building():
    #function to draw the fifth building
    t.begin_fill()
    t.color("palevioletred")
    help1(5,90,90,90)
    help1(13,90,30,90)
    help1(38,90,90,90)
    t.circle(30)
    t.forward(90)
    help2(90,90,90,38)
    help2(90,30,90,13)
    help2(90,90,90,5)
    t.end_fill()

def circle(r, color):
  #function to draw circle filled with wanted color
    t.color(color,color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()


def cloud(): 
    #function to draw the white cloud 
    t.penup()
    t.goto(40,210)
    t.pendown()
    circle(22,"white")
    t.forward(20)
    circle(28,"white")
    t.forward(20)
    circle(30,"white")
    t.right(30)
    circle(32,"white")
    t.forward(30)
    circle(36,"white")
    t.right(10)
def help_sun():
  #help function to draw sun
    x=0
    while (x<360):
        t.penup()
        t.goto(-300,250)
        t.pendown()
        x=x+10
        t.right(x)
        t.forward(70) 
        t.penup()
    
def sun():
   #function to draw the sun   
    t.penup()
    t.color("firebrick")
    t.pendown()
    help_sun()
    t.goto(-280,280)  
    circle(40,"firebrick")   
    t.penup() 
def mountain():
    t.penup()
    t.color("mediumaquamarine")
    t.goto(-280,-200)
    t.pendown()
    t.begin_fill()
    help2(-45,70,90,-70)
    help2(90,70,90,-70)
    help2(90,70,90,-70)
    help2(90,70,90,-70)
    help2(90,70,90,-70)
    help2(90,70,90,-70)
    t.goto(-280,-200)
    t.goto(-350,-250)
    t.color("forestgreen")
    help2(90,80,90,-80)
    help2(90,80,90,-80)
    help2(90,80,90,-80)
    help2(90,80,90,-80)
    help2(90,80,90,-80)
    help2(90,80,90,-80)
    t.goto(-350,-250)
    t.end_fill()
    t.penup()

  
    
def draw_skyline():
    #function to draw the skyline with 5 building, sun, cloud, mountain
    myscreen = turtle.Screen()  
    myscreen.bgcolor("plum")
    t.speed(20)
    mountain()
    t.penup()
    t.color("Orangered")
    t.goto(300,-110)
    t.pendown()
    t.goto(-300,-110)
    t.right(135)
    first_building()
    second_building()
    third_building()
    t.left(90)
    fourth_building() 
    fifth_building()
    cloud()
    sun()
 

