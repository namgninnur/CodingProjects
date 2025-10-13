#Functions in Python can handle using other functions as parameters
def sum_numbers(nums):
    return sum(nums)

def higher_order_function(f,lst):
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers,[1,2,3,4,5])
print(result)

def square(x):          # a square function
    return x ** 2

def cube(x):            # a cube function
    return x ** 3

def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute
    
result = higher_order_function('square')
print(result(-3))
result = higher_order_function('cube')
print(result(-3))
result = higher_order_function('absolute')
print(result(-3))

#Closures
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20

#Decorators

# Normal function
def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g())          # WELCOME TO PYTHON

## Let us implement the example above with a decorator

'''This decorator function is a higher order function
that takes a function as a parameter'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON

#Lambda functions - Map

numbers = [1, 2, 3, 4, 5] # iterable
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
# Lets apply it with a lambda function
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]

#Lambda functions - filter

# Lets filter only even nubers
numbers = [1, 2, 3, 4, 5]  # iterable

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))       # [2, 4]

#Lambda - Reduce

from functools import reduce

numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)    # 15

#EXERCISES
#Data
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Level 1
#Q1 - Explain the difference between map, filter and reduce. 
# Reduce consumes an interable and function and returns a single number.
# Filter consumes an interabel and a function and returns an iterable
# Map conumes an interable and a function

#Q2 - Explain the difference between HOF, closure and decorator
# HOF is a function that contains another function
# Closures are functions which return an outcome from the inner function in the outr function
# Decorators are functions that add new functionality to an existing object without modifying its structure

#Q3a - Map

numbs = [10,12,14,16,18]

def sqrooted(x):
    return x ** 0.5

numbs_sqrooted = map(sqrooted,numbs)
print(list(numbs_sqrooted))
 
#Q3b - Filter
q3data = ['This is the answer to Q3','ALPHA','ssshhh','abcdefghijklmopqrstuvwxyz']

def q3function(para):
    if len(para) > 7:
        return True
    return False

long_names = filter(q3function,q3data)
print(list(long_names))

#Q3c - Reduce
reducables = [1,2,3,4]


def add_them(x,y):
    return int(x)*int(y)

total_num = reduce(add_them, reducables)
print(total_num)

#Q4-6
print(countries)
for x in countries:
    print(x)

for x in names:
    print(x)

for x in numbers:
    print(x)

#Exercises - Level 2
#Q1
def uppercase(para):
    return para.upper()

print(uppercase('hi'))
for x in countries:
    uppercountries = map(uppercase,countries)

print(list(uppercountries))

#Q2 - Squares
#Op A
def sq_the_nums(para):
    return para ** 2

for y in numbers:
    sq_nums = map(sq_the_nums, numbers)

print(list(sq_nums))
#Op B
sq_nums2 = map(lambda x : x ** 2, numbers)
print(list(sq_nums2))

#3 
def make_name_upper(name):
    return name.upper()

for x in names:
    upper_names =map(make_name_upper, names)
print(list(upper_names))

#4 - Filter
def no_land(x):
    if 'land' in x:
        return False
    else:
        return True
    
for x in countries:
    landless = filter(no_land,countries)

print(list(landless))

#5 - Filter 6 chars
def no_six_chars(x):
    if len(x) == 6:
        return False
    else:
        return True

for x in countries:
    sixless = filter(no_six_chars,countries)

print(list(sixless))

#6
def no_six_chars_or_more(x):
    if len(x) >= 6:
        return False
    else:
        return True

for x in countries:
    undersix = filter(no_six_chars_or_more,countries)

print(list(undersix))