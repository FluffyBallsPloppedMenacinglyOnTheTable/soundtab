import pyaudio
import numpy as np

CHUNK = 2**11
RATE = 44100

notes = dict({
    55:"(LOW)",
    65.41:"C2",
    69.3:"C#2",
    73.42:"D2",
    77.78:"D#2",
    82.41:"E2",
    87.31:"F2",
    92.5:"F#2",
    98:"G2",
    103.83:"G#2",
    110:"A2",
    116.54:"A#2",
    123.47:"B2",
    130.81:"C3",
    138.59:"C#3",
    146.83:"D3",
    155.56:"D#3",
    164.81:"E3",
    174.61:"F3",
    185:"F#3",
    196:"G3",
    207.65:"G#3",
    220:"A3",
    233.08:"A#3",
    246.94:"B3",
    261.63:"C4",
    277.18:"C#4",
    293.66:"D4",
    311.13:"D#4",
    329.63:"E4",
    349.23:"F4",
    369.99:"F#4",
    392:"G4",
    415.3:"G#4",
    440:"A4",
    466.16:"A#4",
    493.88:"B4",
    523.25:"C5",
    554.37:"C#5",
    587.33:"D5",
    622.25:"D#5",
    659.26:"E5",
    698.46:"F5",
    739.99:"F#5",
    783.99:"G5",
    830.61:"G#5",
    880:"A5",
    932.33:"A#5",
    987.77:"B5",
    1046.5:"C6",
    1108.7:"C#6",
    1174.7:"D6",
    1244.5:"D#6",
    1318.5:"E6",
    1400:"(HIGH)"
})

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