# Will and Kai


import turtle


'''
    On this assignment, you should work with a partner. You must submit what you have completed at the end of the class period, but you do not need to complete any leftover problems for homework. 
 
    For some of these problems you will need to create a class; for others, you will need to use a library. 
    You do NOT need to put all your solutions in this file, however you should keep all your solutions together, clearly labeled with descriptive file names, in one folder. 
'''
 
 
 
''' 1.
    Create a class, Point, that keeps track of two properties: x and y
    When a point is created, values for x and y should be provided.
 
    The methods for this class are as follows:
    rotate90: rotate the point 90° about the origin
    rotate180: rotate the point 180° about the origin
    rotaten90: rotate -90° about the origin
    translate: given 2 values, translate the point by the given amount.
    flip_horizontally: flip the point on the x-axis
    flip_vertically: flip the point on the y-axis
'''
 
class Point:

    def __init__(self,x,y):

        self.x = x

        self.y = y

        print("Point:",str(x)+","+str(y))

    def rotate90(self):

        self.x = -self.y
        
        self.y = -self.x

        print("Point:",str(x)+","+str(y))

    def rotate180(self):

        self.x = -self.x

        self.y = -self.y

        print("Point:",str(x)+","+str(y))

    def translate(self,transx,transy):

        self.x = self.x + transx

        self.y = self.y + transy

        print("Point:",str(x)+","+str(y))

    def fliphorizontally(self):

        self.x = -self.x

        print("Point:",str(x)+","+str(y))

    def flipvertically(self):

        self.y = -self.y

        print("Point:",str(x)+","+str(y))


 
 
''' 2.
    Create a class, Bicycle, that keeps track of three properties: cadence, gear, speed. 
    When a Bicycle is created, cadence, gear, and speed are accepted as arguments.
 
    The methods for this class are as follows:
    set_gear: given a value, set the gear to that value
    set_cadence: given a value, set the cadence to that value
    apply_brake: given a value, decrease the speed of the bike by that value
    speed_up: given a value, increase the speed of the bike by that value
'''
 
class Bicycle:
   def __init__(self, cadence, gear, speed):
      self.cadence = cadence
      self.gear = gear
      self.speed = speed
   def set_gear(self, value):
      self.gear = value
   def set_cadence(self, value):
      self.cadence = value
   def apply_brake(self, value):
      self.speed -= value
   def speed_up(self, value)
      self.speed += value
 
 
 
''' 3.
    Create a class, student, that keeps track of four properties: energy, hunger, stress, and hours.
    These properties have a range from 0-100, except hours, which has a range from 0-24. 100 energy means they are energetic; 100 hunger means they are very hungry; 100 stress means they are extremely stressed. When you create a new student, assume they have moderate hunger, low stress, a lot of energy, and 24 hours.
 
    The methods for the student class are as follows:
    study: Given a value (to adjust hours), study for that given length of time. Studying decreases energy and increases hunger based on the length of the study.
    sports: Given a value (to adjust hours), play sports for that given length of time. This decreases energy, increases hunger, and decreases stress based on the length of the sports.
    class: Given a value (to adjust hours), attend classes for a given length of time. This decreases energy, increases hunger, and increases stress based on the length of the class.
    take_test: Given a value (to adjust hours), this increases stress. 
    submit_paper: this decreases stress.
    eat_meal: Given a value (to adjust hours), this decreases stress, decreases hunger, and increases energy.
    sleep: Given a time (to adjust hours), this decreases stress, increases energy, and increases hunger.
    new_day: resets the hours in a day.
 
    You may not let a student do more than 24 hours worth of activities in a given day. 
'''
 


class Student:

    def __init__(self,energy,hunger,stress):

        self.energy = energy

        self.hunger = hunger

        self.stress = stress

        self.hours = 0

        if self.hunger > 100:

            self.hunger = 100

        if self.hunger < 0:

            self.hunger = 0

        if self.stress > 100:

            self.stress = 100

        if self.stress < 0:

            self.stress = 0

        if self.energy > 100:

            self.energy = 100

        if self.energy < 0:

            self.energy = 0

    def study(self,x):

        self.hours = self.house + x

        self.energy = self.energy - self.hours

        self.hunger = self.hunger + self.hours

    def sports(self,x):

        self.stress = self.stress - x

        self.hours = self.hours + x

        self.energy = self.energy - x

        self.hunger = self.hunger + x

    def classtime(self,x):

        self.hours = self.hours + x

        self.energy = self.energy - x

        self.hunger = self.hunger + x

        self.stress = self.stress + x

    def test(self,x):

        self.hours = self.hours + x

        self.stress = self.stress + 2x

    def submitpaper(self):

        self.stress = self.stress - 3

    def eatmeal(self,x):

        self.hunger = self.hunger - x

        self.hours = self.hours + x

        self.energy = self.energy + x

        self.stress = self.stress - x

    def sleep(self,x):

        self.hours = self.hours + x

        self.hunger = self.hunger + x

        self.energy = self.energy + x

        self.stress = self.stress - x

    def newday(self):

        self.hours = 0
 
''' 4. 
    Use numpy to create an array of numbers going from 20 to 100 by increments of .25
    Then, multiply all the values in the array by 4. 
    Then. find the sum of all the values.
'''
import numpy
array = numpy.arrange(20,100.25,0.25)
array = array*4
sum = numpy.sum(array)
 
 
 
''' 5.
    Use turtle to draw a star.
'''
 

 
 
''' 6.
    Use SymPy to determine the area of a triangle given points a, b and c.
'''
from sympy import Point, Polygon
a = Point(0,0)
a = Point(0,1)
a = Point(1,0)
triangle = Polygon(a,b,c) 
print(str(triangle.area))

 
''' 7. 
    Use VPython to build a 3D snowman.
'''
 
 
 
 
''' Sources:
    https://docs.oracle.com/javase/tutorial/java/javaOO/classes.html
'''