import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://localhost:5555")

print("Pair Node 2 started (Connected to port 5555).")

try:
    counter = 0
    while True:
        try:
            received = socket.recv_string(flags=zmq.NOBLOCK)
            print(f"Received: {received}")
        except zmq.Again:
            pass

        msg = f"Hello from Node 2 ({counter})"
        socket.send_string(msg)
        print(f"Sent: {msg}")

        counter += 1
        time.sleep(2)
except KeyboardInterrupt:
    print("\nNode 2 shutting down.")
finally:
    socket.close()
    context.term()