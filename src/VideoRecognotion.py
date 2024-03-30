import cv2
import numpy as np
import matplotlib
from matplotlib.pyplot import imshow
from matplotlib import pyplot as plt

class VideoRecognition():
    def getCameraDeviceIndexes() -> list[int]:
        indexes = []
        i = 10
        while i > 0:
            cap = cv2.VideoCapture(i)
            if cap.read()[0]:
                indexes.append(i)
                cap.release()
        return indexes
    

    def LineRecognotion(i) -> None:
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if ret == True:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                blur = cv2.GaussianBlur(gray, (7, 7), 0)
                cann = cv2.Canny(blur, 0, 85, 0)
                cv2.imshow("mask", cann)
            else:   
                print("Failed to get an image")
            k = cv2.waitKey(60) & 0xff
            if k == 27:
                break

        cv2.destroyAllWindows()
        cap.release()



if __name__ == "__main__":
    VideoRecognition.LineRecognotion(0)