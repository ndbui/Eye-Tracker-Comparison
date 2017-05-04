from PIL import Image
import numpy as np
import math
from moviepy.editor import *

def drawSquare(frame,centerY,centerX,color,dimension):
    for y in range(dimension):
        for x in range(dimension):
            frame[centerY - math.floor(dimension/2) + y, centerX - math.floor(dimension/2) + x] = color

def drawWindow(frame,centerY,centerX,color,dimension):
    for x in range(dimension/2 + 1):
        frame[centerY+x , centerX] = color
        frame[centerY , centerX+x] = color
        frame[centerY-x , centerX] = color
        frame[centerY , centerX-x] = color
        # drawSquare(frame,centerY,centerX,(255,0,0),13)

def pause(frame,centerY,centerX,seconds,counter):
    drawSquare(frame,centerY,centerX,(255,0,0),13)
    for x in range(int(seconds*20)):
        img = Image.fromarray(frame, 'RGB')
        img.save('ExperimentFrames/frame'+str(counter + x)+'.png')
        image_list.append('ExperimentFrames/frame'+str(counter + x)+'.png')


w, h = 1600 , 900
rowSteps = 4;
emptyFrame = 255*np.ones((h, w, 3), dtype=np.uint8)

startX = 100;
startY = 100;
frameCounter = 1;
image_list = []

#First row for calibration
for row in range(rowSteps):
    for move in range(35):
        frame = 255*np.ones((h, w, 3), dtype=np.uint8)
        startX+=10
        drawWindow(frame,startY,startX,(0,0,0),100)
        img = Image.fromarray(frame, 'RGB')
        img.save('ExperimentFrames/frame'+str(frameCounter)+'.png')
        image_list.append('ExperimentFrames/frame'+str(frameCounter)+'.png')
        frameCounter+=1

    pause(frame,startY,startX,1.5,frameCounter)
    frameCounter+=30

for move in range(23):
    frame = 255*np.ones((h, w, 3), dtype=np.uint8)
    startY+=10
    drawWindow(frame,startY,startX,(0,0,0),100)
    img = Image.fromarray(frame, 'RGB')
    img.save('ExperimentFrames/frame'+str(frameCounter)+'.png')
    image_list.append('ExperimentFrames/frame'+str(frameCounter)+'.png')
    frameCounter+=1

pause(frame,startY,startX,1.5,frameCounter)
frameCounter+=30

for row in range(rowSteps):
    for move in range(35):
        frame = 255*np.ones((h, w, 3), dtype=np.uint8)
        startX-=10
        drawWindow(frame,startY,startX,(0,0,0),100)
        img = Image.fromarray(frame, 'RGB')
        img.save('ExperimentFrames/frame'+str(frameCounter)+'.png')
        image_list.append('ExperimentFrames/frame'+str(frameCounter)+'.png')
        frameCounter+=1

    pause(frame,startY,startX,1.5,frameCounter)
    frameCounter+=30

for move in range(23):
    frame = 255*np.ones((h, w, 3), dtype=np.uint8)
    startY+=10
    drawWindow(frame,startY,startX,(0,0,0),100)
    img = Image.fromarray(frame, 'RGB')
    img.save('ExperimentFrames/frame'+str(frameCounter)+'.png')
    image_list.append('ExperimentFrames/frame'+str(frameCounter)+'.png')
    frameCounter+=1

pause(frame,startY,startX,1.5,frameCounter)
frameCounter+=30

for row in range(rowSteps):
    for move in range(35):
        frame = 255*np.ones((h, w, 3), dtype=np.uint8)
        startX+=10
        drawWindow(frame,startY,startX,(0,0,0),100)
        img = Image.fromarray(frame, 'RGB')
        img.save('ExperimentFrames/frame'+str(frameCounter)+'.png')
        image_list.append('ExperimentFrames/frame'+str(frameCounter)+'.png')
        frameCounter+=1

    pause(frame,startY,startX,1.5,frameCounter)
    frameCounter+=30

for move in range(23):
    frame = 255*np.ones((h, w, 3), dtype=np.uint8)
    startY+=10
    drawWindow(frame,startY,startX,(0,0,0),100)
    img = Image.fromarray(frame, 'RGB')
    img.save('ExperimentFrames/frame'+str(frameCounter)+'.png')
    image_list.append('ExperimentFrames/frame'+str(frameCounter)+'.png')
    frameCounter+=1

pause(frame,startY,startX,1.5,frameCounter)
frameCounter+=30

for row in range(rowSteps):
    for move in range(35):
        frame = 255*np.ones((h, w, 3), dtype=np.uint8)
        startX-=10
        drawWindow(frame,startY,startX,(0,0,0),100)
        img = Image.fromarray(frame, 'RGB')
        img.save('ExperimentFrames/frame'+str(frameCounter)+'.png')
        image_list.append('ExperimentFrames/frame'+str(frameCounter)+'.png')
        frameCounter+=1

    pause(frame,startY,startX,1.5,frameCounter)
    frameCounter+=30


#
# for move in range(140):
#     frame = 255*np.ones((h, w, 3), dtype=np.uint8)
#     startX-=10
#     drawWindow(frame,startY,startX,(0,0,0),100)
#     img = Image.fromarray(frame, 'RGB')
#     img.save('ExperimentFrames/frame'+str(frameCounter)+'.png')
#     image_list.append('ExperimentFrames/frame'+str(frameCounter)+'.png')
#     frameCounter+=1
#
# for move in range(140):
#     frame = 255*np.ones((h, w, 3), dtype=np.uint8)
#     startY-=5
#     startX+=10
#     drawWindow(frame,startY,startX,(0,0,0),100)
#     img = Image.fromarray(frame, 'RGB')
#     img.save('ExperimentFrames/frame'+str(frameCounter)+'.png')
#     image_list.append('ExperimentFrames/frame'+str(frameCounter)+'.png')
#     frameCounter+=1
#
# for move in range(70):
#     frame = 255*np.ones((h, w, 3), dtype=np.uint8)
#     startY+=10
#     drawWindow(frame,startY,startX,(0,0,0),100)
#     img = Image.fromarray(frame, 'RGB')
#     img.save('ExperimentFrames/frame'+str(frameCounter)+'.png')
#     image_list.append('ExperimentFrames/frame'+str(frameCounter)+'.png')
#     frameCounter+=1
#
# for move in range(140):
#     frame = 255*np.ones((h, w, 3), dtype=np.uint8)
#     startY-=5
#     startX-=10
#     drawWindow(frame,startY,startX,(0,0,0),100)
#     img = Image.fromarray(frame, 'RGB')
#     img.save('ExperimentFrames/frame'+str(frameCounter)+'.png')
#     image_list.append('ExperimentFrames/frame'+str(frameCounter)+'.png')
#     frameCounter+=1
#
# for move in range(70):
#     frame = 255*np.ones((h, w, 3), dtype=np.uint8)
#     startY+=10
#     drawWindow(frame,startY,startX,(0,0,0),100)
#     img = Image.fromarray(frame, 'RGB')
#     img.save('ExperimentFrames/frame'+str(frameCounter)+'.png')
#     image_list.append('ExperimentFrames/frame'+str(frameCounter)+'.png')
#     frameCounter+=1


# for move4 in range(70):
#     frame = 255*np.ones((h, w, 3), dtype=np.uint8)
#     startY-=10
#     drawWindow(frame,startY,startX,(0,0,0),100)
#     img = Image.fromarray(frame, 'RGB')
#     img.save('ExperimentFrames/frame'+str(frameCounter)+'.png')
#     image_list.append('ExperimentFrames/frame'+str(frameCounter)+'.png')
#     frameCounter+=1

my_clip = ImageSequenceClip(image_list, fps=20)
my_clip.write_videofile("calibration.mp4", codec = "mpeg4", audio = False)
