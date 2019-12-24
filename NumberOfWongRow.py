def wrong_row(row):#EventStartTime标注错误，分为-1的没有标注和时间错误
    ClipStartTime = row['ClipStartTime']
    ClipEndTime = row['ClipEndTime']
    EventStartTime = row['EventStartTime']
    EventEndTime = row['EventEndTime']

    if ClipStartTime <= ClipEndTime:
        if ClipStartTime <= EventStartTime:
            if EventStartTime <= ClipEndTime:
                if ClipStartTime <= EventEndTime:
                    if EventEndTime <= ClipEndTime:
                        if EventStartTime <= EventEndTime:
                            return False
    return True

# 总行数： 14548
# 错误行(包括-1和时间不对)： 4415
bball_file_path = '/home/wt/dataset/NCAAbasketball-downloader/bball_dataset_april_4_2_head_refined.csv'


import pandas as pd

count = 0
bball_file = pd.read_csv(bball_file_path,header=0)
for index,row in bball_file.iterrows():
    if wrong_row(row):
        count = count+1
        print(row)
print("总行数：",len(bball_file))
print("错误行(包括-1和时间不对)：",count)