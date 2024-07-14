import os

def to_low_quality(path_videos_to_low, path_videos_lowed, video_id, scale=None):
    if not scale:
        command = "ffmpeg -loglevel error -i " + path_videos_to_low + str(video_id) + ".mp4 -filter:v scale=-1:480 -c:a copy " + path_videos_lowed + str(video_id) + ".mp4"
    else:
        os.remove(path_videos_lowed + str(video_id) + ".mp4")
        command = "ffmpeg -loglevel error -i " + path_videos_to_low + str(video_id) + ".mp4 -filter:v scale=" + scale + " -c:a copy " + path_videos_lowed + str(video_id) + ".mp4"
    return os.system(command)

def print_to_low_quality(path_videos_to_low, path_videos_lowed, video_id, scale=None):
    if not scale:
        command = "ffmpeg -i " + path_videos_to_low + str(video_id) + ".mp4 -filter:v scale=-1:480 -c:a copy " + path_videos_lowed + str(video_id) + ".mp4"
    else:
        command = "ffmpeg -i " + path_videos_to_low + str(video_id) + ".mp4 -filter:v scale=" + scale + " -c:a copy " + path_videos_lowed + str(video_id) + ".mp4"
    print(command)