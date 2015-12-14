# -*- coding: utf-8 -*-

import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup','www.python.org'])
print('Exit code:', r)

print('$ nslookup')
p = subprocess.Popen(['nslookup'],stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output,err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('gbk'))
# 注意，上面用utf-8会有错误，换成gbk就好了
# 所以，我理解的是，我的机器是中文编码的，所以encode的时候可能是用的
# gbk编码的，所以，解码的时候，也要用gbk
print('Exit code:', p.returncode)
