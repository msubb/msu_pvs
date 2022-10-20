import cv2
import pickle
import numpy as np

width, height = 50, 50
render = 0
rbState = True

try:
    with open('CarParkPos_test', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []

def mouseClick(events, x, y, flags, params):

    if events == cv2.EVENT_MOUSEMOVE:
        for pos in posList:
            cv2.circle(img, (pos[0], pos[1]), 3, (0, 0, 255), 3, cv2.FILLED)
            cv2.imshow('Image', img)
        if (len(posList) / 4).is_integer():
            loops = len(posList)
            N = 0
            while (N != loops):
                cv2.polylines(img, [np.array(posList[0+N:4+N])], True, (255, 255, 0), 5)
                N = N + 4
            cv2.imshow('Image', img)

    if events == cv2.EVENT_LBUTTONDOWN:
        global loopNum
        cv2.circle(img, (x, y), 3, (0, 0, 255), 3, cv2.FILLED)
        posList.append((x, y))
        if (len(posList)/4).is_integer():
            cv2.polylines(img, [np.array(posList[-4:])], True, (255,255,0), 5)
            print(posList[-4:])
            print(len(posList)/4)
        cv2.imshow('Image', img)

    if events == cv2.EVENT_RBUTTONDOWN:
        posList.pop()
        print(len(posList) / 4)
        cv2.destroyWindow("Image")

    with open('CarParkPos_test', 'wb') as f:
        pickle.dump(posList, f)

while True:
    img = cv2.imread('carParkImg.png')
    # print(posList)
    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mouseClick)
    key = cv2.waitKey(0)