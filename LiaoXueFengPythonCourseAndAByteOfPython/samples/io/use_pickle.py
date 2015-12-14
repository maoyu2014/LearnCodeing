import pickle

d=dict(name='maoyu',age=20, score=88)
data = pickle.dumps(d)
print(data)

reborn = pickle.loads(data)
print(reborn)

f=open('dump.txt','wb')
pickle.dump(d,f)
f.close()
print('已经写入文件')

f=open('dump.txt','rb')
dd=pickle.load(f)
f.close()
print(dd)

