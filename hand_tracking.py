import cv2
import mediapipe as mp

class HandTracking:

    def __init__(self):
        self.capture = True
        self.noiseRange = 5

        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.mp_hands = mp.solutions.hands

        self.hands = self.mp_hands.Hands(model_complexity=0, min_detection_confidence=0.5, min_tracking_confidence=0.5)

        self.x, self.y = 0, 0
        self.position = [self.x, self.y]

        self.trajectory = [[0,0]]

    def getHands(self, frame):

        # conversão de cores do padrão BGR do opencv para RGB do mediapipe
        frame.flags.writeable = False
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Resultado do reconhecimento de mãos
        results = self.hands.process(frame)

        return results
    
    def getFingerPosition(self, frame, results):

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:

                self.mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    self.mp_hands.HAND_CONNECTIONS)

                for id, lm in enumerate(hand_landmarks.landmark):

                    if id == 8:
                        h, w, c = frame.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)

                        if cx != self.x or cy != self.y:
                            self.x, self.y = cx, cy



