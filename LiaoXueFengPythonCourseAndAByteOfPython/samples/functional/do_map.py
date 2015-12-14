from functools import reduce

def f(x):
    return x*x

print(list(map(f, [1,2,3,4,5,6,7,8,9])))

def normalize(name):
    name = name[0].upper() + name[1:].lower()
    return name

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

def prod(L):
    def multi(x,y):
        return x*y
    return reduce(multi, L)

print('3*5*7*9=', prod([3,5,7,9]))
    
def str2float(s):
    def char2num(s):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    Ln = s.split('.')
    m = reduce(lambda x,y:x*10+y, map(char2num,Ln[0]), 0)
    n=0
    if len(Ln)>1:
        n = reduce(lambda x,y:x*0.1+y, map(char2num, reversed(Ln[1])))
    return m+n*0.1

print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.456000'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))
