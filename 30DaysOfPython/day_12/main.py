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

#2 - New user ID with length and number of IDs as inputs
def user_id_gen_by_user(length,number):
    new_id = [''] * number
    lets_and_nums = string.ascii_letters + string.digits
    for j in range(0,number,1):
        for i in range(0,length,1):
            new_id[j] += lets_and_nums[randint(0,len(lets_and_nums)-1)]
        print(new_id[j])    
    return new_id

user_id_gen_by_user(8,3)

#3 Write a function to generate an RGB color
def rgb_color_gen():
    col = [0]*3
    for i in range(0,3,1):
        #print(i)
        col[i] = randint(0,255)
    #print(tuple(col))
    print('rgb'+ str(tuple(col)))

rgb_color_gen()

#Exercises - Level 2
#1
def list_of_hexa_colours(count):
    hexadecimals = string.ascii_lowercase[0:6]+string.digits
    array = ['#'] * count
    #print(hexadecimals)
    for j in range(0,count,1):
        #print(j)
        for i in range(0,6,1):
            array[j] += str(hexadecimals[randint(0,16-1)])
    return array

print(list_of_hexa_colours(2))

#2
def list_of_rgb_colors(count):
    for i in range(0,count,1):
        rgb_color_gen()

list_of_rgb_colors(3)

#3
print('Q3')
def generate_colours(colour_type,num):
    if colour_type == 'hexa':
        print(list_of_hexa_colours(num))
    elif colour_type == 'rgb':
        list_of_rgb_colors(num)
    else:
        pass

generate_colours('hexa',5)

#Exercises - Level 3
#1 Shuffle list
print('Q1')
def shuffle_list(lst):
    leng = len(lst)
    print(lst[0])
    print('Length is ',leng)
    new_lst = ['ha']*leng
    remaining_lst = lst
    
    for i in range(0,leng,1):
        while new_lst[i] == 'ha':
            #print(i)
            counter = randint(0,leng-1)
            #print(counter)
            #print(lst[counter])
            if lst[counter] in new_lst:
                pass
            else:
                new_lst[i] = lst[counter]
            #print(new_lst[i])
    #print(new_lst)
    #new_lst = lst
    return new_lst

print(shuffle_list(['a','b','c','d','e']))


#2 Unique array
print('Q2')
def unique_array():
    array = ''
    x = 0
    while len(array) < 7:
        new_num = str(randint(0,9))
        if new_num in array:
            #print('duplicate')
            pass
        else:
            #print('unique')
            array += new_num
    print(array)

unique_array()
