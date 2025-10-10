#Methods of creating a list


#1 USe a for loop
#2
language = 'Python'
lst = list(language)
print(type(lst))
print(lst)

#3 List Comprehension
lst2 = [i for i in language]
print(type(lst2))
print(lst2)

#Example of lists of numbers
numbers = [(i,i*i) for i in range(6)]
print(numbers)

#Combining list comprehension with if expression
odd_numbers = [i for i in range(12) if i % 2 != 0]
print(odd_numbers)

#Flattening a three dimensiona array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)

#lambda function - a small anonymous function with a name. We need it when we want to write an anonymous function inside another function
#example
x = lambda param1, param2, param3: param1 * param2 + param3
print(x(5,6,7))

#Exercises
#1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered = [i for i in numbers if i<1]
print(filtered)

#2 
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flat1 = [number for row in list_of_lists for number in row]
flat2 = [number for row in flat1 for number in row]
print(flat2)

#3 Tuple creation
tuples = [(i,1,i,i**2,i**3,i**4,i**5) for i in range(11)]
print(tuples)

#4Flattening
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# Desired output: [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
flat_countries = [[item[0].upper(),item[0].upper()[0:3],item[1].upper()] for country in countries for item in country]
print(flat_countries)

#5 Change to Dictionary
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flat_countries = [{'country' : item[0].upper(),'city' : item[1].upper()} 
                  for i in countries
                  for item in i]
print(flat_countries)
# Desired output:
#[{'country': 'FINLAND', 'city': 'HELSINKI'},
#{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
#{'country': 'NORWAY', 'city': 'OSLO'}]

#6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# Desired output: ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
answer = [(item[0] + ' ' + item[1])
          for person in names
          for item in person]
print(answer)

#7 lambda function to solve a slope or y intercept of a linear function
slope = lambda a, b, c : -a/b
y_intercept = lambda a, b, c : -c/b
print(slope(1,2,3))
print(y_intercept(1,2,3))
#ax+by+c =0