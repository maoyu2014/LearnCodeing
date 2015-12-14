from datetime import datetime, timedelta, timezone
import re

now = datetime.now()
print('now=',now)
print('type(now)=',type(now))
print()


dt = datetime(2015,4,19,12,20)
print('dt=',dt)
print()

dt = now
print('datetime->timestamp:',dt.timestamp())
print()

t = dt.timestamp()
print('timestamp->datetime:',datetime.fromtimestamp(t))
print('timestamp->datetime as UTC+0:',datetime.utcfromtimestamp(t))
print()

cday = datetime.strptime('2015-6-1 18:19:59','%Y-%m-%d %H:%M:%S')
print('strptime:',cday)
print()

print('strftime:',cday.strftime('%a, %b %d %H:%M'))
print()

print('current datetime =',now)
print('current+10 hours =',now+timedelta(hours=8))
print('current-1 day =',now-timedelta(days=1))
print('current+2.5 days =',now+timedelta(days=2,hours=12))
print()

utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9))) 
print(tokyo_dt2)

def to_timestamp(dt_str, tz_str):
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')    
    num = int(re.split(r'[C:]',tz_str)[1])
    dt = dt.replace(tzinfo=timezone(timedelta(hours=num)))
    return dt.timestamp()


t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1==1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('Pass')


