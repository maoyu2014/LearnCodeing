from operator import itemgetter

L = ['bob', 'about', 'Zoo', 'Cridit']
print(sorted(L))
print(sorted(L, key=str.lower))



L=[('Bob',75), ('Adam',92), ('Bart',66), ('Lisa',88)]

def by_name(t):
    return t[0]

def by_score(t):
    return t[1]

L2 = sorted(L, key=by_name)
print(L2)

L3 = sorted(L, key=by_score, reverse=True)
print(L3)

print(sorted(L))
print(sorted(L, key=itemgetter(0)))
print(sorted(L, key=itemgetter(1), reverse=True))
print(sorted(L, key=lambda t:t[1], reverse=True))
