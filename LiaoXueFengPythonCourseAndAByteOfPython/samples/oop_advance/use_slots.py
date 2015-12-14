from types import MethodType

class Student(object):
    __slots__ = ('name', 'age')    

class GraduateStudent(Student):
    pass

s = Student()
s2 = Student()

'''
s.name = 'Michael'
print(s.name)

def set_age(self, age):
    self.age = age

s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

def set_score(self, score):
    self.score = score

Student.set_score = MethodType(set_score, Student)
s.set_score(100)
print(s.score)
s2.set_score(99)
print(s2.score)
'''

s.name = 'Michael'
s.age = 25
try:
    s.score = 99
except AttributeError as e:
    print('AttribteError:',e)

g = GraduateStudent()
g.score = 99
print('g.score=',g.score)
