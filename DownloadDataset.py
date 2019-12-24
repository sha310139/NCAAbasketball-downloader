import argparse
import sys

from urllib import parse
import os
import re
import urllib
import youtube_dl

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading')

ydl_opts = {
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
    'proxy': '127.0.0.1:1080',
    'verbose':True,
    'outtmpl': '%(id)s.mp4'
}

if __name__ == "__main__":

    bball_file_path = 'C:/Users/chwangteng/Downloads/NCAAbasketball-downloader/bball_dataset_april_4_2.csv'
    raw_path = 'C:/Users/chwangteng/PycharmProjects/NCAAbasketball-downloader/raw' #'C:/Users/chwangteng/Downloads/NCAAbasketball-downloader/raw'

    prefix = 'http://youtube.com/watch?v='

    with open(bball_file_path, "r") as f:
        for line in f:
            line_list = line.split(',')
            v_id = line_list[0]
            v_width = line_list[1]

            # if v_width == '490': #1280
            local_list = os.listdir(raw_path)
            target_file = v_id+'.mp4'
            if target_file in local_list:
                pass
            else:
                target_path = os.path.join(raw_path,target_file)
                URL = prefix + v_id
                print("Video URL: " + URL)

                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([URL])

                print('Done Video:',URL)
