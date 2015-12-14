import re

email_address = input('Please:')
m = re.match(r'^(<\w*\s*\w*>)\s*([\w\.\_]+)@(\w+)\.([a-zA-Z]+)$',email_address)
print(m.groups())



'''
if m:
    print('ok!')
else:
    print('failed!')
'''
