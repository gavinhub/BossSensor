#! /usr/local/bin/python
# -*- coding:utf-8 -*-

import os
import sys
import datetime

import cv2

from boss_train import Model

DATA_FILE_PATH = './data'


def capture(image, label):
    sub_dir = os.path.join(DATA_FILE_PATH, label)
    if not os.path.exists(sub_dir):
        os.mkdir(sub_dir)
    filename = datetime.date.strftime(datetime.datetime.now(), "%Y_%m_%d_%H_%M_%S") + "_" + label + '.png'
    filepath = os.path.join(sub_dir, filename)
    cv2.imwrite(filepath, image)


def process(image, model):
    result = model.predict(image)
    if result == 0:  # boss
        print('nothing')
    else:
        print('Kissing!')


if __name__ == '__main__':
    # load model
    if len(sys.argv) <= 1:
        model = Model()
        model.load()

    cap = cv2.VideoCapture(0)
    cascade_path = "/usr/local/opt/opencv/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml"
    cascade = cv2.CascadeClassifier(cascade_path)

    while cap.isOpened():
        _, frame = cap.read()
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_rect = cascade.detectMultiScale(frame_gray, scaleFactor=1.2, minNeighbors=3, minSize=(10, 10))
        if len(face_rect) > 0:
            # print('face detected')
            color = (255, 255, 255)  # 白
            for rect in face_rect:
                width, height = rect[2:4]
                if width < 150 or height < 150:
                    continue
                x, y = rect[0:2]
                cv2.rectangle(frame, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), color, thickness=2)
                image = frame[y - 10: y + height, x: x + width]

                if len(sys.argv) > 1:
                    label = sys.argv[1]
                    capture(image, label)
                else:
                    process(image, model)
                    pass

        # don't show if you don't need it.
        cv2.imshow('Gesture', frame)
        k = cv2.waitKey(50)
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
