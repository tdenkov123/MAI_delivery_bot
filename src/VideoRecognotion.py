import cv2
import numpy as np

class VideoRecognition():
    def Vid2Lines(i = 0) -> None:
        cap = cv2.VideoCapture(i)
        if not cap.isOpened():
            print("Failed to open video capture")
            return -1
        
        while True:
            ret, frame = cap.read()
            if ret:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                ret,thresh_img = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
                contours, _ = cv2.findContours(thresh_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
                
                max=0
                sel_countour=None
                for countour in contours:
                    if countour.shape[0]>max:
                        sel_countour=countour
                        max=countour.shape[0]
                
                arclen = cv2.arcLength(sel_countour, True)
                eps = 0.0005
                epsilon = arclen * eps
                approx = cv2.approxPolyDP(sel_countour, epsilon, True)
                canvas = frame.copy()
                for pt in approx:
                    cv2.circle(canvas, (pt[0][0], pt[0][1]), 7, (0,255,0), -1)
                cv2.drawContours(canvas, [approx], -1, (0,0,255), 2, cv2.LINE_AA)
                img_contours = np.uint8(np.zeros((frame.shape[0],frame.shape[1])))
                cv2.drawContours(img_contours, [approx], -1, (255,255,255), 1)
                cv2.imshow('res', img_contours)
                cv2.imshow('orig', canvas)
            else:
                print("Failed to get an image")
                break
            
            k = cv2.waitKey(60) & 0xff
            if k == 27:
                break

        cv2.destroyAllWindows()
        cap.release()



if __name__ == "__main__":
    VideoRecognition.Vid2Lines()
