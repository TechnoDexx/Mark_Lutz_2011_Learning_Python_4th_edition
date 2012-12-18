#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Animal:
	def reply(self):
		self.speak()

class Mammal(Animal):
	def speak(self):
		pass

class Cat(Mammal):
	def speak(self):
		print('Meow!')

class Dog(Mammal):
	def speak(self):
		print('Bow Wow!')

class Human(Mammal):
	def speak(self):
		print('Hello!')

class Hacker(Human):
	def speak(self):
		print('Hello World!')

if __name__ == '__main__':
	sam = Cat()
	sam.reply()
	tom = Human()
	tom.reply()
	jhon = Hacker()
	jhon.reply()
