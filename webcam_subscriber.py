import cv2
import numpy as np
import zmq

# ZeroMQ Kontext und Subscriber-Socket einrichten
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")

# Topic abonnieren
socket.setsockopt_string(zmq.SUBSCRIBE, "webcam.stream")

print(
    "Webcam-Subscriber läuft. Drücke die Taste 'q' im Videofenster zum"
    " Beenden."
)

try:
    while True:
        # Multipart-Nachricht empfangen ([Topic, Bild-Bytes])
        topic, image_bytes = socket.recv_multipart()

        # Bytes in ein NumPy-Array konvertieren
        np_arr = np.frombuffer(image_bytes, np.uint8)

        # NumPy-Array zurück in ein OpenCV-Bild dekodieren
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        if frame is not None:
            # Bild in einem Fenster anzeigen
            cv2.imshow("ZeroMQ Webcam Stream", frame)

        # Warten auf Tastendruck; wenn 'q' gedrückt wird, Schleife abbrechen
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

except KeyboardInterrupt:
    print("\nSubscriber wird beendet.")
finally:
    cv2.destroyAllWindows()
    socket.close()
    context.term()