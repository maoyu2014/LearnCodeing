from collections import namedtuple

Point = namedtuple('Point',['x','y'])
p = Point(1,2)
print('Point:',p.x,p.y)
print()

from collections import deque

q=deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)
print()

from collections import defaultdict

dd = defaultdict(lambda:'N/A')
dd['key1']='abc'
print('dd[\'key1\']=',dd['key1'])
print('dd[\'key2\']=',dd['key2'])
print()

from collections import OrderedDict

d = dict([('a',1),('b',2),('c',3)])
print(d)
od = OrderedDict([('a',1),('b',2),('c',3)])
print(od)
print(list(od.keys()))
print()

from collections import Counter

c = Counter()
for ch in 'programming':
    c[ch] += 1
print(c)
print()

dc = dict()
for ch in 'programming':
    if ch in dc:
        dc[ch] += 1
    else:
        dc[ch] = 1 
print(dc)
