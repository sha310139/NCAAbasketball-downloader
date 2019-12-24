bball_file_path = '/home/wt/dataset/NCAAbasketball-downloader/bball_dataset_april_4_2_head.csv'
detections = '/home/wt/dataset/NCAAbasketball-downloader/train_test_val_merged_detections_v2_ts_fixed.csv'

target = 's2Hln-wmxBE'
#target = 'rBQ4-zr22Nc'

frames_jpg_dir = '/home/wt/dataset/NCAAtest/testdir'
vi_jpg_dir ='/home/wt/dataset/NCAAtest/vi'

index = 0

first = None

last = None

cache = []

import datetime


# record = []
# with open(bball_file_path, "r") as f:
#     for index, line in enumerate(f):
#         line_list = line.strip('\n').split(',')
#         v_id = line_list[0]
#         if line_list[3]!='-1':
#             seconds = float(line_list[3])/1000.0
#             m, s = divmod(seconds, 60)
#             h, m = divmod(m, 60)
#             line_list[3] = "%d:%02d:%02d" % (h, m, s)
#         if line_list[4]!='-1':
#             seconds = float(line_list[4])/1000.0
#             m, s = divmod(seconds, 60)
#             h, m = divmod(m, 60)
#             line_list[4] = "%d:%02d:%02d" % (h, m, s)
#         if line_list[5]!='-1':
#             seconds = float(line_list[5])/1000.0
#             m, s = divmod(seconds, 60)
#             h, m = divmod(m, 60)
#             line_list[5] = "%d:%02d:%02d" % (h, m, s)
#         if line_list[6]!='-1':
#             seconds = float(line_list[6])/1000.0
#             m, s = divmod(seconds, 60)
#             h, m = divmod(m, 60)
#             line_list[6] = "%d:%02d:%02d" % (h, m, s)
#         if v_id == target:
#             record.append(line)
#             print(line_list)




# with open(detections, "r") as f:
#     for index, line in enumerate(f):
#         line_list = line.split(',')
#         v_id = line_list[0]
#         if v_id==target:
#             if first==None:
#                 first = line
#             last=line
#             if len(cache)<20 and line_list[1] not in cache:
#                 cache.append(line_list[1])
#     print(first)
#     print(last)
#     for l in cache:
#         print(l)
#     for l in cache:
#         print(float(l)/1000000.0/0.2002)

# s2Hln - wmxBE, 00312378733, 0.3039, 0.4342, 0.1164, 0.2634, person_2_00301768133
# s2Hln - wmxBE, 04709871833, 0.7805, 0.4520, 0.0702, 0.2300, person_77_04687749733


import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 5000)
nasdaq = pd.read_csv(bball_file_path,header=0)

want = nasdaq[nasdaq['YoutubeId']==target]

want.sort_values(by=['ClipStartTime','EventEndTime'],inplace=True,ascending=True)


for index, row in want.iterrows():

    # if row['ClipStartTime']<row['EventStartTime'] and row['EventStartTime']<row['ClipEndTime']:
    #     pass
    # else:
    #     want.loc[index, 'EventStartTime'] = row['EventStartTime'] * 10.0

    if row['ClipStartTime']!= -1 :
                seconds = row['ClipStartTime']/1000.0
                m, s = divmod(seconds, 60)
                h, m = divmod(m, 60)
                want.loc[index,'ClipStartTime'] = "%d:%02d:%02d" % (h, m, s)
    if row['ClipEndTime']!= -1 :
                seconds = row['ClipEndTime']/1000.0
                m, s = divmod(seconds, 60)
                h, m = divmod(m, 60)
                want.loc[index,'ClipEndTime'] = "%d:%02d:%02d" % (h, m, s)
    if row['EventStartTime']!= -1 :
                seconds = row['EventStartTime']/1000.0
                m, s = divmod(seconds, 60)
                h, m = divmod(m, 60)
                want.loc[index,'EventStartTime'] = "%d:%02d:%02d" % (h, m, s)
    if row['EventEndTime']!= -1 :
                seconds = row['EventEndTime']/1000.0
                m, s = divmod(seconds, 60)
                h, m = divmod(m, 60)
                want.loc[index,'EventEndTime'] = "%d:%02d:%02d" % (h, m, s)

print(want.head(len(want)))




# negaone = nasdaq[nasdaq['EventStartTime']==-1]
# # 3278
#
# print(len(negaone))
# print(len(nasdaq))
# print(1-len(negaone)/len(nasdaq))
#
# def wrong(ClipStartTime,ClipEndTime, EventStartTime, EventEndTime):
#     if ClipStartTime < ClipEndTime:
#         if ClipStartTime < EventStartTime:
#             if EventStartTime < ClipEndTime:
#                 if ClipStartTime < EventEndTime:
#                     if EventEndTime < ClipEndTime:
#                         if EventStartTime < EventEndTime:
#                             return False
#     return True
#
#
# wrong1 = 0
# for index, row in nasdaq.iterrows():
#     if row['EventStartTime']!=-1:
#         if wrong(row['ClipStartTime'],row['ClipEndTime'],row['EventStartTime'],row['EventEndTime']):
#             #print(row)
#             wrong1 = wrong1+1
#
# print('wrong1',wrong1)
#
#
# for index, row in nasdaq.iterrows():
#     if row['EventStartTime']!=-1:
#         if wrong(row['ClipStartTime'],row['ClipEndTime'],row['EventStartTime'],row['EventEndTime']):
#             nasdaq.loc[index, 'EventStartTime'] = row['EventStartTime'] * 10
#
#
#
# wrong2 = 0
# for index, row in nasdaq.iterrows():
#     if row['EventStartTime']!=-1:
#         if wrong(row['ClipStartTime'],row['ClipEndTime'],row['EventStartTime'],row['EventEndTime']):
#             print(row.values)
#             wrong2 = wrong2+1
#
# print('wrong2',wrong2)


