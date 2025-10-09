#main.py file
#importing a module
import mymodule
print(mymodule.generate_full_name('Steve','Jobs'))

#Import multiple functions at same time
from mymodule import generate_full_name, sum_two_nums, gravity

print(generate_full_name('Alicia','Keys'))
print(sum_two_nums(1,9))
mass = 50
weight = mass * gravity
print(weight)

#Rename imported functions
from mymodule import generate_full_name as fullname, sum_two_nums as sumtwonums, gravity

#Import built in modules

#Import Operating System module
import os

# import the module
import os
# Creating a directory
#os.mkdir('directory_name')
# Changing the current directory
#os.chdir('path')
# Getting current working directory
#os.getcwd()
# Removing directory
#os.rmdir()

#Import System module
import sys

#Some useful sys commands
# to exit sys
#sys.exit()
# To know the largest integer variable it takes
#sys.maxsize
# To know environment path
print(sys.path)
# To know the version of python you are using
#sys.version

from statistics import *

#Can import so we use like this
import math
print(math.pi)

#or like this
from math import pi
print(pi)

#String module
import string
#For help one can use
#print(dir(string))
#help(string)

print(string.digits)
print(string.ascii_letters)

#Random module
from random import random,randint
#print(random())
#print(randint(5,20))

#Exercises Day12
#1 Random user id
def new_user_id(para):
    new_id = ''
    lets_and_nums = string.ascii_letters + string.digits
    length = len(lets_and_nums)
    for i in range(0,para,1):
        new_id += lets_and_nums[randint(0,length-1)]
    #print(new_id)
    return new_id
print(new_user_id(6))

#2 - To complete
