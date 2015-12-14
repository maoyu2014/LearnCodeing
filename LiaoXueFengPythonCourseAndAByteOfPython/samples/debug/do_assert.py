def foo(s):
    n = int(s)
    assert n!=0, 'n is zero!!!'
    return 10/n

def main():
    foo('0')

main()

# python -O **.py可以取消掉assert的功能
