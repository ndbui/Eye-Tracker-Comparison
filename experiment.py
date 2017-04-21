from PIL import Image
import numpy as np
from moviepy.editor import *

def drawWindow(frame,centerX,centerY,color):
    dimension = 100
    for x in range(dimension/2 + 1):
        frame[centerX+x , centerY] = color
        frame[centerX , centerY+x] = color
        frame[centerX-x , centerY] = color
        frame[centerX , centerY-x] = color


w, h = 1600 , 900
emptyFrame = 255*np.ones((h, w, 3), dtype=np.uint8)

startX = 100;
startY = 100;
frameCounter = 1;
image_list = []

#First horizontal movements 140 frames
for move1 in range(140):
    frame = 255*np.ones((h, w, 3), dtype=np.uint8)
    startX+=10
    drawWindow(frame,startY,startX,(0,0,0))
    img = Image.fromarray(frame, 'RGB')
    img.save('ExperimentFrames/frame'+str(frameCounter)+'.png')
    image_list.append('ExperimentFrames/frame'+str(frameCounter)+'.png')
    frameCounter+=1

for move2 in range(70):
    frame = 255*np.ones((h, w, 3), dtype=np.uint8)
    startY+=10
    drawWindow(frame,startY,startX,(0,0,0))
    img = Image.fromarray(frame, 'RGB')
    img.save('ExperimentFrames/frame'+str(frameCounter)+'.png')
    image_list.append('ExperimentFrames/frame'+str(frameCounter)+'.png')
    frameCounter+=1

for move3 in range(140):
    frame = 255*np.ones((h, w, 3), dtype=np.uint8)
    startX-=10
    drawWindow(frame,startY,startX,(0,0,0))
    img = Image.fromarray(frame, 'RGB')
    img.save('ExperimentFrames/frame'+str(frameCounter)+'.png')
    image_list.append('ExperimentFrames/frame'+str(frameCounter)+'.png')
    frameCounter+=1

for move4 in range(70):
    frame = 255*np.ones((h, w, 3), dtype=np.uint8)
    startY-=10
    drawWindow(frame,startY,startX,(0,0,0))
    img = Image.fromarray(frame, 'RGB')
    img.save('ExperimentFrames/frame'+str(frameCounter)+'.png')
    image_list.append('ExperimentFrames/frame'+str(frameCounter)+'.png')
    frameCounter+=1

my_clip = ImageSequenceClip(image_list, fps=20)
my_clip.write_videofile("experiment.mp4", codec = "mpeg4", audio = False)
