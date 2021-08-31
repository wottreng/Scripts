#!/usr/bin/python3
import os
# requires: ffmpeg
fileList = os.listdir(os.getcwd())
mp3 = ""
#cmd = f"ffmpeg -i '{line}' -vn -acodec libmp3lame -ac 2 -ab 160k -ar 48000 '{mp3}'"
#os.system(cmd)
for line in fileList:
    if ".mp4" in line:
        mp3 = line.split(".mp")[0]
        mp3+=".mp3"
        if mp3 not in fileList:
            print(f"\033[1;31m[*]converting {line}[*]\033[0m")
            os.system(f'ffmpeg -i "{line}" -vn -acodec libmp3lame -ac 2 -ab 160k -ar 48000 "{mp3}"')
        else:
            print(f'\033[0;34m[*]"{mp3}" already exists [*]\033[0m')
