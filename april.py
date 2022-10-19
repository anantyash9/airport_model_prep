import cv2
import numpy as np
from pupil_apriltags import Detector
img = cv2.imread('april.jpg',cv2.IMREAD_GRAYSCALE)
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

result =at_detector.detect(img,estimate_tag_pose=True,camera_params=([camera_matrix[0],camera_matrix[4],camera_matrix[6],camera_matrix[7]]),tag_size=5.64)
print(result)