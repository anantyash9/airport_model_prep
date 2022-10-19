# import the opencv library
import cv2
from cv2 import multiply
import numpy as np
from pupil_apriltags import Detector
# img = cv2.imread('april.jpg',cv2.IMREAD_GRAYSCALE)
at_detector = Detector(
   families="tagStandard41h12",
   nthreads=1,
   quad_decimate=1.0,
   quad_sigma=0.0,
   refine_edges=1,
   decode_sharpening=0.25,
   debug=0

)

data = np.load('mat.npz')
camera_matrix=data["mtx"].flatten()
print(camera_matrix)
# define a video capture object
vid = cv2.VideoCapture(4)
vid.set(3, 1920)
vid.set(4, 1080)
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    img=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    result =at_detector.detect(img,estimate_tag_pose=True,camera_params=([camera_matrix[0],camera_matrix[4],camera_matrix[6],camera_matrix[7]]),tag_size=5.64)
    
    if len(result)>1:
        for x in result:
            if x.tag_id==1:
                landmark_t=x.pose_t
                landmark_r=x.pose_R
            if x.tag_id==0:
                plane_r=x.pose_R
                plane_t=x.pose_t
        # print(landmark_r,landmark_t)
        M = np.vstack((np.hstack((landmark_r, -landmark_t)), [0, 0, 0 ,1]))
        new_point=np.matmul(M,np.append(plane_t,[1]))
        n=np.array([[0],[0],[0]])
        print(n)
        val=np.cross(landmark_t,landmark_r)-landmark_t
        # new_point=cv2.perspectiveTransform(plane_t,M)
        print(val)
        print(landmark_t)
    # Display the resulting frame
    cv2.imshow('frame', frame)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()