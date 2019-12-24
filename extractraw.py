raw_directory = '/home/wt/dataset/NCAAbasketball-downloader/raw'

extract_directory_base = '/home/wt/dataset/NCAAbasketball-downloader/extracted'


import os
import threading


filenames=os.listdir(raw_directory)
filenames.sort()

success = 0
total =0
success_lock=threading.Lock()
total_lock=threading.Lock()

sem=threading.Semaphore(8) #最多4个线程并发


import time

time_start=time.time()

def ext(target_dir,cmd):
    with sem:
        os.mkdir(target_dir)

        res = os.system(cmd)

        global success
        global total

        if res==0:
            success_lock.acquire()
            success = success +1
            success_lock.release()

        total_lock.acquire()
        total = total +1
        total_lock.release()

threads = []

for filename in filenames:

    target_dir = os.path.join(extract_directory_base,filename.split('.')[0])
    inputpath = os.path.join(raw_directory,filename)
    #ffmpeg -i s2Hln-wmxBE.mp4 -r 4.995 testdir/%09d.jpg
    cmd="ffmpeg -i "+inputpath+ " -r 4.995 "+target_dir+"/%09d.jpg"

    t_sing = threading.Thread(target=ext, args=(target_dir,cmd))
    threads.append(t_sing)
    t_sing.start()


for t in threads:
    t.join()

print("Total:",total)
print("Total Success:",success)


time_end=time.time()
print('Totally cost time(s):',time_end-time_start)
