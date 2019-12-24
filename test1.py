import argparse
import sys

from urllib import parse
import os
import re
import urllib
import youtube_dl


if __name__ == "__main__":

    bball_file_path = 'C:/Users/chwangteng/Downloads/NCAAbasketball-downloader/bball_dataset_april_4_2.csv'

    ids =[]

    # with open(bball_file_path, "r") as f:
    #     for line in f:
    #         line_list = line.split(',')
    #         v_id = line_list[0]
    #         ClipStartTime = float(line_list[3])
    #         ClipEndTime = float(line_list[4])
    #         print(ClipEndTime-ClipStartTime)
    #         if v_id not in ids:
    #             ids.append(v_id)
    #
    # print(len(ids))

    v_wids = []

    with open(bball_file_path, "r") as f:
        for line in f:
            line_list = line.split(',')
            v_id = line_list[0]
            v_width = line_list[1]
            ClipStartTime = float(line_list[3])
            ClipEndTime = float(line_list[4])
            print(ClipEndTime-ClipStartTime)
            if v_width not in v_wids:
                v_wids.append(v_width)

    print(len(v_wids))
    print(v_wids)



# ffmpeg -i XXX.mp4 -r 4.995005 XXX/%09d.jpg
#-r video frames per second

