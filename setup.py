import subprocess
import sys
import platform

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def installffmpeg():
    if platform.system() == 'Darwin':
        subprocess.check_call(["brew", "install", "ffmpeg"])
    elif platform.system() == 'Windows':
        print("Please use MacOs or Linux")
        exit()

if __name__ == '__main__':
    installffmpeg()
    install('tiktokapi')
    install('moviepy')
    install('customtkinter')
    install('CTkMessagebox')


