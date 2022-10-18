# import the opencv library
import cv2
import numpy as np
data = np.load('mat.npz')
print(data["mtx"].flatten())
# define a video capture object
vid = cv2.VideoCapture(1)
vid.set(3, 1920)
vid.set(4, 1080)
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    h,  w = frame.shape[:2]
    newcameramtx, roi = cv2.getOptimalNewCameraMatrix(data["mtx"], data["dist"], (w,h), 1, (w,h))
    dst = cv2.undistort(frame, data["mtx"], data["dist"], None, newcameramtx)
    x, y, w, h = roi
    dst = dst[y:y+h, x:x+w]
  
    # Display the resulting frame
    cv2.imshow('frame', dst)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()