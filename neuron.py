import numpy as np

class Neuron:

	def __init__(self, th, srcs, snks):
		self.th = th          #threshold of firing
		self.srcs = srcs      #the dictionary of source neurons, {source id:edge weight}
		self.snks = snks      #the dictionary of sink neurons,   {sink id:edge weight}
		self.pt = 0	      #current membrane potential of the neuron, if > th, then fire
		self.st = 0           #current firing status, 0 - not fire, 1 - fired
		self.decay = 0.1      #membrane potential decay rate, pt = exp(-decay)*pt in the next time step

		return

	def add_source(self, src):
		for key in src.keys():
			if key not in self.srcs.keys():
				self.srcs[key] = src[key]
		
		return 

	def add_sink(self, snk):
		for key in snk.keys():
			if key not in self.snks.keys():
				self.snks[key] = snk[key]

		return


	def fire(self, all_st):
		curr_pt = np.exp(-self.decay)*self.pt      #pt of the last time step, need to decay first
		#pt plus the firing of all source neurons
		for src in self.srcs.keys():
			curr_pt += all_st[src]*self.srcs[src]  #fire (0-not fire or 1-fire) of the source neuron * weight to the neuron
		if self.th <= curr_pt:
			self.st = 1                            #fired
			self.pt = 0                            #membrane return to default level after firing
		else:
			self.pt = curr_pt

		return self.st
