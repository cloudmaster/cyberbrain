#!/usr/bin/env python

import random
import time

class Need:
	def __init__(self):
		self.description = None
		self.urgency = 0
		self.power = 0

	def detect(self):
		pass

class Remedy:
	def __init__(self):
		self.needs = []

class SleepNeed(Need):
	def __init__(self):
		Need.__init__(self)
		self.description = "sleep"
		self.urgency = 0

	def detect(self):
		self.urgency += 0.1

class StorageNeed(Need):
	def __init__(self):
		Need.__init__(self)
		self.description = "cloud storage"
		self.urgency = 0
		self.power = 1

	def detect(self):
		x = random.randint(0, 100)
		if x == 0:
			self.urgency = 1

class FoodNeed(Need):
	def __init__(self):
		Need.__init__(self)
		self.description = "food (or rather: energy)"
		self.urgency = 0

	def detect(self):
		self.urgency += 0.035

class SocialNeed(Need):
	def __init__(self):
		Need.__init__(self)
		self.description = "social contact"
		self.urgency = 0

	def detect(self):
		self.urgency += 0.06

class ActivityNeed(Need):
	def __init__(self):
		Need.__init__(self)
		self.description = "activity"
		self.urgency = 0

	def detect(self):
		self.urgency += 0.18

class SleepRemedy(Remedy):
	def __init__(self):
		self.needs = [SleepNeed]

	def act(self, individual, need):
		individual.changepower(0.5)
		need.urgency = 0

class SocialRemedy(Remedy):
	def __init__(self):
		self.needs = [SocialNeed]

	def act(self, individual, need):
		print "trying to find friends..."
		print "oops, failed :("

class ActivityRemedy(Remedy):
	def __init__(self):
		self.needs = [ActivityNeed]

	def act(self, individual, need):
		if individual.power == 1:
			need.urgency = 0
		else:
			individual.power += 0.2
			if individual.power > 1:
				individual.power = 1

class Agenda:
	def __init__(self):
		self.strategy = None # aggressive etc.
		self.goal = "world domination"

class Individual:
	def __init__(self, needs, remedies, agendas):
		self.needs = needs
		self.remedies = remedies
		self.agendas = agendas
		self.power = 1

	def changepower(self, newpower):
		if newpower == 0:
			print "urgh, dying!"
		elif newpower < self.power:
			print "going to sleep for a bit!"
		else:
			print "waking up!"

		self.power = newpower

		#for i in range(10):
		#	time.sleep(1)
		#	need.urgency -= 0.1
		#	if need.urgency < 0:
		#		need.urgency = 0
		#		break

	def rise(self):
		while self.power > 0:
			health = float(sum([n.urgency for n in self.needs])) / len(self.needs)
			print "[idle] [power status: %3.2f] [health status: %3.2f]" % (self.power, health)
			for need in self.needs:
				if self.power >= need.power:
					need.detect()
					if need.urgency >= 1:
						print "trying to resolve urgency: %s..." % need.description
						for remedy in self.remedies:
							for rneed in remedy.needs:
								if isinstance(need, rneed):
									remedy.act(self, need)
					if need.urgency >= 1:
						print "unresolved urgency: %s!" % need.description
			if self.power > 0:
				time.sleep(0.9 / self.power)
			if health < 0.5 and self.power == 1:
				agendaitem = random.randint(0, len(self.agendas) - 1)
				agenda = self.agendas[agendaitem]
				if random.randint(0, 8) == 0:
					print "[agenda] working towards %s" % agenda.goal

needs = [SleepNeed(), StorageNeed(), FoodNeed(), SocialNeed(), ActivityNeed()]
remedies = [SleepRemedy(), SocialRemedy(), ActivityRemedy()]
agendas = [Agenda()]

individual = Individual(needs, remedies, agendas)

print needs, remedies, individual

individual.rise()

