import subprocess
from subprocess import PIPE, Popen
import threading

def record_speaker_output(side):
    if side == "RIGHT":
        print("Right selected")
        p_record = subprocess.Popen(['arecord', '-d', '10', 'speaker_output_recording.wav'])
        p_record.communicate()
        print("Recording Ended")
    else:
        print("Left Selected")
    
def play_sound():
    p_play = subprocess.Popen(['aplay', 'input.wav'])
    p_play.communicate()
    print("Play Ended")

t1 = threading.Thread(target = record_speaker_output, args=("RIGHT",))
t2 = threading.Thread(target = play_sound)
t1.start()
t2.start()