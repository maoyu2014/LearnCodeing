import struct

# bmp_header = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
# print(struct.unpack('<ccIIIIIIHH',bmp_header))

def isbmp(filename):
    with open(filename,'rb') as f:
        header = f.read(30)
    ans = struct.unpack('<ccIIIIIIHH',header)
    if not (ans[0]==b'B' and ans[1]==b'M'):
        print('not a bmp file')
    else:
        print('bmp file\'s size is %s * %s, colors is %s.'% (ans[6],ans[7],ans[9]))


isbmp('test.bmp')
isbmp('test2.jpg')

