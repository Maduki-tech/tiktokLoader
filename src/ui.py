from src.getVideoByURL import getVideoByURL
from CTkMessagebox import CTkMessagebox

import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x300")
        self.title("TikTok Downloader")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0,1), weight=1)
        # create the navigation
        self.navigation = customtkinter.CTkTabview(self, width=500, height=300)
        self.navigation.add("URL")
        self.navigation.add("Trending")
        self.navigation.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.navigation.set("URL")
        # create the elements for the URL tab
        self.inputURL = customtkinter.CTkEntry(self.navigation.tab("URL"), placeholder_text="Tiktok URL")
        self.inputURL.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky="ew")
        self.searchURL = customtkinter.CTkButton(self.navigation.tab("URL"), command=self.getVideoByURL, text="Download Video")
        self.searchURL.grid(row=0, column=2, padx=20, pady=20)


        # self.progressbar = customtkinter.CTkProgressBar(self)
        # self.progressbar.grid(padx=20, pady=10)
        # self.progressbar.set(0)


    def getVideoByURL(self):
        if getVideoByURL(self.inputURL.get()):
            CTkMessagebox(title="Download", message="Video wurde erfolgreich heruntergeladen", icon="check", option_1="Thanks")
        else:
            CTkMessagebox(title="Download", message="Video konnte nicht heruntergeladen werden", icon="cancel", option_1="OK")


    def navigation_function(self, index):
        print(index)


