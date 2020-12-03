import cv2

# print('hello,world')
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# img = cv2.imread('pic/destop.jpg')
while True:
    success, img = cap.read()
    cv2.imshow("Live", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
