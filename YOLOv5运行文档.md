```
python.exe detect.py --source 0

python.exe detect.py --source 0
```



```
python detect.py --source 0  # webcam
                          img.jpg  # image
                          vid.mp4  # video
                          screen  # screenshot
                          path/  # directory
                          'path/*.jpg'  # glob
                          'https://youtu.be/Zgi9g1ksQHc'  # YouTube
                          'rtsp://example.com/media.mp4'  # RTSP, RTMP, HTTP stream
```

```
RTSP：
python detect.py --source OPTION = rtsp://admin:nqiv123123@192.168.1.12/h264/ch1/main/av_stream

网络摄像头：（OPTION = 0）用于从连接的网络摄像头检测活体
Image : (OPTION = filename.jpg)创建带有对象检测叠加层的图像副本
视频：（OPTION = filename.mp4）创建带有对象检测覆盖的视频副本
目录：（OPTION = directory_name/）使用对象检测覆盖创建所有文件的副本
全局文件类型(OPTION = directory_name/*.jpg)创建带有对象检测覆盖的所有文件的副本
RTSP 流：（OPTION = rtsp://170.93.143.139/rtplive/470011e600ef003a004ee33696235daa）用于从流中检测活体
RTMP 流：（OPTION = rtmp://192.168.1.105/live/test）用于从shi'pi流中检测活体
HTTP 流：（OPTION = http://112.50.243.8/PLTV/88888888/224/3221225900/1.m3u8）用于从流中检测活体
```

