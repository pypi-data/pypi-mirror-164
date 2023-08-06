import cv2
import mediapipe as mp
import numpy as np
import os

class SelfieSegmentation():
    def __init__(self, BG_COLOR=(255, 255, 255), MASK_COLOR=(0, 0, 0)):
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_selfie_segmentation = mp.solutions.selfie_segmentation
        self.BG_COLOR = BG_COLOR
        self.MASK_COLOR = MASK_COLOR

    def staticSegmentation(self, path, saveto, saveMask=0, backgroundimage=0):
        with self.mp_selfie_segmentation.SelfieSegmentation(
                model_selection=0) as selfie_segmentation:
            listImg = os.listdir(path)
            i = 10
            for imgPath in listImg:
                image = cv2.imread(f'{path}/{imgPath}')
                image_height, image_width, _ = image.shape
                results = selfie_segmentation.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
                condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.1
                fg_image = np.zeros(image.shape, dtype=np.uint8)
                fg_image[:] = self.MASK_COLOR
                if backgroundimage == 0:
                    bg_image = np.zeros(image.shape, dtype=np.uint8)
                    bg_image[:] = self.BG_COLOR
                else:
                    img = cv2.imread(backgroundimage)
                    bg_image = img
                output_image = np.where(condition, fg_image, bg_image)
                abspath = saveto + str(i) + '.png'
                cv2.imwrite(abspath, output_image)
                if saveMask:
                    abspath = saveto + 'mask' + str(i) + '.png'
                    cv2.imwrite(abspath, output_image)
                i += 1

    def videoSegmentation(self, cam=0, threshold=0.5, backgroundimage=0):
        cap = cv2.VideoCapture(cam)
        with self.mp_selfie_segmentation.SelfieSegmentation(
                model_selection=1) as selfie_segmentation:
            bg_image = None
            while cap.isOpened():
                success, image = cap.read()
                if not success:
                    print("Ignoring empty camera frame.")
                    continue
                image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
                image.flags.writeable = False
                results = selfie_segmentation.process(image)
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                condition = np.stack(
                    (results.segmentation_mask,) * 3, axis=-1) > threshold
                if backgroundimage != 0:
                    img = cv2.imread(backgroundimage)
                    bg_image = img
                else:
                    if bg_image is None:
                        bg_image = np.zeros(image.shape, dtype=np.uint8)
                        bg_image[:] = self.BG_COLOR
                output_image = np.where(condition, image, bg_image)

                cv2.imshow('MediaPipe Selfie Segmentation', output_image)
                if cv2.waitKey(5) == ord('q'):
                    break
        cap.release()
