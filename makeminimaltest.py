import pickle

def sataistic(path):

    #f = open('/home/wt/dataset/NCAAbasketball-downloader/annotations/database_train_merged21.pkl', 'rb')
    f = open(path, 'rb')
    c = pickle.load(f)

    EVENT_CLASSES = {  # 11 classes, excluding steal success Event, including
        "NOEVENT":0,
        "3-pointer success":0,
        "3-pointer failure":0,
        "free-throw success":0,
        "free-throw failure":0,
        "layup success":0,
        "layup failure":0,
        "other 2-pointer success":0,
        "other 2-pointer failure":0,
        "slam dunk success":0,
        "slam dunk failure":0,
        # "steal success",
        # I don't use it
        # because this event has same EventStartTime and EventEndTime,
        # that is,
        # EvetStartTime is marked as -1 in the annotatiaon csv
    }

    count = 0
    max= 5000
    for index, item in enumerate(c):
        label_strig = item['Event']['EventLabel']
        EVENT_CLASSES[label_strig] = EVENT_CLASSES[label_strig] +1

        if label_strig != 'NOEVENT':
            if index < 10000:
                print(item['Event']['EventLabel'], index)

    print(EVENT_CLASSES)




f = open('/home/wt/dataset/NCAAbasketball-downloader/annotations/database_val_merged21.pkl', 'rb')
c = pickle.load(f)



new_list= []
last_item = None
for index, item in enumerate(c):
    if last_item is None:
        last_item = item
    else:
        if item['Event']['EventLabel'] != 'NOEVENT' :
            if last_item['Event']['EventLabel'] == 'NOEVENT':
                new_list.append(last_item)
            new_list.append(item)

        last_item=item

with open('database_val_merged21_lessnoevent.pkl', 'wb') as ff:
    pickle.dump(new_list, ff)


sataistic('database_val_merged21_lessnoevent.pkl')

#train:41777 {'NOEVENT': 6032, '3-pointer success': 3982, '3-pointer failure': 9439, 'free-throw success': 3081, 'free-throw failure': 2098, 'layup success': 3047, 'layup failure': 2872, 'other 2-pointer success': 3610, 'other 2-pointer failure': 7325, 'slam dunk success': 248, 'slam dunk failure': 43}
#test:{'NOEVENT': 828, '3-pointer success': 621, '3-pointer failure': 1403, 'free-throw success': 253, 'free-throw failure': 162, 'layup success': 457, 'layup failure': 422, 'other 2-pointer success': 404, 'other 2-pointer failure': 1093, 'slam dunk success': 37, 'slam dunk failure': 8}
#{'NOEVENT': 381, '3-pointer success': 218, '3-pointer failure': 628, 'free-throw success': 88, 'free-throw failure': 47, 'layup success': 274, 'layup failure': 177, 'other 2-pointer success': 237, 'other 2-pointer failure': 540, 'slam dunk success': 9, 'slam dunk failure': 3}
