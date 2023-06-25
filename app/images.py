from datetime import timedelta
import cv2
import numpy as np
import os
import moviepy.editor


SAVING_FRAMES_PER_SECOND = 30





def get_saving_frames_durations(cap, saving_fps):
    s = []
    clip_duration = cap.get(cv2.CAP_PROP_FRAME_COUNT) / cap.get(cv2.CAP_PROP_FPS)
    for i in np.arange(0, clip_duration, 1 / saving_fps):
        s.append(i)
    return s




durations = []
def main(video_file,uuid):
    filename, _ = os.path.splitext(video_file)
    filename = "media/images/" + str(uuid)
    
    # try :
    video = moviepy.editor.VideoFileClip(video_file)
    # except OSError :
    #     # video_file
    #     print(video_file)
    #     current = os.getcwd() + '\\media\\videos\\v.mp4'
    #     os.replace(video_file,current)
    #     video = moviepy.editor.VideoFileClip(current)
        

    audio = video.audio

    audio.write_audiofile(f"media/audio/{uuid}.mp3")
    audio.close()

    if not os.path.isdir(filename):
        os.mkdir(filename)

    cap = cv2.VideoCapture(video_file)
    fps = cap.get(cv2.CAP_PROP_FPS)

    saving_frames_per_second = min(fps, SAVING_FRAMES_PER_SECOND)
    saving_frames_durations = get_saving_frames_durations(cap, saving_frames_per_second)

    count = 0
    
    while True:
        is_read, frame = cap.read()
        if not is_read:
            break
        frame_duration = count / fps
        try:
            closest_duration = saving_frames_durations[0]
        except IndexError:
            break
        if frame_duration >= closest_duration:
            durations.append(f'{frame_duration}')
            cv2.imwrite(os.path.join(filename, f"{frame_duration}.jpg"), frame)
            try:
                saving_frames_durations.pop(0)
            except IndexError:
                pass
        count += 1
    return '@'.join(durations)

