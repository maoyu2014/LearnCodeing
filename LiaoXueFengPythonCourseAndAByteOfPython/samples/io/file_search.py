import os
import sys

def search(filename, path='.'):
    _files = os.listdir(path)
    for f in _files:
# 注意，下面的isfile判断中一定要写全，即isfile(os.path.join(path,f))
        # 这样才能保证isfile正常工作
        # 否则，如果仅仅是写isfile(f),到了下一层目录中就没法判断了
        if os.path.isfile(os.path.join(path,f)):
            if filename in f:
                print(os.path.join(path,f))
        else:
            search(filename, os.path.join(path,f))


args = sys.argv
if len(args)==1:
    print('please input filename!!!')
else:
    search(args[1])
