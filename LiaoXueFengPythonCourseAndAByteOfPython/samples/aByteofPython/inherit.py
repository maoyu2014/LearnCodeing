class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialize SchoolMember: %s)' % self.name)

    def tell(self):
        print('Name:%s Age:%s ' %(self.name, self.age), end='')

class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialize Teacher: %s)' % self.name)

    def tell(self):
        SchoolMember.tell(self)
        print('Salary:%d' % self.salary)

class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialize Student: %s)' % self.name)

    def tell(self):
        SchoolMember.tell(self)
        print('Marks:%d' % self.marks)

t = Teacher('Mrs.Shrividya',40,30000)
s = Student('Swaroop',22,75)

print()

members = [t,s]
for member in members:
    member.tell()

