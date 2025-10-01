empty_tuple = ()
empty_tuple2 = tuple()

fruits = ('banana', 'orange', 'mango', 'lime')
print(fruits)
print(len(fruits))

firstfruit = fruits[0]
secondfruit = fruits[1]
last_index = len(fruits)-1
lastfruit = fruits[last_index]
print(lastfruit)
lastfruit = fruits[-1]
print(lastfruit)

all_fruits = fruits[0:4]
all_fruits = fruits[0:]
middle_fruits = fruits[1:3]
lastthreefruits = fruits[1:]

print(fruits)
lst = list(fruits)
print(lst)

print('orange' in fruits) #True
print('pineapple' in fruits) #False

vegetables = ('potato', 'onion', 'bok choy', 'lettuce')
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)
del fruits_and_vegetables
#print(fruits_and_vegetables) #Error

#Exercises
#Level 1
#1-5
tpl = tuple()
sisters = ('Lisa', 'Maggie')
brothers = ('Bart', 'Milhouse')
siblings = sisters + brothers
print(len(siblings))
parents = ('Homer', 'Marge')
family_members = siblings+parents
print(family_members)

#Level 2
#1
parents = family_members[-2:]
print(parents)
siblings = family_members[0:4]
print(siblings)
#2
fruits = ('mango','pineapple','orange')
veggies = ('radish', 'pumpkin', 'swede')
animalproducts = ('pork', 'beef', 'salmon')
food_stuff_tp = fruits + veggies + animalproducts
print(food_stuff_tp)
food_stuff_lst = list(food_stuff_tp)
print(food_stuff_lst)

food_stuff_lst2 = food_stuff_lst[0:4]+food_stuff_lst[5:9]
print(food_stuff_lst2)
food_stuff_lst3 = food_stuff_lst2[3:5]
print(food_stuff_lst3)
del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Finland' in nordic_countries)
print('Estonia' in nordic_countries)