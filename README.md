# ZeroMQ-Examples 🚀

This repository contains practical examples of using **ZeroMQ (ØMQ)** in Python. The focus is on the **Publish/Subscribe (Pub/Sub)** pattern, which allows real-time data streaming (such as text messages, live webcam frames, or microphone audio) from a single publisher to one or multiple subscribers.

## ⚙️ Installation & Prerequisites

Before running the examples, you need to install Python, the core ZeroMQ library, and the required Python packages.

### 1. Basic ZeroMQ Installation

Depending on your operating system, install the core ZeroMQ C-library and the official Python bindings (`pyzmq`):

* **Windows:**
  On Windows, installing the Python package is usually sufficient, as pre-compiled binaries for `libzmq` are included automatically:

  ```
  pip install pyzmq
  ```

* **Linux (Ubuntu / Debian):**
  Install the C-library using your package manager first, followed by the Python binding:

  ```
  sudo apt-get update
  sudo apt-get install libzmq3-dev
  pip install pyzmq
  ```

### 2. Additional Libraries for Media Streaming

For the webcam and microphone streaming examples, install the following additional packages:

```
# For webcam video streaming (OpenCV)
pip install opencv-python

# For microphone audio streaming (Sounddevice & NumPy)
pip install sounddevice numpy
```

## 📂 Project Structure

The repository is structured as follows:

* `publisher.py` & `subscriber.py` – Simple text messaging example (weather updates).

* `webcam_publisher.py` & `webcam_subscriber.py` – Live webcam video streaming.

* `microphone_publisher.py` & `microphone_subscriber.py` – Real-time microphone audio streaming.

## 🚀 Examples & Execution

To test each example, open **two separate terminal windows** (one for the publisher, one for the subscriber).

### 1. Basic Text Messaging (Pub / Sub)

A classic example where weather data is broadcasted with specific topic headers (`Wetter.Berlin`) and filtered on the receiving end.

* **Start the Publisher:**

  ```
  python publisher.py
  ```

* **Start the Subscriber:**

  ```
  python subscriber.py
  ```

### 2. Live Webcam Video Stream

Captures frames from a local webcam, encodes them as JPEG images, transmits them over ZeroMQ, and displays the stream in an OpenCV window.

* **Start the Publisher (captures video feed):**

  ```
  python webcam_publisher.py
  ```

* **Start the Subscriber (displays video feed):**

  ```
  python webcam_subscriber.py
  ```

  *Tip: Click on the active video window and press **`q`** to close it.*

### 3. Microphone Audio Stream

Captures audio input from your primary microphone in chunks and broadcasts them to be played back in real-time by the subscriber.

> ⚠️ **Important Notice (Audio Feedback):** If you run both the publisher and subscriber on the same computer, please wear **headphones** to prevent loud audio feedback loops!

* **Start the Publisher (captures audio):**

  ```
  python microphone_publisher.py
  ```

* **Start the Subscriber (plays audio through speakers/headphones):**

  ```
  python microphone_subscriber.py
  ```

## 🌐 Network Configuration (Multi-Device Setup)

By default, all scripts are configured for local testing using `localhost` (`tcp://localhost:5555` / `tcp://*:5555`).

To run the publisher and subscriber on **two different devices within the same local network**:

1. Open the subscriber script and replace `localhost` with the local IP address of the publisher machine (e.g., `tcp://192.168.1.50:5555`).

2. Ensure that the target port (e.g., `5555`) is allowed through the publisher machine's firewall.