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