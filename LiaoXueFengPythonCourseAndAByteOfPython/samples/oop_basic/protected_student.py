# import test

# print(test._private_1('jk'))
# print(test._abc)
# print(test.__ddd)

class Student(object):
    def __init__(self, name, score, test):
        self.__name = name
        self.__score = score
        self._test =test

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0<=score<=100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    def __privateMethod(self):
        return 'privateMethod'

bart = Student('Bart Simpson', 59, 'justTest')
print('bart.get_name()=',bart.get_name())
bart.set_score(60)
print('bart.get_score()=', bart.get_score())

print(bart._Student__name)
print(bart._test)
# print(bart.__privateMethod())
