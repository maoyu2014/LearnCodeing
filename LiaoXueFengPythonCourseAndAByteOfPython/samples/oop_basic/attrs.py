class MyDog(object):
    def __len__(self):
        return 100

dog = MyDog()
print(len(dog))

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x *self.x

obj = MyObject()

print(hasattr(obj, 'x'))
print(obj.x)
print(hasattr(obj, 'y'))
print(setattr(obj, 'y', 19))
print(getattr(obj, 'y'))
print(obj.y)
print(getattr(obj, 'z', 404))
print()

print(hasattr(obj, 'power'))
print(getattr(obj, 'power'))
fn = getattr(obj, 'power')
print(fn)
print(fn())
