import random
import time
import zmq


def main():
    context = zmq.Context()

    # Socket to send tasks to workers
    sender = context.socket(zmq.PUSH)
    sender.bind("tcp://*:5557")

    # Socket to send start signal to sink
    sink = context.socket(zmq.PUSH)
    sink.connect("tcp://localhost:5558")

    print("Press Enter when the workers are ready: ")
    input()
    print("Sending tasks to workers...")

    # Signal start of batch to sink
    sink.send(b"0")

    # Send 10 tasks with random workloads
    total_msec = 0
    for task_nbr in range(1, 11):
        workload = random.randint(100, 500)  # workload in ms
        total_msec += workload
        sender.send_string(str(workload))

    print(f"Total expected execution time: {total_msec} msec")
    time.sleep(1)

    sink.close()
    sender.close()
    context.term()


if __name__ == "__main__":
  main()