import tensorflow.keras
import numpy as np
import cv2


class TeachableMachineCamera:
    def __init__(self, modelUrl, classes=[], textView=True):
        self.model = tensorflow.keras.models.load_model(modelUrl)
        self.cap = cv2.VideoCapture(0)
        self.classes = classes
        self.textView=textView

    def isOpened(self):
        return self.cap.isOpened()

    # idx를 리턴 -> idx == -1이면 ret가 없는걸로 처리해주어
    def process(self):
        ret, img = self.cap.read()
        if not ret:
            return -1

        img = img[:, 200:200 + img.shape[0]]
        img = cv2.flip(img, 1)
        img_input = cv2.resize(img, (224, 224))
        img_input = cv2.cvtColor(img_input, cv2.COLOR_BGR2RGB)
        img_input = (img_input.astype(np.float32) / 127.0) - 1
        img_input = np.expand_dims(img_input, axis=0)
        prediction = self.model.predict(img_input)

        idx = np.argmax(prediction)

        if self.textView:
            cv2.putText(img, text=self.classes[idx] if len(self.classes)>idx else "None", org=(10, 30), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=1.0, color=(255, 0, 255), thickness=2)

        cv2.imshow('result', img)
        return idx

    @staticmethod
    def isExit(key='q'):
        return cv2.waitKey(3) == ord(key)

    def destroyCamera(self):
        self.cap.release()
        cv2.destroyAllWindows()

