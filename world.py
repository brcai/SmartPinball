import numpy as np
import random
from pinball import SmartPinball

class World:

	def __init__(self):
		self.path = []
		self.pinball = SmartPinball(direction=True)
		self.road = [0 for i in range(50)]              #the one-dimensional road the pinball moves on (total length is 50)
		self.road[4] = 1                                 #the barrier on the left side 
		self.road[-4] = 1                                #the barrier on the right side
		
		return

	def simulate(self):
		start_loc = 40  #the initial location of pinball
		loc = start_loc
		pain = 0         #indicator of feeling pain (feel pain when hits the barrier)
		sight = [0 for i in range(self.pinball.sight)]     #indicator of seeing a barrier infront
		cnt = 0
		res = []

		fp = open('location_record.txt', 'w')

		while cnt < 10000:
			print(loc)
			fp.write(str(loc)+'\n')
			if self.road[loc] == 1:                #hits a barrier
				pain = 1
			else:
				pain = 0
			if self.pinball.direction == 1:        #the current moving direction is right
				for i in range(self.pinball.sight):
					sight[i] = self.road[loc+i]    #the vision of the pinball when moving right
			else:                                  #the current moving direction is left
				for i in range(self.pinball.sight):
					sight[i] = self.road[loc-i]    #the vision of the pinball when moving left

			direction = self.pinball.move(sight, pain)  #deciding the direction of next move, based on vision (sight) and feeling (pain)

			loc = loc + direction

			cnt += 1

		fp.close()

		return


if __name__ == "__main__":
	world = World()
	world.simulate()

	
	

	print('end of test')
