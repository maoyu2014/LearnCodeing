def is_odd(n):
    return n%2==1

L = range(100)

print(list(filter(is_odd, L)))

def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

def is_palindrome(n):
    m = int(str(n)[::-1])
    return m==n

output = filter(is_palindrome, range(1,1000))
print(list(output))
