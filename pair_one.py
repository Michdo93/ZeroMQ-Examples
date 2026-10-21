import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:5555")

print("Pair Node 1 started (Bound to port 5555).")

try:
    counter = 0
    while True:
        msg = f"Hello from Node 1 ({counter})"
        socket.send_string(msg)
        print(f"Sent: {msg}")

        try:
            received = socket.recv_string(flags=zmq.NOBLOCK)
            print(f"Received: {received}")
        except zmq.Again:
            pass

        counter += 1
        time.sleep(2)
except KeyboardInterrupt:
    print("\nNode 1 shutting down.")
finally:
    socket.close()
    context.term()