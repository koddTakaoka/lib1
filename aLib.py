# -*- coding: utf-8 -*-

from student import Student
from student import AlreadyRentError as student_AlreadyRentError 
from book import Book
from book import AlreadyRentError as book_AlreadyRentError 
from book import NotRentError

aBook=Book("SQL")
print aBook.getName()

bBook=Book("XML")
print bBook.getName()

aStudent=Student("小林")
print aStudent.getName()

bStudent=Student("大林")
print bStudent.getName()

try:
	aBook.rent(aStudent)
	print aBook.getStudent().getName()
	print aStudent.getBook().getName()
	aBook.rent(bStudent)
except book_AlreadyRentError as err:
    print err.getMessage()

try:
	bBook.back()
except NotRentError as err:
    print err.getMessage()

try:
	bBook.rent(aStudent)
except student_AlreadyRentError as err:
    print err.getMessage()

