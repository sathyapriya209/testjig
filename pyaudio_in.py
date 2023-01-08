import pyaudio
import wave
import threading

def DoAudioTest():
    global Logtext
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    CHUNK = 1024
    RATE = 44100
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "output.wav"
    WAVE_INPUT_FILENAME = "input.wav"
    global data
    global rf
    global Breakloop
    global frames1
    data = []
    frames1 = []
    audio = pyaudio.PyAudio()
    print(audio.get_default_input_device_info())
    print(audio.get_default_output_device_info())
    rf = wave.open(WAVE_INPUT_FILENAME, 'rb')
    Breakloop = 0;
    stream = audio.open(format              = rf.getsampwidth(),
                        channels            = rf.getnchannels(),
                        rate                = rf.getframerate(),
                        input               = True,
                        output              = True,
                        input_device_index  = 6,
                        output_device_index = 6,
                        frames_per_buffer   = CHUNK)
    print("Stream audio opened")
    def recording():
        global data
        global Breakloop
        global rf
        global frames1
        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(rf.getnchannels())
        wf.setsampwidth(rf.getsampwidth())
        wf.setframerate(rf.getframerate())
        print("In Recording")
        while True:
            data = stream.read(CHUNK, exception_on_overflow=True)
            frames1.append(data)
            if Breakloop == 1:
                break;
        wf.writeframes(b''.join(frames1))
        wf.close()
        print("Recording done")

    data1 = rf.readframes(CHUNK)
    threading.Thread(target=recording).start()
    while len(data1):
        stream.write(data1)
        data1 = rf.readframes(CHUNK)
        print("In writing Stream")
    Breakloop = 1;

    stream.stop_stream()
    stream.close()
    audio.terminate()
    
DoAudioTest()