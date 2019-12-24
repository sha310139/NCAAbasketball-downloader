#bball_dataset_april_4_2_head_refined_manually13.csv
#YoutubeId,VideoWidth,VideoHeight,ClipStartTime,ClipEndTime,EventStartTime,EventEndTime,EventStartBallX,EventStartBallY,EventLabel,TrainValOrTest

#train_test_val_merged_detections_v2_ts_fixed_head.csv
#YoutubeId,FrameTime,TopLeftX,TopLeftY,Width,Height,PlayerId


import pandas as pd
import pickle
import os
import cv2






events_csv_path = '/home/wt/dataset/NCAAbasketball-downloader/bball_dataset_april_4_2_head_refined_manually13.csv'
detections_csv_path = '/home/wt/dataset/NCAAbasketball-downloader/dettectionsplit/train_test_val_merged_detections_v2_ts_fixed_head_20_.csv'


save_index = detections_csv_path.split('_')[-2]



events_anno = pd.read_csv(events_csv_path,header=0)
detections_anno = pd.read_csv(detections_csv_path,header=0)


events_length = len(events_anno)
detections_length = len(detections_anno)

def same_frame(rowA ,rowB):
    if rowA['YoutubeId']==rowB['YoutubeId']:
        if rowA['FrameTime']==rowB['FrameTime']:
            return True
    return False

def same_video(rowA,rowB):
    if rowA['YoutubeId'] == rowB['YoutubeId']:
        return True
    return False

def get_events_anno(start_index,to_save_YoutubeId,to_save_FrameTime_in_ms):

    last_is_same_YoutubeId = False
    now_is_same_YoutubeId = False

    found =False

    for index, row in events_anno.iterrows():
        if found==False:
            if index==start_index:
                found=True
                # 属于Clip集，需要进一步判断是否属于Event
                if row['ClipStartTime'] <= to_save_FrameTime_in_ms and to_save_FrameTime_in_ms <= row['ClipEndTime']:
                    # 属于Clip，有事件
                    if row['EventStartTime'] <= to_save_FrameTime_in_ms and to_save_FrameTime_in_ms <= row['EventEndTime']:
                        return {'add_to_dataset': True,
                                'value': {
                                    'VideoWidth': row['VideoWidth'],
                                    'VideoHeight': row['VideoHeight'],
                                    'ClipStartTime': row['ClipStartTime'],
                                    'ClipEndTime': row['ClipEndTime'],
                                    'EventStartTime': row['EventStartTime'],
                                    'EventEndTime': row['EventEndTime'],
                                    'EventStartBallX': row['EventStartBallX'],
                                    'EventStartBallY': row['EventStartBallY'],
                                    'EventLabel': row['EventLabel'],  # train,test,val
                                    'TrainValOrTest': row['TrainValOrTest']}
                                }
                    # 属于Clip，但是没有事件
                    else:
                        return {'add_to_dataset': True,
                                'value': {
                                    'VideoWidth': row['VideoWidth'],
                                    'VideoHeight': row['VideoHeight'],
                                    'ClipStartTime': row['ClipStartTime'],
                                    'ClipEndTime': row['ClipEndTime'],
                                    'EventStartTime': -1,
                                    'EventEndTime': -1,
                                    'EventStartBallX': -1,
                                    'EventStartBallY': -1,
                                    'EventLabel': 'NOEVENT',
                                    'TrainValOrTest': row['TrainValOrTest']}
                                }
                else:
                    pass

            else:
                continue
        else:
            if row['YoutubeId'] == to_save_YoutubeId:
                # 属于Clip集，需要进一步判断是否属于Event
                if row['ClipStartTime'] < to_save_FrameTime_in_ms and to_save_FrameTime_in_ms < row['ClipEndTime']:
                    # 属于Clip，有事件
                    if row['EventStartTime'] < to_save_FrameTime_in_ms and to_save_FrameTime_in_ms < row['EventEndTime']:
                        return {'add_to_dataset': True,
                                'value': {
                                    'VideoWidth': row['VideoWidth'],
                                    'VideoHeight': row['VideoHeight'],
                                    'ClipStartTime': row['ClipStartTime'],
                                    'ClipEndTime': row['ClipEndTime'],
                                    'EventStartTime': row['EventStartTime'],
                                    'EventEndTime': row['EventEndTime'],
                                    'EventStartBallX': row['EventStartBallX'],
                                    'EventStartBallY': row['EventStartBallY'],
                                    'EventLabel': row['EventLabel'],  # train,test,val
                                    'TrainValOrTest': row['TrainValOrTest']}
                                }
                    # 属于Clip，但是没有事件
                    else:
                        return {'add_to_dataset': True,
                                'value': {
                                    'VideoWidth': row['VideoWidth'],
                                    'VideoHeight': row['VideoHeight'],
                                    'ClipStartTime': row['ClipStartTime'],
                                    'ClipEndTime': row['ClipEndTime'],
                                    'EventStartTime': -1,
                                    'EventEndTime': -1,
                                    'EventStartBallX': -1,
                                    'EventStartBallY': -1,
                                    'EventLabel': 'NOEVENT',
                                    'TrainValOrTest': row['TrainValOrTest']}
                                }
                else:
                    pass
            else:
                break


    return {'add_to_dataset':False}

def get_first_YoutubeId_index(YoutubeId):
    for index, row in events_anno.iterrows():
        if row['YoutubeId']==YoutubeId:
            return index

database_train = []
database_test = []
database_val = []
#YoutubeId,FrameTime,TopLeftX,TopLeftY,Width,Height,PlayerId
last_row = None
boxes = []

start_index = 0

for index, row in detections_anno.iterrows():
    print("Current index:",index,"/", detections_length)
    YoutubeId = row['YoutubeId'] #string
    FrameTime = row['FrameTime'] #int
    TopLeftX = row['TopLeftX'] #float
    TopLeftY = row['TopLeftY'] #float
    Width = row['Width'] #float
    Height = row['Height'] #float
    PlayerId = row['PlayerId'] #string


    #Debug
    # if len(database_train) == 30:
    #
    #     for i in range(30):
    #         rec = database_train[i]
    #         image_in_path = os.path.join('/home/wt/dataset/NCAAbasketball-downloader/extracted',rec['ImagePath'])
    #         test_boxes = rec['Boxes']
    #         save_image_path = '/home/wt/dataset/NCAAbasketball-downloader/testdatabase'
    #
    #         im = cv2.imread(image_in_path)
    #
    #         img_height = im.shape[0]
    #         img_width = im.shape[1]
    #
    #         for box in test_boxes:
    #             TopLeftX = box[0]
    #             TopLeftY = box[1]
    #             Width = box[2]
    #             Height = box[3]
    #             cv2.rectangle(im, (int(img_width*TopLeftX), int(img_height*TopLeftY)), (int(img_width*(Width+TopLeftX)), int(img_height*(Height+TopLeftY))), (0, 255, 0), 1)
    #
    #         cv2.imwrite(os.path.join(save_image_path, rec['YoutubeId']+image_in_path.split('/')[-1]), im)
    #     break

    # First row
    if last_row is None:
        last_row=row
        boxes = []
        boxes.append([TopLeftX, TopLeftY, Width, Height, PlayerId])
        start_index = get_first_YoutubeId_index(YoutubeId)
        continue
    # Other row
    else:

        if same_frame(last_row,row):
            boxes.append([TopLeftX, TopLeftY, Width, Height, PlayerId])
        else:
            to_save_YoutubeId = last_row['YoutubeId']
            to_save_FrameTime_in_us = last_row['FrameTime'] # Metric in detection annotation
            to_save_FrameTime_in_ms = to_save_FrameTime_in_us/1000.0 # Metric in event annotation

            event_anno = get_events_anno(start_index,to_save_YoutubeId,to_save_FrameTime_in_ms)

            if event_anno['add_to_dataset']:
                #把上一帧的所有标注整合之后append到对应的数据库
                record = {} #字典
                offset = round(to_save_FrameTime_in_us / 1000000.0 * 4.995 )+ 2
                filename = "%09d.jpg" % (offset)
                record['ImagePath'] = os.path.join(to_save_YoutubeId,filename)

                record['YoutubeId'] = to_save_YoutubeId
                record['FrameTime'] = to_save_FrameTime_in_us
                record['Boxes'] = boxes #列表嵌套列表
                record["Event"] = event_anno['value'] #字典


                if event_anno['value']['TrainValOrTest'] == 'train':
                    database_train.append(record)
                elif event_anno['value']['TrainValOrTest'] == 'test':
                    database_test.append(record)
                elif event_anno['value']['TrainValOrTest'] == 'val':
                    database_val.append(record)
                else:
                    raise RuntimeError('TrainValOrTest key value error:',event_anno['value']['TrainValOrTest'])
            else:
                pass

            #不需要再重新寻找当前video在events_anno的开始行索引
            if same_video(last_row,row):
                pass
            #重新寻找这个video的开始行
            else:
                start_index = get_first_YoutubeId_index(YoutubeId)
                pass

            last_row = row
            boxes = []
            boxes.append([TopLeftX, TopLeftY, Width, Height, PlayerId])

#处理到最后一行之后的情况
to_save_YoutubeId = last_row['YoutubeId']
to_save_FrameTime_in_us = last_row['FrameTime']  # Metric in detection annotation
to_save_FrameTime_in_ms = to_save_FrameTime_in_us / 1000.0  # Metric in event annotation

event_anno = get_events_anno(start_index, to_save_YoutubeId, to_save_FrameTime_in_ms)


#同上，直接复制粘贴的代码
if event_anno['add_to_dataset']:
    # 把上一帧的所有标注整合之后append到对应的数据库
    record = {}  # 字典
    offset = round(to_save_FrameTime_in_us / 1000000.0 * 4.995) + 2
    filename = "%09d.jpg" % (offset)
    record['ImagePath'] = os.path.join(to_save_YoutubeId, filename)

    record['YoutubeId'] = to_save_YoutubeId
    record['FrameTime'] = to_save_FrameTime_in_us
    record['Boxes'] = boxes  # 列表嵌套列表
    record["Event"] = event_anno['value']  # 字典

    if event_anno['value']['TrainValOrTest'] == 'train':
        database_train.append(record)
    elif event_anno['value']['TrainValOrTest'] == 'test':
        database_test.append(record)
    elif event_anno['value']['TrainValOrTest'] == 'val':
        database_val.append(record)
    else:
        raise RuntimeError('TrainValOrTest key value error:', event_anno['value']['TrainValOrTest'])
else:
    pass






with open('database_train_'+save_index+'_.pkl', 'wb') as f:
    pickle.dump(database_train, f)
with open('database_test_'+save_index+'_.pkl', 'wb') as f:
    pickle.dump(database_test, f)
with open('database_val_'+save_index+'_.pkl', 'wb') as f:
    pickle.dump(database_val, f)

print('database_train_length:', len(database_train))
print('database_test_length:', len(database_test))
print('database_val_length:', len(database_val))

#单线程速度有点慢，但是多线程的话分割再合并，又会复杂一点，反正也就生成一次，所以就没写了。
#多线程，首先把detection的标注文件分成4部分，假设4线程，分割的时候要保证同一个帧不能被阶段，之后也没什么了，就是直接写成多线程。理论上提速4倍，直到达到内存上限。