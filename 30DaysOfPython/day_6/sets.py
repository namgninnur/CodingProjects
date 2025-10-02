st1 = set()
st2 = {'train', 'car', 'plane', 'ferry'}
print(len(st1))
print(len(st2))
print('Does set st2 contain plane? ', 'plane' in st2)

st2.add('bus')
print(st2)
st2.update(['bicycle','hovercraft','hot air balloon'])
print(st2)

st2.remove('hot air balloon')
st2.discard('bicycle')
print(st2)
removed_item = st2.pop()
print(removed_item)
print(st2)

st2.clear()
print(st2)

lst = ['red','orange','yellow']
st3 = set(lst)
st4 = set(['blue', 'green', 'purple'])
st5 = st3.union(st4)
print(st5)

multiples_of_three = {0,3,6,9,12,15,18,21,24,27,30}
even_nums = {0,2,4,6,8,10,12,14,16,18,20}
even_mults_of_three = multiples_of_three.intersection(even_nums)
print(even_mults_of_three)

python = {'p','y','t','h','o','n'}
dragon = {'d','r','a','g','o','n'}
rag = {'r','a','g'}
reddragon = dragon.union(['r','e','d'])
print(reddragon)

print(rag.issubset(dragon))
print(dragon.issuperset(rag))
print(python.issuperset(rag))

non_shared_letters = dragon.symmetric_difference(python)
print(non_shared_letters)

print(rag.isdisjoint(python))

#Exercises
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
# level 1
#1-4
print(len(it_companies))
it_companies.add('Twitter')
it_companies.update(['OpenAI','Cisco','Canva'])
it_companies.remove('Oracle')
#Q5 - Remove produces an error if subject is not in set, while discard does not

#level2
#1-7
ABjoined = A.update(B)
ABintersection = A.intersection(B)
print('Is A a subset of B ?', A.issubset(B))
print('Are A and B disjoint sets? ', A.isdisjoint(B))
AB = A.union(B)
BA = B.union(A)
ABsymmetricdiff = A.symmetric_difference(B)
del A, B, AB, BA, ABjoined, ABintersection

#Level 3
#Q1
age_st = set(age)
print('The length of the list is ', len(age), ' and the length of the set is ', len(age_st))
#Q2
#Sets cannot have repeat members and have no indexing
#String is a combination of text
#Tuples are immutable
#Lists have indexing and can have repeat members
#Q3
sentence = ('I am a teacher and I love to inspire and teach people')
sentence = sentence.split()
sentence = set(sentence)
print(len(sentence))