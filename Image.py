import cv2
cap = cv2.VideoCapture(0)
print("To save picture click on 'S' key")
while True:
    ret, frame = cap.read()
    cv2.imshow("Webcam", frame)  
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        File = "C:/Users/Lenovo/Desktop/python programs jetson nano/captured_image.jpg"
        cv2.imwrite(f"{File}", frame)
        print("Image captured Succuess fully...") 
        print(f"Image is saved in the folder {File}")
        break
cap.release()  
cv2.destroyAllWindows()
