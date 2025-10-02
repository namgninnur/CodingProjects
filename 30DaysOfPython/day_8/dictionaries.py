# syntax
empty_dict = {}
# Dictionary with data values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct['key1'])

person = {
    'first_name':'Tom',
    'last_name':'Hanks',
    'age':50,
    'country':'USA',
    'is_married':True,
    'skills':['Acting', 'Dancing', 'Flying', 'Ping Pong'],
    'address':{
        'street':'Space street',
        'zipcode':'01234'
    }
    }

#Use get to avoid errors if searching for a key that does not exist
print(person.get('first_name')) # Tom
print(person.get('country'))    # USA
print(person.get('skills')) #['Acting, 'Dancing', 'Flying', 'Ping Pong']
print(person.get('city'))   # None

person['glasses'] = False
person['skills'].append('Running')
print(person)

person['glasses'] = True
print(person)

#removing items
person.pop('age')
person.popitem() #removes last item
del person['is_married']

print(person.items)
print(person.clear())
print(person)
del person
del dct

dct = {'Liverpool':'Football','Crystal Palace':'Football','Surrey':'Cricket','Barbarians':'Rugby'}
dct_copy = dct.copy()
print(dct.keys())
print(dct.values())

#Exercises
#1-2
dog = dict()
dog['Name'] = 'Coco'
dog['Colour'] = 'brown'
dog['Legs'] = '4'
dog['Age'] = '2'
print(dog)

#3-4
student = {'first_name':'Harry','last_name':'Potter','Gender':'Male', 'Age': '18', 'Marital Status':'Single','Skills':['Magic','Flying']}
print(len(student))
print(student['Skills'])
print(type(student['Skills']))
student['Skills'].append('Being Moody')
student['Glasses'] = True
keys = student.keys()
values = student.values()
student_tuples = student.items()
del student['Marital Status']
del student