import numpy as np
import cv2
import os
import shutil
import vision_test

def take_video():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_POS_MSEC,60)
    
    cv2.startWindowThread()
    
    FILE_OUTPUT = 'output.mov'
    
    if os.path.isfile(FILE_OUTPUT):
        os.remove(FILE_OUTPUT)
        
    currentFrame = 0
    
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    out = cv2.VideoWriter()
    success = out.open('output.mov',fourcc, 15.0, (1280,720),True)
    
    while(cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()
    
        if ret == True:
            # Handles the mirroring of the current frame
            frame = cv2.flip(frame,1)
    
            # Saves for video
            out.write(frame)
    
            # Display the resulting frame
            cv2.imshow('frame',frame)
            cv2.moveWindow('frame',0,0)
            
        else:
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
        # To stop duplicate images
        currentFrame += 1
    
    # When everything done, release the capture
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    FrameCapture('output.mov')

def FrameCapture(path): 
    shutil.rmtree('shots')
    os.makedirs('shots')
    
    # Path to video file 
    vidObj = cv2.VideoCapture(path) 
  
    # Used as counter variable 
    count = 0
  
    # checks whether frames were extracted 
    success = 1
  
    while success: 
  
        # vidObj object calls read 
        # function extract frames 
        success, image = vidObj.read() 
  
        # Saves the frames with frame-count 
        cv2.imwrite("shots/%d.jpg" % count, image) 
  
        count += 1
    
    vidObj.release()
    cv2.destroyAllWindows()