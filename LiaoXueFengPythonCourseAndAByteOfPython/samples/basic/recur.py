def move(n, a, b, c):
    if n==0:
        return
    move(n-1, a, c, b)
    print(a,'--->',c)
    move(n-1, b, a, c)

move(3, 'A', 'B', 'C')

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

print('fact(1)=', fact(1))
print('fact(5)=', fact(5))
print('fact(10)=', fact(10))
