import cv2

from hand_tracking import HandTracking
from mouse_control import MouseControl

HandTracking = HandTracking()
MouseControl = MouseControl()

if __name__ == '__main__':

    camera = cv2.VideoCapture(0)
            
    while HandTracking.capture:
        status, frame = camera.read()

        if not status or cv2.waitKey(1) & 0xff == ord('q'):
            HandTracking.capture = False

        results = HandTracking.getHands(frame)
        HandTracking.getFingerPosition(frame, results)
        MouseControl.moveMouse(HandTracking.x, HandTracking.y)

        cv2.imshow('MediaPipe Hands', cv2.flip(frame, 1))
