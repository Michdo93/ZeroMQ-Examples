# ZeroMQ-Examples 🚀

This repository contains various examples demonstrating different messaging patterns using **ZeroMQ (ØMQ)** in Python. It covers Publish/Subscribe, Request-Reply, Task Pipelines, and Peer-to-Peer communication.

---

## ⚙️ Installation & Prerequisites

Before running the examples, make sure you have Python, the ZeroMQ C library, and the required Python packages installed.

### 1. Basic ZeroMQ Installation

Depending on your operating system:

*   **Windows:**
    Usually, installing the Python package is sufficient since precompiled binaries are bundled:
    ```bash
    pip install pyzmq
    ```
*   **Linux (Ubuntu / Debian):**
    Install the underlying C library first, followed by the Python binding:
    ```bash
    sudo apt-get update
    sudo apt-get install libzmq3-dev
    pip install pyzmq
    ```

### 2. Additional Libraries for Media Examples

For the webcam and microphone scripts, extra libraries are needed:

```bash
# For webcam streaming (OpenCV)
pip install opencv-python

# For microphone audio streaming (Sounddevice & NumPy)
pip install sounddevice numpy
```

---

## 📂 Project Structure

* `publisher.py` & `subscriber.py` – Simple text messaging (Pub/Sub pattern).
* `webcam_publisher.py` & `webcam_subscriber.py` – Live webcam video streaming.
* `microphone_publisher.py` & `microphone_subscriber.py` – Real-time microphone audio streaming.
* `request_client.py` & `response_server.py` – Synchronous Request-Reply (Req/Rep pattern).
* `pipeline_push.py`, `pipeline_pull.py`, `pipeline_sink.py` – Parallel task distribution (Push/Pull pattern).
* `pair_one.py` & `pair_two.py` – Exclusive bidirectional communication (Pair pattern).

---

## 🚀 Examples & Execution Guide

### 1. Simple Text Messaging (Pub / Sub)

* **Start Publisher:** `python publisher.py`
* **Start Subscriber:** `python subscriber.py`

### 2. Webcam Video Stream

* **Start Publisher:** `python webcam_publisher.py`
* **Start Subscriber:** `python webcam_subscriber.py` *(Press `q` inside the video window to exit)*

### 3. Microphone Audio Stream

> ⚠️ **Warning:** Wear headphones if running both on the same machine to avoid acoustic feedback!

* **Start Publisher:** `python microphone_publisher.py`
* **Start Subscriber:** `python microphone_subscriber.py`

### 4. Request-Reply (Req / Rep)

Synchronous client-server communication where a client sends a request and must wait for a reply.

* **Start Server:** `python response_server.py`
* **Start Client:** `python request_client.py`

### 5. Task Pipeline (Push / Pull)

Distributes workloads from a ventilator across multiple workers, aggregating results at a sink.

1. Start the **Sink**: `python pipeline_sink.py`
2. Start one or more **Workers**: `python pipeline_pull.py`
3. Start the **Ventilator**: `python pipeline_push.py` *(Press Enter in the ventilator terminal to dispatch tasks)*

### 6. Exclusive Pair (Pair-to-Pair)

Direct 1-to-1 bidirectional communication between two independent nodes.

* **Start Node 1:** `python pair_one.py`
* **Start Node 2:** `python pair_two.py`