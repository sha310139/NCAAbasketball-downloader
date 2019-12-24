import pickle
data = ['aa', 'bb', 'cc']
for i in range(1000000):
    data.append([1,2,3,4,5,6,7,8])
 # dumps 将数据通过特殊的形式转换为只有python语言认识的字符串


with open('tmp.pkl', 'wb') as f:
    pickle.dump(data, f)

# f2 = open('tmp.pkl', 'rb')
# c2 = pickle.load(f2)
# print(c2)