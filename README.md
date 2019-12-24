# NCAAbasketball-downloader
Download all videos from Stanford's NCAA basketball dataset. Moreover, you can use this library to clean incorrect data, extract frames from videos as per the sample rate in the paper and merge object detection & event detection annotations into a single pkl file for further multitask research.

## Requirements
- Python 3.6
- youtube-dl
- ffmpeg

## Usage

**WARNING：** Before you start any download from YouTube, please be sure, that you have checked [YouTube Terms Of Service](https://www.youtube.com/static?template=terms) and you are compliant. Especially check section 5.H.  

## Download all videos:
```python
python DownloadDataset.py
```
