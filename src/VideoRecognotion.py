import cv2
from cv2 import drawContours

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
    

    def LineRecognotion(i = 0) -> None:
        cap = cv2.VideoCapture(i)   
        while True:
            ret, frame = cap.read()
            if ret == True:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                blurred = cv2.GaussianBlur(gray, (5, 5), 0)
                def showCanny():
                    cann = cv2.Canny(blurred, 50, 85, 0)
                    cv2.imshow("mask", cann)
                def showContours():
                    threshholded = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY)[1]
                    contours, _ = cv2.findContours(threshholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                    cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)
                    cv2.imshow("contours", frame)
                showContours()
                #showCanny()
            else:   
                print("Failed to get an image")
            k = cv2.waitKey(60) & 0xff
            if k == 27:
                break

        cv2.destroyAllWindows()
        cap.release()



if __name__ == "__main__":
    VideoRecognition.LineRecognotion()