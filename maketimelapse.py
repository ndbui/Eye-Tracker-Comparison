import heatmap
import csv
import os
import time
from moviepy.editor import *

#Generate directory path
timestr = time.strftime("%Y%m%d-%H%M%S")
folderpath = "./Results/" + str(timestr)
if not os.path.exists(folderpath):
    os.makedirs(folderpath)
if not os.path.exists(folderpath+"/imgs"):
    os.makedirs(folderpath+"/imgs")
print "Saving heatmaps to " + folderpath

hm = heatmap.Heatmap()
pts = []
mod = 0
counter = 0
imgno = 0

#Generate heatmaps over time intervals of a second
with open('./bin/x86/Release/Output/gazeDataOutput.csv', 'r') as csvfile:
    freader = csv.reader(csvfile)
    r1 = next(freader)
    r2 = next(freader)
    mysize = r2[2].strip()
    mysize = mysize.split(" x ")
    mysize = map(int, mysize)
    mysize = tuple(mysize)
    for row in freader:
        mod = (mod + 1)%2
        if mod == 1:
            counter += 1
            pts.append((int(row[0]), mysize[1] - int(row[1])))
            if counter%50==0:
                imgno += 1
                img = hm.heatmap(pts, size = mysize, area = ((0,0), mysize), dotsize=75) #scale dotsize up?
                img.save(folderpath+ "/imgs/hm" + str(imgno) + ".png")
                pts = []
imgno += 1
img = hm.heatmap(pts, size = mysize, area = ((0,0), mysize), dotsize=75)
img.save(folderpath + "/imgs/hm" + str(imgno) + ".png")

#Generate timelapse video
print "Making timelapse..."
image_list = []
for x in xrange(imgno):
    image_list.append(folderpath + "/imgs/hm" + str(x+1)+".png")
my_clip = ImageSequenceClip(image_list, fps=1)
my_clip.write_videofile(folderpath+"/timelapse.mp4", codec = "mpeg4", audio = False)
