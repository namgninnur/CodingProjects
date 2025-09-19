age = 100
height = 180.1
complex = 2 + 3j

#Q4 - Area of Triangle
base = float(input('Enter base: '))
height = float(input ('Enter height: '))
area = base * height / 2
print('The area of the triangle is ',area)

#Q5 - Perimeter of triangle
side_a = float(input('Enter the length of side A :'))
side_b = float(input('Enter the length of side B :'))
side_c = float(input('Enter the length of side C :'))
perimeter = side_a+side_b+side_c
print('The perimeter of the triangle is ',perimeter,' units')

#Q6 - Area and Perimeter of Rectangle
length = float(input('Enter the length of rectangle:'))
width = float(input('Enter the width of rectangle :'))
area = length * width
perimeter = 2 * length + 2 * width
print('The area of the rectangle is ',area,' units')
print('The perimeter of the rectangle is ',perimeter,' units')

#Q7 - Circle
radius = float(input('Enter radius of circle:'))
pi = float(3.14)
area = pi * radius ** 2
perimeter = 2 * pi * radius
print('The area of the circle is ',area,' units')
print('The perimeter of the circle is ',perimeter,' units')

#8-10 - Slopes
x1 = 1
y1 = 2 * x1 - 2
x2 = 5
y2 = 2 * x2 - 2
m8 = (y2-y1)/(x2-x1)
x = 0
y_intercept = 2 * x - 2
y = 0
x_intercept = (y+2)/2
print('Q8 - Slope = ',m8,', Y Intercept = ',y_intercept,', X intercept = ',x_intercept)
x1 = 2 #Start of Q9
x2 = 6
y1 = 2
y2 = 10
m9 = (y2-y1)/(x2-x1)
dist = ((x2-x1)**2 + (y2-y1)**2)**0.5
print('Q9 - Slope = ',m9,', Euclidian distance = ',dist)
print('Is Slope m8 = Slope m9: ', m8 == m9) #Q10

#11 Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
if y == 0:
    x = float(input('Input value of x to solve for y: '))
    y = x**2 + 6*x + 9
    print('The value of y is: ',y)
print('When x = -3, y=0')

#12
str1 = 'python'
str2 = 'dragon'
len1 = len(str1)
len2 = len(str2)
print(len2 > len1)

#13
print('on' in str1 and 'on' in str2)

#14
sentence = 'I hope this course is not full of jargon.'
print('jargon' in sentence)

#15
print('on' not in str1 and 'on' not in str2)

#16
len1 = len('python')
len1f = float(len1)
len1s = str(len1f)
print(len1s)

#17 - Check to see if number is even.
x = int(input('Insert number to check even/odd status: '))
if x % 2 == 0:
    print(x,' is even')
elif x % 2 == 1:
    print(x,' is odd')
else:
    print(x,' is an invalid number')

#18
fd = 7/3
val = float(2.7)
print(fd == val)

#19/20
print(type('10') == type(10))
print(float('9.8') == 10)

#21
hours = float(input('Enter hours: '))
rate = float(input('Enter rate per hour: '))
weekly = hours*rate
print('Your weekly earning is ',weekly)

#22
years = int(input('Enter number of years: '))
seconds = years * 365 * 24 * 60 ** 2
print('You hae lived for ',seconds,' seconds.')

#23
x=1
while x<6:
    print(x,1,x,x**2,x**3)
    x+=1
