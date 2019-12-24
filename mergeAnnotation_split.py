import pandas as pd

detections_csv_path = '/home/wt/dataset/NCAAbasketball-downloader/train_test_val_merged_detections_v2_ts_fixed_head.csv'

batch = 200000


detections_anno = pd.read_csv(detections_csv_path,header=0)

database_length = len(detections_anno)


def same_frame(rowA ,rowB):
    if rowA['YoutubeId']==rowB['YoutubeId']:
        if rowA['FrameTime']==rowB['FrameTime']:
            return True
    return False

last_row = None

i = batch
first = 0


count = 0
while( i < database_length):

    currentrow = detections_anno.loc[i]

    if last_row is None:
        last_row = currentrow
        i = i+1
    else:
        if same_frame(last_row,currentrow):
            i=i+1
        else:
            outpath = '/home/wt/dataset/NCAAbasketball-downloader/train_test_val_merged_detections_v2_ts_fixed_head_' + str(
                count) + '_.csv'
            #提取从first到i-1位置上的数据，前后都闭合
            split_file = detections_anno[first:i]#左闭右开
            split_file.to_csv(outpath,index=None)
            #保存文件
            print(first,i,count)

            count = count+1
            first =i
            if i+batch < database_length:
                i = i+batch
                last_row = detections_anno.loc[i]
            else:
                break


first = i-batch
last = database_length
split_file = detections_anno[first:last]  # 左闭右开
outpath = '/home/wt/dataset/NCAAbasketball-downloader/train_test_val_merged_detections_v2_ts_fixed_head_' + str(
    count) + '_.csv'
split_file.to_csv(outpath, index=None)

print(first,last,count)

#保存最后一个文件
