def consumer():
    r=''
    while True:
        n=yield r
        print('[CONSUMER] consuming %s...' % n)
        r='200 OK'


def produce(c):
    c.send(None)
    n=0
    while n<5:
        n += 1
        print('[PROCEDURE] Producing %s...' % n)
        r=c.send(n)
        print('[PROCEDURE] Consumer return: %s' % r)
    c.close()

c=consumer()
produce(c)




