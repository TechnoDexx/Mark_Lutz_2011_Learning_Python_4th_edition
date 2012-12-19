#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Scene:
	def __init__(self):
		self.customer = Customer()
		self.clerk = Clerk()
		self.parrot = Parrot()

	def action(self):
		self.customer.line()
		self.clerk.line()
		self.parrot.line()

class Actor:
	def line(self):
		pass

class Customer(Actor):
	def line(self):
		print('customer: "thats\'s one ex-bird!"')

class Clerk(Actor):
	def line(self):
		print('clerk: "no it isn\'t..."')

class Parrot(Actor):
	def line(self):
		print('parrot: None')

if __name__ == '__main__':
	scene = Scene()
	scene.action()
