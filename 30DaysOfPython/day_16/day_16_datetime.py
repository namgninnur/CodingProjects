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