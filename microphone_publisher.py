import sounddevice as sd
import zmq

# ZeroMQ Setup
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")

# Audio-Konfiguration
SAMPLERATE = 16000  # 16 kHz (ausreichend für Sprache)
CHANNELS = 1  # Mono
BLOCKSIZE = 1024  # Anzahl der Frames pro Paket


def audio_callback(indata, frames, time, status):
  """Diese Funktion wird automatisch aufgerufen, sobald neue Audiodaten

  vom Mikrofon bereitstehen.
  """
  if status:
    print(status)

  # Das NumPy-Array in Bytes umwandeln
  audio_bytes = indata.tobytes()

  # Topic und Audiodaten als Multipart-Nachricht senden
  socket.send_multipart([b"mic.stream", audio_bytes])


# Starte den Mikrofon-Stream
print("Mikrofon-Publisher gestartet. Sende Audio... (Strg+C zum Beenden)")

try:
  with sd.InputStream(
      samplerate=SAMPLERATE,
      channels=CHANNELS,
      blocksize=BLOCKSIZE,
      callback=audio_callback,
  ):
    # Die Schleife hält das Programm am Laufen, während der Callback im Hintergrund arbeitet
    while True:
      sd.sleep(1000)

except KeyboardInterrupt:
  print("\nPublisher wird beendet.")
finally:
  socket.close()
  context.term()