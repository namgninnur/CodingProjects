#Exception Handling concepts

#HL Concept
#try:
    #Run this code
#except: (potentially with condition)
    #Run when there is an exception
#else:
    #Run when no exceptions
#finally:
    #Always run this code

#Examples
try:
    print(10+'5')
except:
    print('Ooops?')

try:
    #name = input('Enter your name? ')
    #year_born = input('What\'s your birth year? ')
    age = 2025- int(year_born)
    print(f'You are {name} and you\'re age is {age}')
except TypeError:
    print('Type error has occured')
except ValueError:
    print('Value error has occured')
except SyntaxError:    
    print('Syntax error has occured')
except NameError:
    print('Name Error has happened')
else:
    print('I usually run with the try block')
finally:
    print('I always run')

#Shorter option
try:
    #name = input('Enter your name? ')
    #year_born = input('What\'s your birth year? ')
    age = 2025- year_born
    print(f'You are {name} and you\'re age is {age}')
except Exception as e:
    print(e)


#Unpacking lists
#uses two operators
# * for tuples and ** for dictionaries
def sum_of_4_nums(a,b,c,d):
    return a+b+c+d

lst = [1,2,3,4]
print(sum_of_4_nums(*lst))

numbers = range(2,7)
print(list(numbers))
args = [2, 7]
numbers2 = range(*args)
print(list(numbers2))

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last) 

#unpacking
def unpacking_team_info(name, country, city, sport):
    return f'{name} is a {sport} team in {country}, {city}.'
dct = {'name':'Spirit', 'country':'England', 'city':'London', 'sport':'Cricket'}
print(unpacking_team_info(**dct))

#Packing
# packing lists
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1,2,3,4,5,6))
print(sum_all(1,2,3,4,5,6,7,8))

# packing dictionaries

def packing_team_info(**kwargs):
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_team_info(name='Crystal Palace', sport='football',city ='South London'))

#Spreading in Python
lst_one = [1,2,3]
lst_two = [5,6,7,8]
lst = [0, *lst_one, 4, lst_two]
print(lst)
lst = [0, *lst_one, 4, *lst_two]
print(lst)

#Enumerate
for index, item in enumerate([20,30,40]):
    print(index,item)

print(enumerate([20,30,40]))

for index, i in enumerate(countries):
    print('hi')
    if i == 'Norway':
        print(f'The country {i} has been found at index {index}')

#Zip to combine lists when looping through them
fruits = ['apple', 'orange','lemon', 'passionfruit','lime']
veggies = ['tomato', 'lettuce', 'potato','carrot','onion']
f_and_v = []
for f, v in zip(fruits,veggies):
    f_and_v.append({'fruit':f, 'veg':v})

print('F&V is',f_and_v)

#Exercises
#Q1
names = ['Finland','Sweden','Norway','Denmark','Iceland','Estonia','Russia','Latvia']
*nordic_countries, es, ru, la = names
print(nordic_countries)
print(es)
print(ru)
print(la)