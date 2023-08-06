# Selfie Segmentation
This library is used for selfie segmentation of static and live webcam feed. You ca add images or a constant backgroundd colour over your image/live feed
It is usefull for projects like: Face recognition, Facial expression recognition and others, where an accurate segmentation will enhance the feed to the neural network therefore increasing the accuracy of the model

**::Test code::**
```
from selfiesegmentation.Segmentation import SelfieSegmentation
ss = SelfieSegmentation( BG_COLOR=(255, 255, 255), MASK_COLOR=(0, 0, 0))
ss.staticSegmentation(path, saveto, saveMask=0, backgroundimage=0)
# If backgroundimage = 'path of the image' The segmentation will 
# have a image instead of plain background colour
videoSegmentation(self, cam=0, threshold=0.5, backgroundimage=0)

```
