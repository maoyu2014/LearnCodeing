import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s()' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')

now()
print(now.__name__)

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2015-3-25')

now()
print(now.__name__)


def logger(text):
    if isinstance(text, str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('begin %s %s():' %(text, func.__name__))
                ret = func(*args, **kw)
                print('end %s %s():' %(text, func.__name__))
                return ret
            return wrapper
        return decorator
    else:
        func = text
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('begin call %s():' %(func.__name__))
            ret = func(*args, **kw)
            print('end call %s():' %(func.__name__))
            return ret
        return wrapper

@logger
def today():
    print('正在工作...')
today()

@logger('execute')
def today2():
    print('working now....')
today2()
