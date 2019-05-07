from random import gauss
import time
import logging

logging.basicConfig(level=logging.DEBUG)

class Environment(object):
	def __init__(self):
		self.planes_in_env = [] 

	def add_plane(self, plane):
		self.planes_in_env.append(plane)

	def simulate_trbulance(self):
		turbulance_value = gauss(0.75, 1.0)
		for j,i in enumerate(self.planes_in_env):
			if i.is_alive:
				i.tilt_sensor(turbulance_value)
				i.corect_angle()
			else:
				self.planes_in_env.pop(j)
		time.sleep(2)


class Plane(object):
	tilt_correction = 0.75
	def __init__(self, name):
		self.tilt_angle = gauss(0,4)
		self.name = name
		self.is_alive = True
	
	def tilt_sensor(self, turbulance_value):
		self.tilt_angle += turbulance_value

	def corect_angle(self):
		logging.debug('It\'s {} plane'.format(self.name))
		logging.debug('Our tilt angle is {}'.format(self.tilt_angle))
		if self.tilt_angle > 0.0:
			self.tilt_angle -= 0.75
			logging.debug('turning {} degres left'.format(self.tilt_correction))
		else:
			self.tilt_angle += 0.75
			logging.debug('turning {} degres right'.format(self.tilt_correction))
		if abs(self.tilt_angle) > 90:
			logging.debug('This is the end :(')
			self.is_alive = False
			
if __name__ == '__main__':
	f16_plane = Plane("F16")
	boeing = Plane("boeing")
	envir = Environment()
	envir.add_plane(f16_plane)
	envir.add_plane(boeing)
	while True:
		envir.simulate_trbulance()
