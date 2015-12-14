import hashlib

'''
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())
'''


def calc_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()

'''
db={
    'michael':'e10adc3949ba59abbe56e057f20f883e',
    'bob':'878ef96e86145580c38c87f0410ad153',
    'alice':'99b1c2188db85afee403b1536010c2c9'
}
'''

db={}

def get_md5(new_pass):
    return calc_md5(new_pass)

def register(username, password):
    db[username] = get_md5(password+username+'the-Salt')
    

def log(user, password):
    try:
        if db[user] == get_md5(password+user+'the-Salt'):
            return True
        else:
            return False
    except:
        return False

while True:
    user = input('USER:')
    password=input('PASS:')
    case = input('CASE1:register; CASE2:login! --->')
    if case=='1':
        register(user, password)
        print('register OK!')
    else:
        if log(user,password):
            print('login OK!')
        else:
            print('login NO!')
    print()

