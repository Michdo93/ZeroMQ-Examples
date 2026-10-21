import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

for request in range(1, 6):
    print(f"Sending request {request}...")
    socket.send_string(f"Hello {request}")

    # Wait for the reply
    message = socket.recv_string()
    print(f"Received reply {request}: [{message}]")

socket.close()
context.term()