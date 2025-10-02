a = 2
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')

if a > 0:
    if a % 2 == 0:
        print('A is a positive even number')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

if a > 0 and a % 2 == 0:
    print('a is a positive even number')

user = 'Bob'
access_level = 5
if user == 'admin' or access_level >= 8:
    print('Access Granted')
else:
    print('Denied')

#Exercises
#Level 1
# #Q1
age = int(input('Enter your age: '))
if age >= 18:
    print('You are old enough to drive')
else:
    print('You need ',18-age,' more years to learn to drive')

#q2
my_age = 35
your_age = int(input('What is your age? '))

if my_age == your_age:
    print('We are the same age')
elif my_age > your_age:
    if my_age - your_age > 2:
        print('I am ',my_age-your_age,' years older than you')
    else:
        print('I am ',my_age-your_age,' year older than you')
else:
    print('You are older than me! Ha')

#q3
num_one = int(input('Num one please?'))
num_two = int(input('num two please?'))

if num_one > num_two:
    print(num_one,' is greater than ',num_two)
elif num_one < num_two:
    print(num_one,' is less than ',num_two)
else:
    print(num_one,' is equal to ',num_two)

#Level 2
#Q1
score = int(input('Enter ''%'' score: '))
if score >= 85 and score <= 100:
    print('High Distinction')
elif score >= 75:
    print('Distinction')
elif score >= 65:
    print('Credit')
elif score >= 50:
    print('Pass')
else:
    print('Fail')

#Q2
winter = {'June','July','August'}
spring = {'September','October','November'}
summer = {'December','January','February'}
autumn = {'March', 'April', 'May'}

month = input('Enter the current month: ')

if month in winter:
    print('Its cold in winter')
elif month in spring:
    print('The flowers bloom in spring')
elif month in summer:
    print('We go to the beach in summer')
else:
    print('It gets windy in autumn')

#q3
fruits = ['banana', 'orange', 'mango', 'lemon']

new_fruit = input('Enter your favourite fruit: ')
if new_fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(new_fruit)
    print(fruits)

#Level 3
person = {
    'first_name': 'Trevor',
    'last_name': 'Noah',
    'age': 45,
    'country': 'South Africa',
    'is_marred': True,
    'skills': ['Comedy','TV','DJing','Python'],
    'address': {
        'street': 'Funny street',
        'zipcode': '99999'
    }
    }
if person['skills'] is not 'None':
    len_person = len(person['skills'])
    print(len_person)
    if len_person % 2 == 0:
        print('Even')
        print[skills]21
        skills = list(person.values()'skills'))
        middle_key = person[len_person/2:len_person/2+1]
        print
    elif len_person % 2 == 1:
        middle_key = len_person/2 + 0.5
        print(person['skills'])
    else:
        print('Oops')
    print(middle_key)

