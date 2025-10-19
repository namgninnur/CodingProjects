import datetime
print(dir(datetime))

from datetime import datetime
now = datetime.now()
print(now)
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()
print(day,month,year, hour,minute)
print('timestamp is',timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')

christmas = datetime(2025,12,25)
print(christmas)

t = now.strftime("%H:%M:%S, %d/%m/%Y")
print(t)

#Using strptime
date_string = "1 July, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object = ", date_object)

from datetime import date
d = date(2025,12,24)
print(d)
print('current date:',d.today())
today = date.today()
print('current year = ', today.year)
print('current month = ',today.month)

#time
from datetime import time
a = time()
print ('a:',a)
b = time(10,30,51)
print('b:',b)
c = time(hour=10,minute=30,second=51)
print('c:',c)
d = time(10,30,51,20445)
print('d:',d)

#time_difference
today = date(2025,10,17)
new_year = date(2026,1,1)
time_left_this_year = new_year - today
print(time_left_this_year)

t1 = datetime(2025,10,17,17,33)
t2 = datetime(2026,1,1)
diff = t2-t1
print(diff)

#using timedelta
from datetime import timedelta
t1 = timedelta(weeks=12, days = 8, hours = 4, seconds = 3)
t2 = timedelta(days = 5, hours = 19, minutes =10, seconds = 59)
t3= t1-t2
print(t3)

#Exercises
#1
from datetime import datetime
print(now.day, now.month, now.year, now.hour, now.minute, now.timestamp())
#2
print(now.strftime("%m/%d/%Y, %H:%M:%S"))
#3
date_string = "5 December 2017"
sol = datetime.strptime(date_string,"%d %B %Y")
print(sol)
#4
new_year = datetime(2026,1,1)
time_diff = new_year-now
print(time_diff)
#5
jan1970 = datetime(1970,1,1)
time_diff2 = now-jan1970
print(time_diff2)
#6 How can one use date-time module?
# For timing how long different steps in a process take to execute?
# For interacting the outcomes of formula with the variable of current time
# For implementing delays in logic/#for triggering specific actions
