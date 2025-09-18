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
