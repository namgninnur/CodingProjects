import re

#match only searches the start of a string
txt = 'Python is a cool language. Python is a useful tool to know'
match = re.match('Python is a', txt, re.I)
print(match)

span = match.span()
print(span)
start, end = span
print(start, end)
substring = txt[start:end]
print(substring)

#search looks in the entire string
match = re.search('is a', txt, re.I)
print(match)
span = match.span()
print(span)
start, end = span
print(start, end)
substring = txt[start:end]
print(substring)

#findall can find multiple matches
matches = re.findall('is a',txt, re.I)
print(matches)

#re.I ignores the case, otherwise it would need to be formatted like below
txt2 = 'Python is a language but the python is a snake'
matches = re.findall('Python|python', txt2)
print(matches)

#replacing a substring
match_replaced = re.sub('Python|python','C++', txt2,re.I)
print(match_replaced)

txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%','',txt)
print(matches)

#splitting text
split = re.split('\n',matches)
print(split)

#writing RegEx patterns

regex_pattern = r'orange'
txt = 'Orange and grapefruit are fruits. An old saying is that an apple a day keeps the doctor away, but honestly I prefer oranges'
matches = re.findall(regex_pattern, txt)
print(matches)

matches = re.findall(regex_pattern, txt, re.I)
print(matches)

#OR

regex_pattern = r'[Oo]range'
matches = re.findall(regex_pattern, txt)
print(matches)

regex_pattern = r'[Oo]range|an'
matches = re.findall(regex_pattern, txt)
print(matches)

regex_pattern = r'[a].'  # this square bracket means a and . means any character except new line
txt = '''Apple and banana are fruits arnt they?'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['an', 'an', 'an', 'a ', 'ar']

regex_pattern = r'[a]n.*'  # . any character, * any character zero or more times 
txt = '''apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)

txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'  # ? means here that '-' is optional
matches = re.findall(regex_pattern, txt)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']

#Quantifiers
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}'  # exactly four times
matches = re.findall(regex_pattern, txt)
print(matches)  # ['2019', '2021']

#Cart ^
regex_pattern = r'^This'  # ^ means starts with
regex_pattern = r'[^A-Za-z ]+'  # ^ in set character means negation, not A to Z, not a to z, no space

#Exercises
#Level 1
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
matches = re.sub('[^A-Za-z ]','',paragraph)
print(matches)

split = re.split(' ',matches)
split = list(dict.fromkeys(split))
print(split)
counts = {value: 0 for value in split}
print(counts)

for x in counts:
    #re.I ignores the case, otherwise it would need to be formatted like below
    matches = re.findall(x, paragraph)
    counts[x] = len(matches)

final = dict(sorted(counts.items(), key = lambda item: item[1], reverse=True))
print(final)

#Q2
txt = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.'
numbersonly = re.sub('[a-zA-Z]','',txt)
print(numbersonly)