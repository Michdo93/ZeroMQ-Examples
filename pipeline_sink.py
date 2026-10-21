import time
from opentelemetry import context
import zmq

def main():
    context = zmq.Context()

    # Socket to receive results from workers
    receiver = context.socket(zmq.PULL)
    receiver.bind("tcp://*:5558")

    # Wait for start of batch
    s = receiver.recv()
    print("Batch started, collecting results...")
    
    start_time = time.time()

    # Collect results from 10 tasks
    for task_nbr in range(10):
        s = receiver.recv()
        print(".", end="", flush=True)

        end_time = time.time()
        total_time = (end_time - start_time) * 1000
        print(f"\nTotal elapsed time: {total_time:.2f} msec")

    receiver.close()
    context.term()


if __name__ == "__main__":
  main()