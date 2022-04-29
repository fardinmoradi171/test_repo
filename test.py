from time import time

from threading import Thread

class Person():
	def __init__(self,name,family,age):
		self.name = name
		self.family = family
		self.age = age
	def fullname(self):
		print(f"name is {self.name}\n family is:{self.family}\n age is {self.age}") 
