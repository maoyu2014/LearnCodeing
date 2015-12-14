import types

class Animal(object):
    pass

class Dog(Animal):
    pass

class Husky(Dog):
    pass

def fn():
    pass

a = Animal()
d = Dog()
h = Husky()

print(type(123))
print(type('str'))
print(type(None))
print(type(abs))
print(type(a))
print(type(fn))
print()

print(type(123)==type(465))
print(type(123)==int)
print(type('abc')==type('123'))
print(type('abc')==str)
print(type('abc')==type(123))
print(type([1,2,3])==list)
print()

print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x:x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)
print()

print(isinstance(h, Husky))
print(isinstance(h, Dog))
print(isinstance(h, Animal))
print(isinstance(d, Husky))
print(isinstance('a', str))
print(isinstance(123, int))
print(isinstance(b'a', bytes))

print(isinstance([12,34,45], (list, tuple)))
print(isinstance((1,2,3),(list, tuple)))
