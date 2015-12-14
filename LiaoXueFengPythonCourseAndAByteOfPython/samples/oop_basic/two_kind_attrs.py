'''
class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90
print(s.score)
print(s.name)
'''

class Student(object):
    name = 'Student'

s = Student()
print(s.name)
print(Student.name,'\n')

s.name = 'Michael'
print(s.name)
print(Student.name, '\n')

del s.name
print(s.name)

