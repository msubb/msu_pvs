# code notes pushed the updating file to a separate script

import pickle
import cv2
import cvzone
import numpy as np
import serial
import time

cap = cv2.VideoCapture(0)

with open('CarParkPos_test', 'rb') as f:
    posList = pickle.load(f)

width, height = 50, 50

N = 0
spaceCounter = 0
emptySpace = 0
localSpace = 0

while True:

    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    success, img = cap.read()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25,
                                         16)  # this is what is being count non zero
    imgMedian = cv2.medianBlur(imgThreshold, 5)
    kernel = np.ones((3, 3), np.uint8)
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

    for pos in posList:
        cv2.circle(img, (pos[0], pos[1]), 3, (0, 0, 255), 3, cv2.FILLED)
    #     cv2.imshow("lines", img)

    opsp = 0
    N = 0
    spaceCounter = 0
    emptySpace = 0
    takenSpace = 0
    signVar = 0
    # if (len(posList) / 4).is_integer():  # it needs to be 4 to form the polygon
    loops = len(posList)
    while (N != loops):

        pts = np.array(posList[0 + N:3 + N])

        ## (1) Crop the bounding rect
        rect = cv2.boundingRect(pts)
        x, y, w, h = rect
        croped = imgDilate[y:y + h, x:x + w].copy()

        ## (2) make mask
        pts = pts - pts.min(axis=0)

        mask = np.zeros(croped.shape[:2], np.uint8)
        cv2.drawContours(mask, [pts], -1, (255, 255, 255), -1, cv2.LINE_AA)

        ## (3) do bit-op
        dst = cv2.bitwise_and(croped, croped, mask=mask)
        print(N)

        count = cv2.countNonZero(dst)
        print(count)

        if count < 230:
            color = (0, 255, 0)
            thickness = 5
            spaceCounter += 1
            emptySpace += 1
            cv2.polylines(img, [np.array(posList[0 + N:4 + N])], True, (255, 255, 0), 5)
        else:
            color = (0, 0, 255)
            thickness = 2
            spaceCounter += 1
            cv2.polylines(img, [np.array(posList[0 + N:4 + N])], True, (0, 0, 255), 5)

        takenSpace = spaceCounter - emptySpace
        # print("space counter" + str(spaceCounter))
        # print("empty counter" + str(emptySpace))
        # print("full counter" + str(takenSpace))

        cvzone.putTextRect(img, str(count), (x, y), scale=1, thickness=2, offset=0, colorR=color)

        cvzone.putTextRect(img, f'Free: {emptySpace}/{len(posList) / 4}', (100, 50), scale=3, thickness=5,
                           offset=20, colorR=(0, 200, 0))
        N = N + 4

        with open('file.pkl', 'wb') as test:
            pickle.dump(emptySpace, test)

        print("empty space = " + str(emptySpace))

    cv2.imshow("Image", img)
    # cv2.imshow("ImageBlur", imgBlur)
    # cv2.imshow("ImageThres", imgDilate)
    cv2.waitKey(1)  # this needs to be zero to show lines for some reason
