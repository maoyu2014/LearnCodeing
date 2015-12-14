import math

def quadratic(a,b,c):
    delta = math.sqrt(b*b-4*a*c)
    if delta>0:
        x1 = (-b + delta) / (2*a)
        x2 = (-b - delta) / (2*a)
        return x1,x2
    elif delta==0:
        x1 = -b / (2*a)
        return x1
    else:
        print('no real results')

print(quadratic(2,3,1))
print(quadratic(1,3,-4))
