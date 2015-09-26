import numpy as np
from moviepy.editor import *

# Open video file
clip = VideoFileClip("./The.Lord.of.the.Rings.the.Fellowship.of.the.Ring.EXTENDED.2001.720p.BrRip.x264.BOKUTOX.YIFY.mp4")

# Get volume array from video
print "\nGathering audio info...\n"
cut = lambda i: clip.audio.subclip(i,i+1).to_soundarray(fps=22000)
volume = lambda array: np.sqrt(((1.0*array)**2).mean())
volumes = [volume(cut(i))*1000 for i in range(0,int(clip.audio.duration-2))] 

# Create volume segments
print "\nProcessing audio data...\n"
print len(volumes)
volumeSegments = [(volumes[i*3]+volumes[i*3+1]+volumes[i*3+2], i) for i in range(len(volumes)/3)]

# Find five loudest segments
print "\nSelecting Hype\n"
maxElements = []
for i in range(5):
    maxElements.append(max(volumeSegments))
    volumeSegments.remove(maxElements[i])

maxElements.sort(key=lambda x: x[1])

# Cut together video of top 5
print "\nTrimming down video\n"
clip1 = clip.subclip(maxElements[0][1]*3,maxElements[0][1]*3+3)
clip2 = clip.subclip(maxElements[1][1]*3,maxElements[1][1]*3+3)
clip3 = clip.subclip(maxElements[2][1]*3,maxElements[2][1]*3+3)
clip4 = clip.subclip(maxElements[3][1]*3,maxElements[3][1]*3+3)
clip5 = clip.subclip(maxElements[4][1]*3,maxElements[4][1]*3+3)

video = concatenate_videoclips([clip1,clip2,clip3,clip4,clip5])

# Add intro



video.write_videofile("LOTRresult.mp4")

video.close()
