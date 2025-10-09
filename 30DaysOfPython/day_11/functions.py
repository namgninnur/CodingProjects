def multiply_two_numbers ():
    num_one = 3
    num_two = 4
    total = num_one*num_two
    return total

print(multiply_two_numbers())

def greetings (name):
    message = 'Hello '+name
    return message

print(greetings('Sarah'))

def generate_full_name (first_name, last_name):
    space = ' '
    full_name = first_name+space+last_name
    return full_name

print('The best Swiss tennis player is ',generate_full_name('Martina','Hingis'))

def add_two_numbers(num1,num2):
    total = num1+num2
    print(total)

print(add_two_numbers(num2= 5, num1 = 7))

def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print(sum_all_nums(2,3,4,5))


#Exercises - Level 1
#1
def add_two_numbers(num1,num2):
    total=num1+num2
    return total

print(add_two_numbers(4,5))
#2 Area of a circle
def area_of_circle(r, pi = 3.14):
    area_of_circle = pi * r * r
    return area_of_circle

print(area_of_circle(r = 10))

#3 Add all nums
def add_all_nums(*nums):
    total = 0
    for i in nums:
        print(i)
        print(type(i))
        if type(i) == str:
            print('This is not a number')
        elif type(i) == int:
            print('This is a number')
            total = total + i
            print(total)
    return total

print(add_all_nums(1,2,'Bye',3,4,'Hello'))

#4 Temperature Conversion
def convert_celsius_to_fahrenheit(C):
    F = (C*9/5)+32
    return F

print(convert_celsius_to_fahrenheit(20))

#5 Check season
def check_season(month,hemisphere = 'Northern'):
    if hemisphere == 'Northern':
        if month in ['Dec','Jan','Feb']:
            season = 'Winter'
        elif month in ['Mar','Apr','May']:
            season = 'Spring'
        elif month in ['Jun','Jul','Aug']:
            season = 'Summer'
        elif month in ['Sep','Oct','Nov']:
            season = 'Autumn'
        else:
            season = 'Invalid data entry'
    elif hemisphere == 'Southern':
        if month in ['Dec','Jan','Feb']:
            season = 'Summer'
        elif month in ['Mar','Apr','May']:
            season = 'Autumn'
        elif month in ['Jun','Jul','Aug']:
            season = 'Winter'
        elif month in ['Sep','Oct','Nov']:
            season = 'Spring'
        else:
            season = 'Invalid data entry'
    else:
        season = 'Oops'
    
    return season

print(check_season('Jul','Northern'))

#6 Slope
def calculate_slope (a,b,c): # form of ax + by = c
    slope = -a/b
    return slope

print(calculate_slope(2,3,4))

#7 Quadratic Equation
def solve_quadratic_eqn(a,b,c): #Form of ax^2 + bx + c = 0
    x1 = (-b + (b**2-4*a*c)**0.5)/(2*a)
    x2 = (-b - (b**2-4*a*c)**0.5)/(2*a)
    return (x1,x2)

print(solve_quadratic_eqn(1,6,-12))

#8 Named print list
def print_list(lst):
    for i in lst:
        print(i)

print_list(['Hi','bob',3,5.6,'ghj'])

#9 Reverse List
def reverse_list(lst):
    count = 0
    rev_lst = ['']*len(lst)
    for i in lst:
        rev_lst[count] = lst[len(lst)-count-1]
        count = count+1
    return rev_lst 

print(reverse_list(['A','B','C','D']))

#10 Capitalise all items
def capitalise_all_items(*lst):
    for i in lst:
        I = i.capitalize()
        print(I)

print(capitalise_all_items('aaaa','bbbbbbb','cccc'))

#11 Add item
def add_item(lst,item):
    lst.append(item)
    print(lst)

add_item(lst = ['Chocolate','Cookies','Cake','Carrots'],item = ['Capsicum','Coffee'])

#12 remove item
def remove_item(lst,item):
    lst.remove(item)
    print(lst)

remove_item(lst = ['Chocolate','Cookies','Coffee','Cake','Carrots'],item = 'Cake')

#13 sum of numbers
def sum_of_numbers(num):
    total=0
    for i in range(num+1):
        total += i
    
    return total

print(sum_of_numbers(3))
#14 sum of odds
def sum_of_odds(num):
    total=0
    for i in range(num+1):
        if i % 2 == 0:
            pass
        else:
            total += i
    
    return total

print(sum_of_odds(3))

#15 sum of evens
def sum_of_evens(num):
    total=0
    for i in range(num+1):
        if i % 2 == 0:
            total += i
        else:
            pass
    
    return total

print(sum_of_evens(4))

#Exercises - Level 2
#1a
def evens_and_odds(para):
    num_evens = 0
    num_odds = 0
    for i in range(0,para+1,1): #+1 to account for Zero
        #print(i)
        if i % 2 == 0:
            num_evens +=1
            #print('a')
        elif i % 2 == 1:
            num_odds +=1
            #print('b')
    return num_evens, num_odds

print(evens_and_odds(100))

#1b
def factorial(para):
    sum = 1
    for i in range(1,para+1,1):
        sum = sum*i
    return sum

print(factorial(4))

#2
def is_empty(para = None):
    if para is None:
        print('The parameter is empty')
    else:
        print('The parameter is not empty')

is_empty(['sdfsdfs','asfasf'])

#3 Multiple functions which intake lists
def calculate_mean(*paras):
    total = 0
    for i in paras:
        #print(i)
        total += i
        #print(total)
    #print(len(paras))
    mean = total/len(paras)
    #print(mean)
    print ('The mean is ', mean)
    return mean

def calculate_median(*paras):
    paras_list = []
    for i in paras:
        paras_list.append(i)
    paras_list.sort()
    if len(paras_list) % 2 == 1:
        index = int(len(paras_list)/2-0.5)
        median = paras_list[index]
    elif len(paras_list) % 2 == 0:
        index1 = int(len(paras_list)/2)
        index2 = int(len(paras_list)/2-1)
        median = (paras_list[index1]+paras_list[index2])/2
    print ('The median is ', median)
    return median

def calculate_mode(*paras):
    arr = set(paras)
    #print(arr)
    mode = max(arr, key=paras.count)
    print('The mode is ',mode)
    return mode

def calculate_range(*paras):
    max_range = max(paras)
    min_range = min(paras)
    paras_range = max_range - min_range
    print('The range is ',paras_range)
    return range

def calculate_variance(*paras):
    #print(paras)
    mean = calculate_mean(*paras)
    #print(mean)
    length = len(paras)
    #print(length)
    i = 0
    stds = [''] * length
    stds_sq = stds
    sum_sqs = 0
    #print(stds)
    while i < len(paras):
        print(i)
        #print(paras[i])
        #print(mean)
        stds[i] = paras[i]-mean
        #print(stds[i])
        stds_sq[i] = stds[i]**2
        print(stds_sq[i])
        sum_sqs += stds_sq[i]
        i += 1
    variance = sum_sqs/(length-1)
    #print(stds)
    print('The variance is ', variance)
    return variance

def calculate_std(*paras):
    std = calculate_variance(*paras)**0.5
    print(std)
    print('The standard deviation is ', std)
    return std

calculate_mean(4,7,2,2,2)
calculate_median(4,7,2,2,2)
calculate_mode(4,7,4,4,4,2,2,2)
calculate_range(4,7,2,2,2)
calculate_variance(46,69,32,60,52,41)
calculate_std(2,4,6,8)

#Exercises Level 3
#1 Is prime?
def is_prime(para):
    for i in range(2,para,1):
        prime = True
        #print(i)
        if para % i == 0:
            prime = False
            break
        else:
            pass
    if prime == True:
        print(para,'is PRIME')
    else:
        print(para,'is sadly not prime. Please try again')

print(is_prime(29))

#2 Is unique
def is_unique(*paras):
    list_length = len(paras)
    #print(list_length)
    set_length = len(set(paras))
    #print(set_length)
    if list_length == set_length:
        is_unique = True
    else:
        is_unique = False
    return is_unique

print(is_unique(1,2,3,5))

#3 Same data type
def same_data_type(*paras):
    #typ = int()
    length = len(paras)
    same_type = True
    for i in paras:
        if i == paras[0]:
            typ = type(paras[0])
        elif type(i) == typ:
            pass
        else:
            same_type = False
            print('Not all same type')
            break
    if same_type == True:
        print('All the same type')

same_data_type(1,2,3)

#4 Valid python variable
def is_valid_python_var(para):
    pass
#Incomplete - unsure how to pass an invalid variable into the function to test it without generating a failure

#5
#Not completed