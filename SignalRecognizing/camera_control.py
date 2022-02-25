import cv2
import mediapipe as mp

class CameraControl:

    def __init__(self):
        self.capture = True
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.mp_hands = mp.solutions.hands

    # Método de teste para abrir a câmera já com o reconhecimento de mãos
    def openCamera(self):

        # Instancia a classe de reconhecimento de mãos
        with self.mp_hands.Hands(model_complexity=0, min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:

            # Inicia a captura da camera
            camera = cv2.VideoCapture(0)
            
            while self.capture:
                status, frame = camera.read()

                if not status or cv2.waitKey(1) & 0xff == ord('q'):
                    self.capture = False

                frame.flags.writeable = False
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                results = hands.process(frame)

                # Draw the hand annotations on the image.
                frame.flags.writeable = True
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        self.mp_drawing.draw_landmarks(
                            frame,
                            hand_landmarks,
                            self.mp_hands.HAND_CONNECTIONS,
                            self.mp_drawing_styles.get_default_hand_landmarks_style(),
                            self.mp_drawing_styles.get_default_hand_connections_style())

                # Flip the image horizontally for a selfie-view display.
                cv2.imshow('MediaPipe Hands', cv2.flip(frame, 1))
