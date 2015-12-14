import json

d=dict(name='leilei', age=20, score=88)
data=json.dumps(d)
print('JOSN str:',data)
reborn=json.loads(data)
print('REBORN str:',reborn)
print()

f=open('dump2.txt','w')
json.dump(d,f)
f.close()

with open('dump2.txt','r') as f:
    data2=json.load(f)
print('FROM file:',data2)



class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    def __str__(self):
        return 'Student object (%s %s %s)' % (self.name, self.age, self.score)

s=Student('maolala',20,88)
std_data=json.dumps(s,default=lambda obj:obj.__dict__)
print('Dump Student:',std_data)
rebuild=json.loads(std_data,object_hook=lambda d:Student(d['name'],d['age'],d['score']))
print('REBUILD:',rebuild)
