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