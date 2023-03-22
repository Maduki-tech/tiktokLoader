from src.ui import App   



if __name__ == "__main__":
    ui = App()
    ui.resizable(False, False)
    ui.mainloop()
    # getVideoByURL("https://www.tiktok.com/@abed_comedy/video/7208259632890973445")




#
#
#
# # Liste der Emojis
# emojis = ["❤️", "😂", "🤔", "😍", "👍"]
#
#
#
# # URL des TikTok Videos eingeben
# url = input("Geben Sie die URL des TikTok Videos ein: ")
#
#
#
# # Herunterladen des TikTok Videos
# video_bytes = api.get_video_by_url(url)
#
#
#
# # Speichern des Videos
# with open("original_video.mp4", "wb") as f:
#     f.write(video_bytes)
#
#
#
# # Laden des Videos mit moviepy
# video = VideoFileClip("original_video.mp4")
#
#
#
# # Entfernen des TikTok Wasserzeichens
# watermark = ImageClip("tiktok_watermark.png").set_duration(video.duration)
# video = CompositeVideoClip(
# [video, watermark.set_position(("right", "bottom"))])
#
#
#
# # Spiegeln des Videos
# video = video.fx(vfx.mirror_x)
#
#
#
# # Platzieren von zufälligen Emojis auf dem Video
# for i in range(random.randint(1, 2)):
#     emoji = random.choice(emojis)
#     x = random.uniform(0.1, 0.9)
#     y = random.uniform(0.1, 0.9)
#     txt_clip = TextClip(emoji, fontsize=50, color='white', font='Arial')
#     txt_clip = txt_clip.set_pos((x, y)).set_duration(video.duration)
#     video = CompositeVideoClip([video, txt_clip])
#
#
#
# # Zufälliges Kürzen des Videos
# start = random.uniform(0.2, 0.8)
# end = random.uniform(start+0.1, video.duration)
# video = video.subclip(start, end)
#
#
#
# # Entfernen der Metadaten
# video = video.set_audio(None).set_meta({})
#
#
#
# # Erstellen von fünf bearbeiteten Videos
# for i in range(5):
# # Randomisierung des MD5-Hashes
#     md5 = hashlib.md5(str(random.random()).encode('utf-8')).hexdigest()
# # Speichern des bearbeiteten Videos
#     video.write_videofile(f"edited_video_{md5}.mp4")
