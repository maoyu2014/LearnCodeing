'模块注释'


import functools

int2 = functools.partial(int, base=2)

print('1000000=',int2('1000000'))
print('1010101=',int2('1010101'))

max2 = functools.partial(max, 10)
print(max2(5,6,7))
