import cv2
import numpy as np
# Contours Function
def getContours(img):
    contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 500:
            cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
            peri = cv2.arcLength(cnt,True)
            print(peri)

            # corner point
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            # print(approx)
            print(len(approx))
            objCor = len(approx)
            # Bounding Box
            x, y, w, h = cv2.boundingRect(approx)
            if objCor ==3 :objectType = "Try"
            # Rectangle check
            elif objCor == 4:
                aspRatio = w/float(h)
                # Square Check
                if aspRatio > 0.95 and aspRatio< 1.05: objectType = "Square"
                else : objectType = "Rectangle"
            
            # check square
            elif objCor > 4:
                objectType = "Circle"

            else: objectType="None"
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(110,0,120),3)
            cv2.putText(imgContour,objectType,(x+(w//2),y+(h//2)),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)




path = "images/shapes.png"
img = cv2.imread(path)
imgContour = img.copy()
imgCanny = cv2.Canny(img,50,50)
getContours(imgCanny)

# imgBlack = np.zeros_like(img)
cv2.imshow("Image", img)

cv2.imshow("image contour",imgContour)
cv2.imshow("Canny Image",imgCanny)
# cv2.imshow("Image Black",imgBlack)

cv2.waitKey(0)
