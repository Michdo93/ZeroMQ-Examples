import time
import zmq


def main():
    context = zmq.Context()

    # Socket to receive tasks from ventilator
    receiver = context.socket(zmq.PULL)
    receiver.connect("tcp://localhost:5557")

    # Socket to send results to sink
    sender = context.socket(zmq.PUSH)
    sender.connect("tcp://localhost:5558")

    print("Worker started, waiting for tasks...")

    try:
        while True:
            workload = receiver.recv_string()
            workload_ms = int(workload)
            print(f"Processing task (workload: {workload_ms}ms)...")
            time.sleep(workload_ms / 1000.0)

            # Send completion signal to sink
            sender.send(b"Done")
    except KeyboardInterrupt:
        print("\nWorker stopping.")
    finally:
        receiver.close()
        sender.close()
        context.term()


if __name__ == "__main__":
    main()