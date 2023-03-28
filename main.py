import json
import asyncio
from TikTokApi import TikTokApi
from flask import Flask
from src.getVideoByURL import getVideoByURL   
import random
import json
from datetime import date
# if __name__ == "__main__":
#     getVideoByURL('https://www.tiktok.com/@aileensager/video/7212075500578147589')


app = Flask(__name__)
@app.route('/')
def index():
    asyncio.set_event_loop(asyncio.new_event_loop())
    # return json.dumps({"error": "Please use /getVideoByURL?url=URL"})
    DEVICE_ID = str(random.randint(10000, 99999999))
# create new folder
    # today = date.today()
# os.mkdir(today.strftime("%d-%m-%Y"))
    # slice url by last /
    url = "https://www.tiktok.com/@aileensager/video/7212075500578147589"
    id = url.split("/")[-1]
    with TikTokApi(custom_device_id=DEVICE_ID) as api:
        print(url)
        video = api.video(id=id)
        info_full = video.info_full()
        json_object = json.dumps(info_full, indent=4)
        #
        # # print(video.info_full())
        # with open("full_info.json", "w") as f:
        #     f.write(json_object)
        #
        # # Bytes of the TikTok video
        # video_data = video.bytes()
        #
        # with open("out.mp4", "wb") as out_file:
        #     out_file.write(video_data)
        if json_object != None:
            return json.dumps(info_full)
        else:
            return json.dumps({"error": "Video not found"})
    # data = getVideoByURL("https://www.tiktok.com/@aileensager/video/7212075500578147589")
    # return data


app.run(host="https://tiktokloader.onrender.com");

