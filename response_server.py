import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

print("Response Server is running...")

try:
    while True:
        # Wait for next request from client
        message = socket.recv_string()
        print(f"Received request: [{message}]")

        # Simulate some processing work
        time.sleep(1)

        # Send reply back

        response = f"World (Processed: {message})"
        socket.send_string(response)

except KeyboardInterrupt:
    print("\nServer shutting down.")
finally:
    socket.close()
    context.term()