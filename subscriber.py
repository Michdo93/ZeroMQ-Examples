import zmq

# ZeroMQ Kontext erstellen
context = zmq.Context()

# Socket als Subscriber definieren
socket = context.socket(zmq.SUB)

# Verbinden zum Publisher
socket.connect("tcp://localhost:5555")

# WICHTIG: Ein Subscriber muss definieren, welche Themen ihn interessieren!
# Wenn du alles empfangen möchtest, nimm: socket.setsockopt_string(zmq.SUBSCRIBE, "")
socket.setsockopt_string(zmq.SUBSCRIBE, "Wetter.Berlin")

print("Subscriber laeuft und wartet auf 'Wetter.Berlin'...")

try:
    while True:
        # Nachricht empfangen
        message = socket.recv_string()
        print(f"Empfangen: {message}")

except KeyboardInterrupt:
    print("\nSubscriber wird beendet.")
finally:
    socket.close()
    context.term()