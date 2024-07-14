import os
import pandas as pd
from math import floor, ceil

# Automatization: To extract segments
def extract_video_start_and_end_secs(video_uid, clip_uid, path_validation_file):
    import json

    with open(path_validation_file) as nlq_val_file:
        nlq_val = json.load(nlq_val_file)

    for video in nlq_val['videos']:
        if video['video_uid'] == video_uid:

            for clip in video['clips']:
                if clip['clip_uid'] == clip_uid:
                    return clip["video_start_sec"]
                
def extract_segment(path_videos_to_extract, path_videos_segmented, video_uid, video_start, clip_start, clip_end, i):
    command = "ffmpeg -loglevel error -i " + path_videos_to_extract + video_uid + " -ss " + str(floor(abs(video_start + clip_start))) + " -to " + str(ceil(abs(video_start + clip_end))) + " -c copy " + path_videos_segmented + str(i) + ".mp4"
    os.system(command)
