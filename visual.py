detections = '/home/wt/dataset/NCAAbasketball-downloader/train_test_val_merged_detections_v2_ts_fixed_head.csv'
#YoutubeId,FrameTime,TopLeftX,TopLeftY,Width,Height,PlayerId

target = 'O8F5jyfYH8k'

frames_jpg_dir = '/home/wt/dataset/NCAAtest/extest'
vi_jpg_dir ='/home/wt/dataset/NCAAtest/vitest'


import pandas as pd
import os
import cv2

bball_file = pd.read_csv(detections,header=0)


def same_frame(rowA ,rowB):
    if rowA['YoutubeId']==rowB['YoutubeId']:
        if rowA['FrameTime']==rowB['FrameTime']:
            return True
    return False


index = 1567400
last = bball_file.loc[0]
boxes = []
boxes.append([bball_file.loc[0,'TopLeftX'],bball_file.loc[0,'TopLeftY'],bball_file.loc[0,'Width'],bball_file.loc[0,'Height']])
while(index<len(bball_file)):
    #print(index)
    if same_frame(last,bball_file.loc[index]):
        boxes.append([bball_file.loc[index,'TopLeftX'],bball_file.loc[index,'TopLeftY'],bball_file.loc[index,'Width'],bball_file.loc[index,'Height']])
    else:
        if last['YoutubeId']==target:
            print(last['FrameTime'] / 1000000.0 * 4.995)
            offset = round(last['FrameTime'] / 1000000.0 * 4.995 )+ 2 #??????????????总之都不太对，不知道是因为IOU太低还是真的extract的时候有错误
            filename = "%09d.jpg" % (offset)
            image_in_path = os.path.join(frames_jpg_dir, filename)
            image_out_path = os.path.join(vi_jpg_dir, filename)

            im = cv2.imread(image_in_path)

            img_height = im.shape[0]
            img_width = im.shape[1]


            for record in boxes:
                cv2.rectangle(im, (int(img_width*record[0]), int(img_height*record[1])), (int(img_width*(record[2]+record[0])), int(img_height*(record[3]+record[1]))), (0, 255, 0), 1)

            cv2.imwrite(image_out_path, im)

        last = bball_file.loc[index]
        boxes = []
        boxes.append(
            [bball_file.loc[index, 'TopLeftX'], bball_file.loc[index, 'TopLeftY'], bball_file.loc[index, 'Width'],
             bball_file.loc[index, 'Height']])

    index = index+1
