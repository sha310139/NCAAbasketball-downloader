# NCAAbasketball-downloader
Download all videos from Stanford's [NCAA basketball dataset](http://basketballattention.appspot.com/). Moreover, you can use this library to clean incorrect data, extract frames from videos as per the sample rate in the paper [Detecting Events and Key Actors in Multi-Person Videos](https://arxiv.org/abs/1511.02917) and merge object detection & event detection annotations into a single pkl file for further multitask research.

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
