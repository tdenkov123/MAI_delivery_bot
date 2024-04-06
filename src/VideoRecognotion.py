import cv2
import Application

class VideoRecognition(Application):
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
                blur = cv2.GaussianBlur(gray, (7, 7), 0)
                cann = cv2.Canny(blur, 50, 85, 0)
                cv2.imshow("mask", cann)
            else:   
                print("Failed to get an image")
            k = cv2.waitKey(60) & 0xff
            if k == 27:
                break

        cv2.destroyAllWindows()
        cap.release()



if __name__ == "__main__":
    VideoRecognition.LineRecognotion()