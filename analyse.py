import pandas as pd

origion_path = '/home/wt/dataset/NCAAbasketball-downloader/bball_dataset_april_4_2_head.csv'
final_path = '/home/wt/dataset/NCAAbasketball-downloader/bball_dataset_april_4_2_head_refined.csv'

ori = pd.read_csv(origion_path,header=0)
final = pd.read_csv(final_path,header=0)

ori_EventLabel = ori.groupby(["EventLabel"], as_index=False).size()
print('ori dataset length:',len(ori))
print('ori_EventLabel',ori_EventLabel)


final_EventLabel = final.groupby(["EventLabel"], as_index=False).size()
print('final dataset length:',len(final))
print('final_EventLabel',final_EventLabel)

final_TrainValOrTest = final.groupby(["TrainValOrTest"], as_index=False).size()
print('final_TrainValOrTest',final_TrainValOrTest)

# ori dataset length: 14548
# ori_EventLabel EventLabel
# 3-pointer failure          2482
# 3-pointer success          1142
# free-throw failure          400
# free-throw success          675
# layup failure              1640
# layup success              1550
# other 2-pointer failure    2603
# other 2-pointer success    1264
# slam dunk failure            55
# slam dunk success           358
# steal success              2379

# final dataset length: 10133
# final_EventLabel EventLabel
# 3-pointer failure          2075
# 3-pointer success           964
# free-throw failure          342
# free-throw success          551
# layup failure              1341
# layup success              1303
# other 2-pointer failure    2148
# other 2-pointer success    1073
# slam dunk failure            45
# slam dunk success           291

# final_TrainValOrTest TrainValOrTest
# test     1153
# train    8453
# val       527

