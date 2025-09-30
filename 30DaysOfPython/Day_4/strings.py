#Day4 Exercises

#1-2 Concatenate
a = 'Thirty'
b = 'Days'
c = 'Of'
d = 'Python'
space = ' '
answer = a+space+b+space+c+space+d
print(answer)

e = 'Coding'
f = 'For'
g = 'All'
q2 = e+space+f+space+g
print(q2)

#3-11 Variables
company = '\"Coding for All\"'
print(company)
company = company.upper()
print(company)
company = company.lower()
print(company)
company = company.capitalize()
print(company)
company = company.title()
print(company)
company = company.swapcase()
print(company)

company = company.title()
length = len(company)
sliced = company[8:length-1]
print(sliced)

print(company.rfind('Coding'))

company = company.replace('Coding','Python')
print(company)

#Q12-13
string2 = 'Python for Everyone'
string2o = string2
index1 = string2.rindex('Everyone')
string2 = string2[0:index1]
all = 'All'
string2 = string2+all
print(string2)

string3 = 'Coding For All'
print(string3.split())

#14
string14 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(string14.split(', '))

#15-17
print(string3[0])
length = len(string3)
print(length-1)
print(string3[10])

#18-19
string2 = string2o.title()
string2 = string2.split(' ')
string2a = string2[0]
string2b = string2[1]
string2c = string2[2]
abbrev2 = string2a[0]+string2b[0]+string2c[0]
print(abbrev2)

string3 = string3.title()
string3o = string3
string3 = string3.split(' ')
string3a = string3[0]
string3b = string3[1]
string3c = string3[2]
abbrev3 = string3a[0]+string3b[0]+string3c[0]
print(abbrev3)

#20-22
print(string3o.find('C'))
print(string3o.find('F'))
print(string3o.rfind('i'))

#23-27
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))
print(sentence.rindex('because'))
sentence_sliced = sentence.replace('because because because ','')
print(sentence_sliced)

#28-30
print('Q28 '+string3o)
print(string3o.startswith('Coding'))
print(string3o.endswith('coding'))

string30 = '  Coding For All   '
print(string30.strip(' '))

#31
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

#32
list32 = ['Djanjo', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(list32)
list32joined = ' '.join(list32)
print(list32joined)

#33-34
print('I am enjoying this challenge \nI just wonder what is next')
print('Name\tAge\tCountry\tCity\nBob\t250\tFrance\tParis')

#35
r = 10
pi = 3.14
a = pi * r ** 2
print(f'radius = {r}\narea = {pi} * radius ** 2\nThe area of a circle with radius {r} is {a} meters square.'.format())

#36
a=8
b=6
print(f'{a}+{b}={a+b}')
print(f'{a}-{b}={a-b}')
print(f'{a}*{b}={a*b}')
print(f'{a}/{b}={a/b}')
print(f'{a}%{b}={a%b}')
print(f'{a}//{b}={a//b}')
print(f'{a}**{b}={a**b}')

