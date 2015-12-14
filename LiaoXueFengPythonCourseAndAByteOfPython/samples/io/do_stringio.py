from io import StringIO

f = StringIO()
f.write('hello')
f.write('')
f.write('world!')
print(f.getvalue())


f = StringIO('水面细风生，\n菱哥慢慢升，\n客厅林小时，\n灯火叶状名。')
while True:
    s = f.readline()
    if s=='':
        break
    print(s.strip())
