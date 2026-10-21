import cv2
import zmq

# ZeroMQ Kontext und Publisher-Socket einrichten
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")

# Webcam öffnen (0 ist standardmäßig die integrierte/erste Kamera)
cap = cv2.VideoCapture(0)

print("Webcam-Publisher gestartet. Drücke Ctrl+C zum Beenden.")

try:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Fehler beim Abrufen des Kamerabildes.")
            break

        # Optional: Bildgröße anpassen, um Datenmenge im Netzwerk zu reduzieren
        frame = cv2.resize(frame, (640, 480))

        # Das Frame als JPEG komprimieren (Qualität 80 von 100)
        success, encoded_image = cv2.imencode(
            ".jpg", frame, [int(cv2.IMWRITE_JPEG_QUALITY), 80]
        )
        if not success:
            continue

        # Als Bytes konvertieren
        image_bytes = encoded_image.tobytes()

        # Topic und Bilddaten als Multipart-Nachricht senden
        # ZeroMQ erlaubt mehrere Teile: Teil 1 = Topic, Teil 2 = Daten
        socket.send_multipart([b"webcam.stream", image_bytes])

        # Kleine Pause, um die Framerate zu steuern (ca. 30 FPS)
        cv2.waitKey(30)

except KeyboardInterrupt:
    print("\nPublisher wird beendet.")
finally:
    cap.release()
    socket.close()
    context.term()