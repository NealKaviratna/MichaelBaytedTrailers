import numpy as np
from moviepy.editor import *

# Michael Bayte Video
def michaelBayte(filename, clipLength, numClips):
    # Open video file
    clip = VideoFileClip(filename)

    # Get volume array from video
    print "\nGathering and processing audio data...\n"
    cut = lambda i: clip.audio.subclip(i,i+1).to_soundarray(fps=22000)
    volume = lambda array: np.sqrt(((1.0*array)**2).mean())
    volumes = [volume(cut(i))*1000 for i in range(0,int(clip.audio.duration-2))]

    # Create volume segments
    print "\nCreating volume segments...\n"
    volumeSegments = [(volumes[i*clipLength]+volumes[i*clipLength+1]+volumes[i*clipLength+2], i) for i in range(len(volumes)/clipLength)]

    # Find loudest segments
    print "\nSelecting Hype\n"
    maxElements = []
    for i in range(numClips):
        maxElements.append(max(volumeSegments))
        volumeSegments.remove(maxElements[i])

    maxElements.sort(key=lambda x: x[1])

    # Cut together video of loudest clips
    print "\nCutting together video\n"
    clips = [clip.subclip(x[1]*clipLength, x[1]*clipLength+clipLength) for x in maxElements]
    video = concatenate_videoclips(clips)
    
    # Write out video
    video.write_videofile(filename + "MichaelBayted.mp4")



