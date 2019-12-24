bball_file_path = '/home/wt/dataset/NCAAbasketball-downloader/bball_dataset_april_4_2_head.csv'
#bball_file_path = 'testcsv3.csv'
#YoutubeId,VideoWidth,VideoHeight,ClipStartTime,ClipEndTime,EventStartTime,EventEndTime,EventStartBallX,EventStartBallY,EventLabel,TrainValOrTest

import pandas as pd


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 5000)

bball_file = pd.read_csv(bball_file_path,header=0)
bball_file.sort_values(by=['YoutubeId','ClipStartTime','EventEndTime'],inplace=True,ascending=True)

#根据三列排序，暂时保存，方便处理ClipStartTime的-1和标注错误，以便后续将时间标注合并到球员标注文件
bball_file = bball_file.reset_index(drop=True)
#bball_file.to_csv('/home/wt/dataset/NCAAbasketball-downloader/bball_dataset_april_4_2_head_sort.csv',index=None)


#----------------------------------------------------------------------------------------------------------------
#删除错误的EventStartTime行错误
def wrong_row(row):#EventStartTime标注错误，分为-1的没有标注和时间错误
    ClipStartTime = row['ClipStartTime']
    ClipEndTime = row['ClipEndTime']
    EventStartTime = row['EventStartTime']
    EventEndTime = row['EventEndTime']

    #steal ball的-1要不要判断为正常，关系到是否将steal ball当作一个类训练，其实训练也不错，因为可以获取事情高潮的时间点
    #目前所有-1的，包括steal ball判断为异常

    if ClipStartTime <= ClipEndTime:
        if ClipStartTime <= EventStartTime:
            if EventStartTime <= ClipEndTime:
                if ClipStartTime <= EventEndTime:
                    if EventEndTime <= ClipEndTime:
                        if EventStartTime <= EventEndTime:
                            return False
    return True

#根据三个关键字段来判断是不是属于同一个clip.
def same_clip(rowA,rowB):
    if rowA['YoutubeId'] == rowB['YoutubeId']:
        if rowA['ClipStartTime'] == rowB['ClipStartTime'] or  rowA['ClipEndTime'] == rowB['ClipEndTime']:
            return True
    return False
#这个行索引index对于这个datafram来说是合法的
def is_valid_index(index, dataframe):
    if index>=0:
        if index<len(dataframe):
            return True
    return False

bball_file_length = len(bball_file)

#初始化
# last_ClipStartTime = bball_file.loc[bball_file_length-1, 'ClipStartTime']
# last_ClipEndTime = bball_file.loc[bball_file_length-1,'ClipEndTime']
# last_wrong = wrong_row(bball_file.loc[bball_file_length-1])
# last_index = bball_file_length-1

iter_p = 0
indexes_to_delete = []

new_ClipStartTime_index_from=None
while( iter_p < bball_file_length ):

    current_ClipStartTime = bball_file.loc[iter_p, 'ClipStartTime']
    current_ClipEndTime = bball_file.loc[iter_p, 'ClipEndTime']
    current_wrong = wrong_row(bball_file.loc[iter_p])

    if current_wrong==True:

        if new_ClipStartTime_index_from != None:
            if same_clip(bball_file.loc[iter_p], bball_file.loc[new_ClipStartTime_index_from]):
                bball_file.loc[iter_p, 'ClipStartTime'] = bball_file.loc[new_ClipStartTime_index_from,'EventEndTime']

        #加入错误列表单,最后删除
        if iter_p not in indexes_to_delete:
            indexes_to_delete.append(iter_p)
        #当前行成为需要引用的行
        new_ClipStartTime_index_from = iter_p


        #前一条和当前条是属于同一个Clip
        if same_clip(bball_file.loc[iter_p-1],bball_file.loc[iter_p]):
            #前一条也是错的，不用管，直接处理下一行，OK
            if wrong_row(bball_file.loc[iter_p-1]):
                iter_p = iter_p + 1
                continue
            #前一条是正确的，就修改之前所有同Clip的结束时间为前一条（这个前一条是相对于目前行的绝对位置，并不是相对位置）
            else:
                new_ClipEndTime_index_from = iter_p-1
                up_iter = new_ClipEndTime_index_from

                while(up_iter>=0):
                    if same_clip(bball_file.loc[iter_p],bball_file.loc[up_iter]):
                        bball_file.loc[up_iter,'ClipEndTime'] = bball_file.loc[new_ClipEndTime_index_from,'EventEndTime']
                    else:
                        break
                    up_iter = up_iter -1
                #iter_p = iter_p + 1
        # 前一条和当前条并不属于同一个Clip
        else:
            #iter_p = iter_p + 1
            pass


    else:
        if new_ClipStartTime_index_from != None:
            if same_clip(bball_file.loc[iter_p], bball_file.loc[new_ClipStartTime_index_from]):
                bball_file.loc[iter_p, 'ClipStartTime'] = bball_file.loc[new_ClipStartTime_index_from,'EventEndTime']
        #iter_p = iter_p + 1

    iter_p = iter_p + 1



bball_file.drop(indexes_to_delete, inplace=True)
bball_file = bball_file.reset_index(drop=True)
bball_file.to_csv('/home/wt/dataset/NCAAbasketball-downloader/bball_dataset_april_4_2_head_refined.csv',index=None)
