import numpy as np
from neuron import Neuron

class NeuronSys:

	def __init__(self):
		self.all_n = [0,1,2]
		self.all_st = [0,0,0]                               #the firing status of all neurons
		self.eye = Neuron(0.1, srcs={}, snks={2:1})         #the visual neuron
		self.skin = Neuron(0.1, srcs={}, snks={2:100})        #the sensor neuron
		self.rudder = Neuron(10, srcs={0:1, 1:100}, snks={})             #the action neuron
		self.all_neurons = [self.eye, self.skin, self.rudder]

		return

	def stdp(self):
		if self.eye.st == 1 and self.rudder.st == 1:  #when "eye" sees the barrier and "rudder" changes the direction, 
			self.rudder.srcs[0] += 1              #it means there is a casual relationship and the connection between "eye" and "rudder" enhances

		return

	def see(self, strength):
		if sum(strength) > 0:                    #when sees the barrier, the pt of "eye" neuron increases
			self.eye.pt += sum(strength)
		else:
			self.eye.pt = 0

		return

	def pain(self, strength):
		if strength > 0:                         #when feel the hit, the pt of "skin" neuron increases
			self.skin.pt += strength 
		else:
			self.skin.pt = 0

		return

	def run(self):
		for id, nn in enumerate(self.all_neurons):  #for every round, check the status of all neurons, and update their connections weights by STDP
			tmp = nn.fire(self.all_st)
			self.all_st [id] = tmp
		self.stdp()
		for id, nn in enumerate(self.all_neurons):
			nn.st = 0

		return


class SmartPinball:

	def __init__(self, direction):
		self.brain = NeuronSys()
		self.speed = 1
		self.direction = 1                       #moving direction of pinball, 1 - right, -1 - left
		self.sight = 4				 #how far can "eye" sees infront, i.e., "sight" meters ahead of the pinball

		return

	def move(self, color, pain):
		self.brain.see(color)
		self.brain.pain(pain)
		self.brain.run()
		change = self.brain.all_st[-1]
		if change == 1:
			self.direction *= -1

		return self.direction
