# -*- coding: utf-8 -*-
#from book import Book

class AlreadyRentError:
	def __init__(self,book):
		self.msg="貸りています"
		self.book=book

	def getMessage(self):
		return self.book.getName() + " を " + self.msg

class Student:
	"""A simple student class"""
	def __init__(self,name):
		self.name = name
		self.book = None

	def getName(self):
		return self.name

	def rent(self, book):
		if self.book is None:
			self.book = book
		else:
			raise AlreadyRentError(self.book)

	def getBook(self):
		return self.book
