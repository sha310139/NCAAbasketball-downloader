# NCAAbasketball-downloader
Download all videos from Stanford's [NCAA basketball dataset](http://basketballattention.appspot.com/). Moreover, you can use this library to clean incorrect data, extract frames from videos as per the sample rate in the paper [Detecting Events and Key Actors in Multi-Person Videos](https://arxiv.org/abs/1511.02917) and merge object detection & event detection annotations into a single pkl file for further multitask research. Since the codes are not well organized, please modify the codes yourself.   
If you want to download all videos from OneDrive, please contact me <18020100027@pop.zjgsu.edu.cn>.

## Requirements
- Python 3.6
- [youtube-dl](https://github.com/ytdl-org/youtube-dl)
- ffmpeg

## Usage

**WARNING：** Before you start any download from YouTube, please be sure, that you have checked [YouTube Terms Of Service](https://www.youtube.com/static?template=terms) and you are compliant. Especially check section 5.H.  

### Download all videos(youtube-dl):
This requires 112GB of network traffic and disk space.  
```python
python DownloadDataset.py
```
  
### Extract frames from videos (Multi Thread, ffmpeg based):
**WARNING：** Video will be resampled to 4.995 frames per second, as the origional fps is 29.97.  
```python
python extractraw.py
```

### Clean the dataset:
**WARNING：** This action will delete wrong annotations. Specifically, wrong annotations are those:
1. With '-1' lable in EventStartTime ( Although the author think 'steal success' has same EventStartTime and EventEndTime)
2. 'EventStartTime' and 'EventEndTime' not reasonable values as per 'ClipStartTime' and 'ClipEndTime'  
```python
def wrong_row(row):
    if ClipStartTime <= ClipEndTime:
        if ClipStartTime <= EventStartTime:
            if EventStartTime <= ClipEndTime:
                if ClipStartTime <= EventEndTime:
                    if EventEndTime <= ClipEndTime:
                        if EventStartTime <= EventEndTime:
                            return False
    return True
```
```python
python SortAndDelete.py
```
### Merge object detection & event detection annotations to frame by frame (for Multitask research, which I do):
This action is very slow, so I split one big annotation file(train_test_val_merged_detections_v2_ts_fixed_head.csv) to 20 splits and do them simultaneously.
```python
python mergeAnnotation_split.py
python mergeAnnotation.py
python mergesplitpkl.py
```
## References
- [[1]Detecting Events and Key Actors in Multi-Person Videos](https://arxiv.org/abs/1511.02917)
