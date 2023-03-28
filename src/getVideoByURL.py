from TikTokApi import TikTokApi
import random
import json
from datetime import date

DEVICE_ID = str(random.randint(10000, 99999999))
# create new folder

today = date.today()
# os.mkdir(today.strftime("%d-%m-%Y"))

def getVideoByURL(url: str):
    # slice url by last /
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
