#syntax
#"r" - read
#"a" - append
#"w" - write
#"x" - create
#"t" - text
#"b" - binary

#Open and read txt file
f = open('./30DaysOfPython/day_19/reading_file_example.txt')
txt = f.read()
print(type(txt))
print(txt)
f.close()

#Read first 10 chars
f = open('./30DaysOfPython/day_19/reading_file_example.txt')
txt2 = f.read(10)
print(type(txt2))
print(txt2)
f.close()

#Only read first line
f = open('./30DaysOfPython/day_19/reading_file_example.txt')
txt3 = f.readline()
print(type(txt3))
print(txt3)
f.close()

#Read all the text line by line
f = open('./30DaysOfPython/day_19/reading_file_example.txt')
txt4 = f.readlines()
print(type(txt4))
print(txt4)
f.close()

#Or can use splitlines()
f = open('./30DaysOfPython/day_19/reading_file_example.txt')
txt5 = f.read().splitlines()
print(type(txt5))
print(txt5)
f.close()

#Can also open files using 'with' which closes files by itself
with open('./30DaysOfPython/day_19/reading_file_example.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)

#Updating files
#'a' = append to end of file
#'w' = write - overwrites existing content, creates file if it doesnt exist

with open('./30DaysOfPython/day_19/writing_file_example.txt','a') as f:
    f.write('Doc doesnt exist so new doc with this text to be created')

#Deleting files
import os
if os.path.exists('./30DaysOfPython/day_19/example.txt'):
    os.remove('./30DaysOfPython/day_19/example.txt')
else:
    print('The file does not exist')

#File Types
#.txt covered above
#.json = JavaScript Object Notation aka 'a stringified JavaScript object or Python dictionary
#example

# dictionary
person_dct= {
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}
# JSON: A string form a dictionary
person_json = "{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}"

# we use three quotes and make it multiple line to make it more readable
person_json2 = '''{
    "name":"Beyonce",
    "country":"France",
    "city":"Bordeaux",
    "skills":["Singing", "Dancing","Acting"]
}'''

#Change JSON to Dictionary
import json
person_dct2 = json.loads(person_json2)
print(type(person_dct2))
print(person_dct2)
print(person_dct2['name'])

#Change dictionary to JSON
import json
person3 = {
    "name": "Tom",
    "country": "America",
    "city": "Los Angeles",
    "skills": ["flying","jumping","running"]
}

person_json3 = json.dumps(person3, indent = 2)
print(type(person_json3))
print(person_json3)

#saving as JSON
with open('./30DaysOfPython/day_19/json_example.json','w',encoding='utf-8') as f:
    json.dump(person3, f, ensure_ascii=False, indent=2)

#CSV files
import csv
with open('./30DaysOfPython/day_19/csv_example.csv','w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
    csvwriter.writerow(['Text','Type','Count'])
    csvwriter.writerow(['Chocolate','snack',5])
    csvwriter.writerow(['Cookies','snack',7])
    csvwriter.writerow(['Apple','fruit',2])

with open('./30DaysOfPython/day_19/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is a foodstuff. It is a {row[1]} and I have {row[2]} left.')
            line_count += 1
    print(f'Number of lines: {line_count}')

#XLSX
#revisit after learning pip

#import xlrd
#excel_book = xlrd.open_workbook('sample.xls')
#print(excel_book.nsheets)
#print(excel_book.sheet_names)

#Exercises - Day_19

#1 count the number of lines and words in a text.

import os 
def counter (filename):
    result = {"file": filename,"lines": 0, "words" : 0}
    filename = './data/'+str(filename)
    try:
        f = open(filename)
        lines = f.readlines()
        for line in lines:
            line = line.strip(os.linesep)
            result["lines"] +=1
            result["words"] += len(line.split())
    except Exception as e:
        print(e)
    finally:
        return result

print(counter('obama_speech.txt'))
print(counter('donald_speech.txt'))
print(counter('michelle_obama_speech.txt'))
print(counter('melina_trump_speech.txt'))

#Q2 Create a function that finds the ten most spoken languages from a json input file

def most_spoken_languages(filename,limit):
    # Get the countries_data.json into a dictionary
    import json
    #filename = 'countries_data.json'
    filename = './data/'+str(filename)
    #print(filename)
    with open(filename, 'r') as file:
        country_dct = json.load(file)
    #print(country_dct[0:2])

    #Create a list of all the languages per country
    language_lst = []
    for x in country_dct:
        if x['languages'] in language_lst:
            #print('Yay')
            pass
        else:
            language_lst.append(x['languages'])
        #language_lst[(x['languages'])] = 0
    #print(language_lst)

    #Break open the second tier []
    language_lst2 = []
    for xs in language_lst:
        #print(xs)
        for x in xs:
            language_lst2.append(x)
    #print(language_lst2)

    #Convert into a dictionary and count instances of each language
    language_lst3 = list(set(language_lst2)) # getting rid of dupes
    #print(language_lst3)
    zerocount = [0]*len(language_lst3)
    d1 = zip(language_lst3,zerocount)
    d1 = (dict(d1))
    #now we have a dict of languages each with 0 occurences

    #count occurences for each language
    for x in country_dct:
        for y in x['languages']:
            d1[y] += 1    

    #Sort languages by # of countries spoken
    d2 = {k: v for k, v in sorted(d1.items(), key = lambda item: item[1], reverse = True)}

    #Retun top reslts until specified limit
    first_x_pairs = {d2[k]:k for k in list(d2)[:int(limit)]}

    return first_x_pairs

print(most_spoken_languages('countries_data.json',10))

#Q3 - Read the countries_data.json file and create a function that creates a list of ten most populated countries

def most_populated_countries(filename,limit):
    # Get the countries_data.json into a Python dictionary
    import json
    filename = './data/'+str(filename)
    with open(filename, 'r') as file:
        country_dct = json.load(file)

    #Create a dictionary of all the countries and their pops
    country_lst = []
    pop_lst = []
    for x in country_dct:
        country_lst.append(x['name'])
        pop_lst.append(x['population'])

    d1 = zip(country_lst,pop_lst)
    d1 = (dict(d1))

    #Sort countries by population
    d2 = {k: v for k, v in sorted(d1.items(), key = lambda item: item[1], reverse = True)}

    #Retun top results until specified limit
    first_x_countries = {k:d2[k] for k in list(d2)[:int(limit)]}

    return first_x_countries

print(most_populated_countries('countries_data.json',10))

#Level 2 Exercises
