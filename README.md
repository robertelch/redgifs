# redgifs
a small python module to interact with https://redgifs.com/

# installation:
```
pip install git+https://github.com/NacreousDawn596/redgifs -U
```

# Usage:
 init the module:
 ```py
 import redgifs
 
 api = redgifs.Redgifs()
 ```
 
 to display your temp token:
 ```py
 import redgifs
 
 api = redgifs.Redgifs()
 print(api.token)
 ```
 
 to search some videos:
 ```py
 import redgifs
 
 api = redgifs.Redgifs()
 results = api.search("Keyword", count) # count should be between 10..80
 ```
 
 to get a video by ID:
 ```py
 import redgifs
 
 api = redgifs.Redgifs()
 video = api.getGifById("id")
 ```
 
 to get a list of videos by ids:
 ```py
 import redgifs
 
 api = redgifs.Redgifs()
 videos = api.getGifsById("id1 id2 id3")
 ```
 
 to get similar videos to a video:
 ```py
 import redgifs
 
 api = redgifs.Redgifs()
 similar_videos = api.getSimilarGifsTo("video_id")
 ```
 
 to download a video:
 ```py
 import redgifs
 
 api = redgifs.Redgifs()
 api.download("video_id")
 #or:
 video = api.getGifById("id")
 video.download()
 ```
 
 **if you got any suggestions or issues, don't forget to report them!!**
