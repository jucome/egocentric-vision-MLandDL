import os
import sys
import pandas as pd

from extract_segment import extract_segment, extract_video_start_and_end_secs
from to_low_quality import to_low_quality, print_to_low_quality
# Automatization: To extract segments

## Args:
## 1: Do you want to use the predictions of clip_start_sec?: True or False
use_predictions = False

if len(sys.argv) > 1:
    use_predictions = sys.argv[1] == 'True'

if use_predictions:
    clip_start_sec = "clip_start_sec_pred"
    clip_end_sec = "clip_end_sec_pred"
    root_segmented_videos = './videos_segmented/predictions/'
    sample_50_videos = "sample_50_videos_with_pred.csv"

else:
    clip_start_sec = "clip_start_sec"
    clip_end_sec = "clip_end_sec"
    root_segmented_videos = './videos_segmented/ground_truth/'
    sample_50_videos = "sample_50_videos.csv"


path_validation_file = './nlq_val.json'
path_videos_to_extract = './videos_to_extract/'
path_videos_segmented = root_segmented_videos + 'high_resolution/'
path_videos_lowed = root_segmented_videos + 'low_resolution/'
sample_file_csv = pd.read_csv(sample_50_videos).set_index("id")

# Videos downloaded
videos_downloaded = os.listdir(path_videos_to_extract)

# Extract the segment of interest of the video and low 
for i in range(1, sample_file_csv.shape[0]  +1):
    video_uid, clip_uid, clip_start, clip_end = sample_file_csv.loc[i]["video_uid"], sample_file_csv.loc[i]["clip_uid"], float(sample_file_csv.loc[i][clip_start_sec]), float(sample_file_csv.loc[i][clip_end_sec])
    video_start = extract_video_start_and_end_secs(video_uid, clip_uid, path_validation_file)

    if video_uid in videos_downloaded:
        extract_segment(path_videos_to_extract, path_videos_segmented, video_uid, video_start, clip_start, clip_end, i)

        run = to_low_quality(path_videos_segmented, path_videos_lowed, i)
        
        if run != 0:
            run = to_low_quality(path_videos_segmented, path_videos_lowed, i, scale='852:480')
            if run!=0:
                print_to_low_quality(path_videos_segmented, path_videos_lowed, i, scale='852:480')

print("\n"*5 + "=================> FINISHED :D <=================" + "\n"*5)
