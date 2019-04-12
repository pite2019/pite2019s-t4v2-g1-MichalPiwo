#
#Flight simulator. 
#Write a code in python that simulates the tilt correction of the plane (angle between plane wings and earth). 
#The program should print out current orientation, and applied tilt correction. 
#The program should run in infinite loop, until user breaks the loop. 
#Assume that plane orientation in every new simulation step is random angle with gaussian distribution (the planes is experiencing "turbulations"). 

#With every simulation step the orentation should be corrected, applied and printed out.
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#When you are done upload this code to your github repository. 
#
#Delete these comments before commit!
#Good luck.


from random import gauss
import time

class FlightSimulator(object):
	def __init__(self):
		self.tilt_angle = 0.0

	#def turbulence(self):
	#	self.tilt_angle = gauss(0.0, 15.0)

	def run_simulation(self):
		while 1:
			#self.turbulence()
			self.__next__()
			print("Huston we have a problem!!!!!")
			if self.tilt_angle > 0.0:
				print("turn", abs(int(self.tilt_angle)), "degres right")
			else:
				print("turn", abs(int(self.tilt_angle)), "degres left")

			time.sleep(2)
	
	def __iter__(self):
		return self

	def __next__(self):
		self.tilt_angle = gauss(0.0, 15.0)
		

if __name__ == "__main__":
	simulator = FlightSimulator()
	simulator.run_simulation()