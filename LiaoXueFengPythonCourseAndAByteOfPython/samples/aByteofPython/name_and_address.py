import pickle
import sys

class Person:
    def __init__(self, name):
        self.name = name


# reading data from file
# if it is the first time running this software,empty dict()
try:
    with open('./name_and_address.txt','rb') as f:
        mydict = pickle.load(f)
except FileNotFoundError as e:
    mydict = dict()

# 1
def add_person():
    print('请输入姓名：')
    name = input()
    print('请输入电话号码：')
    telephone = input()
    print('请输入电子邮件：')
    email = input()
    p = Person(name)
    p.telephone = telephone
    p.email = email
    mydict[p.name]=p

#2
def modify_person():
    print('请输入姓名：')
    name = input()
    if name in mydict:
        p = mydict[name]
        mydict.pop(name)
        print('请输入姓名：')
        name = input()
        print('请输入电话号码：')
        telephone = input()
        print('请输入电子邮件：')
        email = input()
        p.name = name
        p.telephone = telephone
        p.email = email
        mydict[p.name] = p
    else:
        print('此人不存在，请重新输入姓名')

# 3
def delete_person():
    print('请输入姓名：')
    name = input()
    if name in mydict:
        p = mydict[name]
        mydict.pop(name)
    else:
        print('此人不存在，请重新输入姓名')

# 4
def search_person():
    print('请输入姓名：')
    name = input()
    if name in mydict:
        p = mydict[name]
        print('此人信息如下：','name:',p.name,'telephone:',p.telephone,'email:',p.email)
    else:
        print('此人不存在，请重新输入姓名')


# 5 
def out_software():
    with open('./name_and_address.txt','wb') as f:
        pickle.dump(mydict, f)
    sys.exit()

# tell user how to use
while True:
    print('\n按1：添加联系人\n按2：修改联系人\n按3：删除联系人\n按4：搜索联系人\nquit退出!')
    get_command = input()

    if get_command=='0':
        for p in mydict.values():
            print('name:',p.name,'telephone:',p.telephone,'email:',p.email)
    elif get_command=='1':
        add_person()
    elif get_command=='2':
        modify_person()
    elif get_command=='3':
        delete_person() 
    elif get_command=='4':
        search_person() 
    elif get_command=='quit':
        out_software()
    else:
        print('输入错误，请重新输入，1-4之间：')

