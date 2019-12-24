bball_path = '/home/wt/dataset/NCAAbasketball-downloader/bball_dataset_april_4_2_head_refined_manually13.csv'

import pandas as pd

ori = pd.read_csv(bball_path,header=0)



valtime = 0
testtime = 0
for index, row in ori.iterrows():
    if row['TrainValOrTest']=='val':
        valtime = valtime + float(row['EventEndTime'])-float(row['EventStartTime'])
    if row['TrainValOrTest'] == 'test':
        testtime = testtime + float(row['EventEndTime']) - float(row['EventStartTime'])

print('valtime(s)',valtime/1000.0)
print('valtime frames',valtime/1000.0 * 4.995)
print('testtime(s)',testtime/1000.0)
print('testtime frames',testtime/1000.0 * 4.995)


# valtime(s) 598.9240539999986
# valtime frames 2991.625649729993
# testtime(s) 1319.8707520000114
# testtime frames 6592.7544062400575

