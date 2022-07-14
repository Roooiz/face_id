from mtcnn import MTCNN
import cv2

cap = cv2.VideoCapture(0)
detector = MTCNN()

while True:
    ret, frame = cap.read()
    output = detector.detect_faces(frame)

    for single_output in output:
        x, y, w, h = single_output['box']
        cv2.rectangle(frame, pt1=(x, y), pt2=(x+w, y+h), color=(266, 0, 0), thickness=3)

    cv2.imshow('web', frame)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
