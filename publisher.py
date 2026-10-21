import time
import zmq

# ZeroMQ Kontext erstellen
context = zmq.Context()

# Socket als Publisher definieren
socket = context.socket(zmq.PUB)

# Bindet den Socket an einen Port (hier Port 5555 auf localhost)
socket.bind("tcp://*:5555")

print("Publisher gestartet. Sende Wetterdaten...")

try:
    while True:
        # Themen definieren
        topic1 = "Wetter.Berlin"
        topic2 = "Wetter.Paris"

        # Nachrichten generieren
        message1 = f"{topic1} 18°C, sonnig"
        message2 = f"{topic2} 14°C, regnerisch"

        # Nachrichten senden (Topic und Nachricht getrennt)
        socket.send_string(message1)
        socket.send_string(message2)

        print(f"Gesendet: {message1} | {message2}")
        time.sleep(2)  # Alle 2 Sekunden senden

except KeyboardInterrupt:
    print("\nPublisher wird beendet.")
finally:
    socket.close()
    context.term()