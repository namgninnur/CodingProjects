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