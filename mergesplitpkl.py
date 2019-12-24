




import pickle

phase  = 'val'

dataset = []



#将21个分割的pkl文件，总计63个，分别生成train，test和val
for i in range(21): # 0,1,2,....,19,20


    f = open('pklsplit/database_'+phase+'_'+str(i)+'_.pkl', 'rb')
    c = pickle.load(f)
    dataset.extend(c)


with open('database_'+phase+'_merged21.pkl', 'wb') as ff:
    pickle.dump(dataset, ff)

print("Length:",phase,len(dataset))

#Length: train  359552
#Length: test    46645
#Length: val     22831
