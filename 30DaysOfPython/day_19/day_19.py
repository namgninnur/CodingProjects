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
#Extract all incoming email address as a list from the email_Exchange_big.txt file

import re
f = open('./data/email_exchanges_big.txt')
txt = f.read() # read first 1000 chars
txt2 = re.sub(' ','', txt,re.I)
txt3 = re.sub(' ','',txt2,re.I)
#print(txt3)

regex_pattern = r'[ *]?From:[ *].*' #looking for all the From: 's
matches = re.findall(regex_pattern, txt3, re.I)
print(matches)
print(type(matches))

new_matches = []
for i in matches:
    new_i = re.sub(' ?From: ','',i,re.I)
    if new_i in new_matches:
        pass
    else:
        new_matches.append(new_i)

print(new_matches)
print(len(new_matches))
print(type(new_matches))

f.close()

#Exercise 5 and 6

#Plan
#Import file, remove punctuation, split on spaces,
def most_common_words(text,x):
    import re
    filename=str(text)
    f = open(filename)
    txt = f.read() # read first 1000 chars

    txt2 = re.sub('[^A-Za-z ]','',txt)
    txt3 = txt2.split(' ')
    #print(txt3)

    word_count = dict.fromkeys(txt3,0)
    #print(word_count)

    #for each word (case insensitive), iterate and either add to dictionary if new, or increase count if existing
    for i in txt3:
        if i in word_count:
            word_count[i] +=1
        else:
            pass
    #order descending based on count
    word_count = {k: v for k, v in sorted(word_count.items(), key = lambda item: item[1], reverse=True)[:x]}
    print(filename,word_count)
    f.close()
    return

most_common_words('./data/obama_speech.txt',10)
most_common_words('./data/donald_speech.txt',10)
most_common_words('./data/michelle_obama_speech.txt',10)
most_common_words('./data/melina_trump_speech.txt',10)

#7 Create a python application that checks similarity between two texts
#Take two files or strings as parameters

#functions to clean text - i.e. remove punctuation
#function to remove common support words e.g. and, in etc
#function to check similarity - % of words in text A that are in text B
def similarity_checker(filename1,filename2):
    #open two files
    import re
    filename1_str=str(filename1)
    f1 = open(filename1_str)
    #txt1 = f1.read(1000) # read first 1000 chars
    txt1 = f1.read()

    filename2_str=str(filename2)
    f2 = open(filename2_str)
    txt2 = f2.read()

    #remove punctuation from both files
    txt1_wordsonly = re.sub('[^A-Za-z ]','',txt1)
    txt1_split = txt1_wordsonly.split(' ')
    txt1_unique = list(dict.fromkeys(txt1_split,0))
    

    txt2_wordsonly = re.sub('[^A-Za-z ]','',txt2)
    txt2_split = txt2_wordsonly.split(' ')
    txt2_unique = list(dict.fromkeys(txt2_split,0))
    
    #remove common words
    #adding data folder topath
    import sys
    sys.path.insert(0,"./data")

    from stop_words import stop_words
    #print(stop_words)

    #removing stop words from comparison lists
    txt1_unique_clean = []
    for i in txt1_unique:
        if i in stop_words:
            pass
        else:
            txt1_unique_clean.append(i)
    
    txt2_unique_clean = []
    for i in txt2_unique:
        if i in stop_words:
            pass
        else:
            txt2_unique_clean.append(i)
    
    #counting common words
    count = 0
    for i in txt1_unique_clean:
        if i in txt2_unique_clean:
            count += 1

    similarity = (count/len(txt1_unique_clean))*100
    similarity_formatted = f"{similarity:.2f}"
    return str('Similarity % is ')+str(similarity_formatted)+str('%')

print(similarity_checker('./data/michelle_obama_speech.txt','./data/melina_trump_speech.txt'))
print(similarity_checker('./data/obama_speech.txt','./data/donald_speech.txt'))

#Exercise 8 - Find 10 most repeated words in romeo_and_juliet.txt
most_common_words('./data/romeo_and_juliet.txt',10)

#Exercise 9
#9a - Count the number of lines containing python or Python
#9b - Count the number of lines containing JavaScript, javascript or Javascript
#9c - Count the number of lines containing Java and not JavaScript

#9a
p_count = 0
with open('./data/hacker_news.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    for row in csv_reader:
        #print(str(row))
        if str('Python') in str(row):
            p_count += 1
        elif str('python') in str(row):
            p_count += 1
        else:
            pass
print(p_count)

#9b
j_count = 0
with open('./data/hacker_news.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    for row in csv_reader:
        #print(str(row))
        if str('JavaScript') in str(row):
            j_count += 1
        elif str('javascript') in str(row):
            j_count += 1
        elif str('Javascript') in str(row):
            j_count += 1
        else:
            pass
print(j_count)

#9c
j2_count = 0
with open('./data/hacker_news.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    for row in csv_reader:
        if str('Java') in str(row):
            if str('JavaScript') in str(row):
                pass
            else:
                j2_count += 1

print(j2_count)