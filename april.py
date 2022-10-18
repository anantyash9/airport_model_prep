from pupil_apriltags import Detector
import cv2
at_detector = Detector(
   families="tag41h12",
   nthreads=1,
   quad_decimate=1.0,
   quad_sigma=0.0,
   refine_edges=1,
   decode_sharpening=0.25,
   debug=0
)
img=cv2.imread("april.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(at_detector.detect(gray))