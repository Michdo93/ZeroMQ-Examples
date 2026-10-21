import numpy as np
import sounddevice as sd
import zmq

# ZeroMQ Setup
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")
socket.setsockopt_string(zmq.SUBSCRIBE, "mic.stream")

# Gleiche Audio-Konfiguration wie beim Publisher!
SAMPLERATE = 16000
CHANNELS = 1
BLOCKSIZE = 1024

print("Mikrofon-Subscriber laeuft und gibt Ton aus... (Strg+C zum Beenden)")

try:
  # Starte den Audio-Ausgabe-Stream
  with sd.OutputStream(
      samplerate=SAMPLERATE, channels=CHANNELS, dtype="float32"
  ) as stream:
    while True:
      # Empfange Topic und Audio-Bytes
      topic, audio_bytes = socket.recv_multipart()

      # Bytes zurück in ein NumPy-Array konvertieren
      np_arr = np.frombuffer(audio_bytes, dtype=np.float32)

      # In die richtige Form bringen (Blockgröße x Kanäle)
      audio_chunk = np_arr.reshape(-1, CHANNELS)

      # Audio direkt an die Lautsprecher übergeben
      stream.write(audio_chunk)

except KeyboardInterrupt:
  print("\nSubscriber wird beendet.")
finally:
  socket.close()
  context.term()