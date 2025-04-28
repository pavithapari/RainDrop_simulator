import cv2
import mediapipe as mp
slicing_positions = []  
cam_w,cam_h=0,0

def detect_slices():
    global slicing_positions
    global cam_w,cam_h
    cap = cv2.VideoCapture(0)
    cam_w,cam_h=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(cam_w,cam_h)
    if not cap.isOpened():
        print("Error")
    mpHands = mp.solutions.hands
    hands = mpHands.Hands()

    while True:
        success, img = cap.read()
        if not success:
            continue

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x * cam_w), int(lm.y *cam_h)
                    if id ==8:
                        slicing_positions.append((cx, cy))
        cv2.imshow("Hand Tracking", img)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        

    cap.release()
    cv2.destroyAllWindows()
