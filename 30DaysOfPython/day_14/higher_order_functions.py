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

#7 No 'e'

def no_starting_E(x):
    if x[0] == 'E':
        return False
    else:
        return True
    
for x in countries:
    countries_with_no_starting_E = filter(no_starting_E,countries)

print(list(countries_with_no_starting_E))

#8 Combo list iterator

def no_e_at_all(x):
    if 'E' in x:
        return False
    else:
        return True
    
for x in countries:
    countries_w_no_e = filter(no_e_at_all,map(make_name_upper,countries))

print(list(countries_w_no_e))

#9 - Return only strings

lst = [1,2,3.4,'aaaa','b','c',['a','a'],['b',2.3],[1,'a',4.2]]


def get_string_lists(x):
    if type(x) == str:
        return True
    else:
        return False
    
for x in lst:
    result = filter(get_string_lists,lst)

print(list(result))

#10
def sum_all_numbers(x,y):
    result = int(x)+int(y)
    return result

for x in numbers:
    answer = reduce(sum_all_numbers,numbers)

print(answer)

#11

last_country = countries.pop()

def concatenate_all_countries(x,y):
    conc = x +', '+ y
    return conc

for x in countries:
    section = reduce(concatenate_all_countries,countries)

print(section,'and',last_country,'are north European countries')

#12 Categorise countries
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];

def categorise_countries(x):
    if 'a' in x or 'A' in x:
        return False
    else:
        return True

for x in countries:
    ia_countries = filter(categorise_countries,countries)

#print(list(ia_countries))

#13 - Create dictionary of countries per starting letter

# Set-up dictionary
import string
countries_dict = dict()
x= 0
      
while x < len(str(string.ascii_uppercase)):
    countries_dict[string.ascii_uppercase[x]] = 0
    x = x+1

#Iterate through each letter/country combo
countries_dict1 = countries_dict
for y in countries_dict1:
    for z in countries:
        if z[0] == y:
            countries_dict1[y] += 1

print(countries_dict1)

#13b - If letter in country at all
countries_dict2 = countries_dict

def uppercase(para):
    return para.upper()
for x in countries:
    uppercountries = map(uppercase,countries)

upperlist = list(uppercountries)

#upper_countries = list(uppercase_decorator(countries))
for y in countries_dict2:
    #print(y)
    for z in upperlist:
        #print(z)
        if z.count(str(y)) > 0:
            countries_dict2[y] += 1
            print(z)

print(countries_dict2)




