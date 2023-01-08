import time
import pexpect
import subprocess

gPC_PlayPauseNoOfTimes = int(5)

MicTestAnalyze = pexpect.spawn("java -jar Connection1.0.2.jar", encoding='utf-8',echo=False)
                               
while True:
                               
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
            elif (line.find('java.net.ConnectException') != -1) :
                TerminateLoop = True
                break
            elif (line.find('No Device Found') != -1) :
                TerminateLoop = True
                break
            elif (line.find('element could not be located') != -1) :
                TerminateLoop = True
                break
            elif (line.find('Unable to create a new remote session') != -1) :
                TerminateLoop = True
                break
            elif (line.find('Build info') != -1) :
                TerminateLoop = True
                break                    
            elif (line.find('Device Connected Succesfully') != -1) :
                print("hello")
                if gPC_PlayPauseNoOfTimes != 0 :
                   time.sleep(10)
                print('Play Testing is going to be started')
                
                for i in range(gPC_PlayPauseNoOfTimes):
                    Cmds = 'adb -s ' + "RZ8M43FFMJV" + ' logcat -c'
                    proc1 = subprocess.Popen(Cmds,stdout=subprocess.PIPE, shell = True)
                    time.sleep(5)
                    proc1.kill()
                    proc1.wait()
                    for line in out :
                            print(line)
                            if (line.find('Enter a number') != -1) :
                               MicTestAnalyze.send("0"+ "\n")            
                            elif (line.find('Enter a number') != -1) :            
                               MicTestAnalyze.send("1" + "\n")
                    