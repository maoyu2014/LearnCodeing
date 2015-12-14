from enum import Enum, unique

@unique
class weekday(Enum):
    Sun=0
    Mon=1
    Tue=2
    Wed=3
    Thu=4
    Fri=5
    Sat=6

day1 = weekday.Mon

print('day1=',day1)
print('weekday.Tue=',weekday.Tue)
print('weekday[\'Tue\']=',weekday['Tue'])
print('weekday.Tue.value=',weekday.Tue.value)
print('day1==weekday.Mon?',day1==weekday.Mon)
print('day1==weekday.Tue?',day1==weekday.Tue)
print('day1==weekday(1)?',day1==weekday(1))

for name,member in weekday.__members__.items():
    print(name,'=>',member,',',member.value)

Month = Enum('Month', ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))

for name,member in Month.__members__.items():
    print(name,'=>',member,',',member.value)

print(type(Enum))
print(type(Month))
print(isinstance(Month.Jan, Month))
print(isinstance(Month.Jan, Enum))
print(issubclass(Month, Enum))
