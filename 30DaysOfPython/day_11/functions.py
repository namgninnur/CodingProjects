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