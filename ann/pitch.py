
import numpy as np
import pyaudio

CHUNK = 2**11
RATE = 44100 

p=pyaudio.PyAudio()
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK)

for i in range(int(1000*44100/1024)): #open stream time
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    peak=np.average(np.abs(data))*2
    bars="#"*int(50*peak/2**16)
    print("%04d %05d %s"%(i,peak,bars))

    #TBD NOTE DETECTION 

stream.stop_stream()
stream.close()
p.terminate()