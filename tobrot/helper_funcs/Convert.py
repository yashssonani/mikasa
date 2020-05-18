import subprocess
from subprocess import call   
import asyncio
#video_file = "input.mkv"
out_put_file_name = "/storage/emulated/0/Videoder/output34.mkv34.mkv"
def convert_video(video_file, out_put_file_name):   
    command = [
        "ffmpeg",
        #"-hide_banner",
        "-i",
        video_file,
        "-c:v",
        #start_time,
        "libx264",
        #end_time,
        #"-async",
        "-c:a",
        #"-strict",
        #"-2",
        #"-c",
        "copy",
        out_put_file_name
    ]
    process =call(command, shell=False)
    return out_put_file_name;
    
a = convert_video("/storage/emulated/0/Telegram/input1.mp4", out_put_file_name)
print(a)
 