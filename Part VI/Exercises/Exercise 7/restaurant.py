﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Lunch:
	def __init__(self):
		self.customer = Customer()
		self.employee = Employee()
	
	def order(self, foodName):
		self.customer.placeOrder(foodName, self.employee)
	
	def result(self):
		self.customer.printFood()


class Customer:
	"""
	Класс клиента
	"""
	
	def __init__(self):
		pass
	
	def placeOrder(self, foodName, employee):
		self.food = employee.takeOrder(foodName)
	
	def printFood(self):
		print(self.food.foodName)


class Employee:
	def takeOrder(self, foodName):
		return Food(foodName)


class Food:
	def __init__(self, n):
		self.foodName = n


if __name__ == '__main__':
	lunch = Lunch()
	lunch.order('Borsch')
	lunch.result()
