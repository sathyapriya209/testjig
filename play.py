import time
import pexpect
import subprocess
gPC_PlayPauseNoOfTimes = int(0)
if gPC_PlayPauseNoOfTimes == 0 :
       TerminateLoop = False
MicTestAnalyze = pexpect.spawn("java -jar Connection1.0.2.jar", encoding='utf-8',echo=False)
while 1:
                MicTestAnalyze.expect(["\r\n", pexpect.EOF],timeout = 120)
                out = MicTestAnalyze.before.split("\r\n")
                for line in out :
                    print(line)
                    if (line.find('Device Version') != -1) :
                        MicTestAnalyze.send("11" + "\n")            
                    elif (line.find('Device Model Name') != -1) :           
                        MicTestAnalyze.send("samsung" + "\n")
                    elif (line.find('your Connected Device') != -1) :
                        MicTestAnalyze.send("RZ8M43FFMJV" + "\n")            
                    elif (line.find('Enter Device Name') != -1) :
                        MicTestAnalyze.send("44:90"+ "\n")
                    elif (line.find('Device name from the list') != -1) :            
                        MicTestAnalyze.send("Rockerz 330 Pro_4490" + "\n")                     
                    elif (line.find('No Device Found') != -1) :
                        TerminateLoop = True
                        break
                    elif (line.find('Device Connected Succesfully') != -1) :
                        print("hello")
                    for line in out :
                            print(line)
                            if (line.find('Enter a number') != -1) :
                               MicTestAnalyze.send("0"+ "\n")            
                            elif (line.find('Enter a number') != -1) :            
                               MicTestAnalyze.send("1" + "\n")     