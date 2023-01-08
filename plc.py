f playcontrol == True :
        print("started")
        CTC_TestInProgress = False
        State = 0
        ActionCount = (gPC_PlayPauseNoOfTimes*2)
        bTest = False
    
        if gPC_PlayPauseNoOfTimes != 0 and gPC_NextPrevNoOfTimes != 0 :
            if gPC_PlayPauseNoOfTimes == 0:
                State = 1
                ActionCount = gPC_NextPrevNoOfTimes        
            
            while 1:                    
                PlayDetected = False
                PauseDetected = False
                NextDetected = False
                PrevDetected = False
            
                #Clear logs 	
                Cmds = 'adb -s ' + MP1_SerialNumber + ' logcat -c'
                proc1 = subprocess.Popen(Cmds,stdout=subprocess.PIPE, shell = True)
                time.sleep(15)
                proc1.kill()
                proc1.wait()
            
                
                if CTC_TestInProgress == True :
                    if State == 0 :
                        print("State 0")
                        if bTest == False :
                            bTest = True
                            CTC_Control(1,1)
                            print("state 0 true")
                        else :
                            CTC_Control(0,1)
                            bTest = False                                   
                    elif State == 1 :
                        CTC_Control(1,1)
                        print("State 1")
                    elif State == 2 :    
                        CTC_Control(0,1)
                        print("State 2")
                    break
                else :
                    while 1:
                        CommandGiven = False
                        MicTestAnalyze.expect(["\r\n", pexpect.EOF],timeout = 120)
                        out = MicTestAnalyze.before.split("\r\n")                    
            
                        for line in out :                        
                            if (line.find('Enter a number') != -1) :
                                print(line)
                                if State == 0 :
                                    if bTest == False :
                                        MicTestAnalyze.send("0"+ "\n")
                                        bTest = True
                                        CommandGiven = True
                                        print("State true")
                                    else :
                                        MicTestAnalyze.send("1"+ "\n")
                                        bTest = False
                                        CommandGiven = True
                                        print("State 0 executed")
                                elif State == 1 :
                                    MicTestAnalyze.send("2"+ "\n")
                                    CommandGiven = True
                                    print("State 1 executed")
                                elif State == 2 :    
                                    MicTestAnalyze.send("3"+ "\n")
                                    CommandGiven = True
                                    print("State 2 executed")
                                break
                        if CommandGiven == True:
                            break
                time.sleep(10)
                    
                if State == 0:
                    Cmds ='adb -s ' +  MP1_SerialNumber + ' logcat  APM_AudioPolicyManager:V *:S -d'                         
                else :
                    Cmds ='adb -s ' +  MP1_SerialNumber + ' logcat FaceWidgetMediaSessionManager:V *:S -d'                    
            
                proc1 = subprocess.Popen(Cmds, stdout=subprocess.PIPE, shell = True)
                for line in proc1.stdout:
                    print(line)
                    if b"startOutput" in line:                            
                        PlayDetected = True                
                        print( " Song Played successfully " )
                        break                                        
                    if b"stopOutput" in line:                            
                        PauseDetected = True                
                        print( " Song Paused successfully " )
                        break 
                    if b"onMetadataChanged()" in line and State == 1:                            
                        NextDetected = True                
                        print( " Next Song Played Sucessfully " )
                        break
                    if b"onMetadataChanged()" in line and State == 2:                            
                        PrevDetected = True                
                        print( " Prev Song Played successfully " )
                        break

                proc1.kill()
                proc1.wait()
            
                if PlayDetected == True :
                    gNumberOfPlayDetected = gNumberOfPlayDetected + 1
                if PauseDetected == True :
                    gNumberOfPauseDetected = gNumberOfPauseDetected + 1
                if NextDetected == True :
                    gNumberOfNextDetected = gNumberOfNextDetected + 1
                if PrevDetected == True :
                    gNumberOfPrevDetected = gNumberOfPrevDetected + 1
                
                ActionCount = ActionCount - 1
                if ActionCount == 0:
                    State = State + 1
                    ActionCount = gPC_NextPrevNoOfTimes
                if State == 3:
                    
                    print(gNumberOfPlayDetected)
                    print(gNumberOfPauseDetected)
                    print(gNumberOfNextDetected)
                    print(gNumberOfPrevDetected)
                    CTC_TestInProgress = False
                    
                    if IsHeadPhoneDevice == True :
                        MicTestAnalyze.send("4"+ "\n")                    
                        break
                    else :
                        State = 0
                        ActionCount = (gPC_PlayPauseNoOfTimes*2)
                        bTest = False                        
                        CTC_TestInProgress = True
                
                if CTC_TestInProgress != True
                    break
           
    if callcontrol == True :

        if gCC_AnsEndNoOfTimes == 0 and gCC_RejectNoOfTimes == 0 :
            app.Log('Mobile phone - Call control Options are not selected')
    #Handle error

        TotalCallTimes = gCC_AnsEndNoOfTimes + gCC_RejectNoOfTimes

        NumberOfAnsCallDetected = int(0)
        NumberOfEndCallDetected = int(0)
        NumberOfRejectCallDetected = int(0)

        if gCC_AnsEndNoOfTimes != 0 :
            time.sleep(10)
            print('Call Testing is going to be started')
            for i in range(gCC_AnsEndNoOfTimes) :
                Cmds = 'adb -s ' + MP2_SerialNumber + ' shell am start -a android.intent.action.CALL -d tel:' + MP1_PhoneNumber  
                proc = subprocess.Popen(Cmds,stdout=subprocess.PIPE, shell = True)

                CallAcceptanceDetected = False
                CallEndDetected = False

                endtime = datetime.datetime.now() + datetime.timedelta(seconds=30)

                time.sleep(20)
                #Call CTC one touch
                if IsHeadPhoneDevice == True :
                    Cmds = 'adb -s ' + MP1_SerialNumber + ' shell input keyevent 5'
                    proc1 = subprocess.Popen(Cmds,stdout=subprocess.PIPE, shell = True)
                    time.sleep(5)
                    proc1.kill()
                    proc1.wait()
                else :
                    CTC_Control(1,1)

                ContinueInCall = False

                while 1:
                    Cmds = 'adb -s ' + MP1_SerialNumber + ' logcat -c'
                    proc1 = subprocess.Popen(Cmds,stdout=subprocess.PIPE, shell = True)
                    time.sleep(5)
                    proc1.kill()
                    proc1.wait()

                    if ContinueInCall == True:
                        if IsHeadPhoneDevice == True :
                            Cmds = 'adb -s ' + MP1_SerialNumber + ' shell input keyevent 6'
                            proc1 = subprocess.Popen(Cmds,stdout=subprocess.PIPE, shell = True)
                            time.sleep(5)
                            proc1.kill()
                            proc1.wait()
                        else :
                            CTC_Control(1,1)

                    Cmds = 'adb -s ' + MP1_SerialNumber + ' logcat  RegiGvnBase:V  CallStateMachine:V *:S -d'
                                #print(Cmds)
                    proc1 = subprocess.Popen(Cmds, stdout=subprocess.PIPE, shell = True)

                    for line in proc1.stdout:
                                #print(line)
                        if b"RegiGvnBase: onCallStatus: event=EVENT_CALL_ESTABLISHED" in line:                            
                            CallAcceptanceDetected = True                
                            print("Incoming Call Answered")
                            break
                
                        if b"CallStateMachine: Enter [EndingCall], errorCode=200" in line:                            
                            CallEndDetected = True
                            print("Call is Ended")
                            break

                    proc1.kill()
                    proc1.wait()                                                        

                    if CallAcceptanceDetected == True:
                        NumberOfAnsCallDetected = NumberOfAnsCallDetected + 1
                        CallAcceptanceDetected = False
                        ContinueInCall = True
                        continue
                                                            
                    if CallEndDetected == True :
                        NumberOfEndCallDetected = NumberOfEndCallDetected + 1
                        CallEndDetected = False
                        time.sleep(10)
                        break   

                    if datetime.datetime.now() >= endtime :
                        time.sleep(30)
                        Cmds = 'adb -s ' + MP1_SerialNumber + ' shell input keyevent 6'
                        proc1 = subprocess.Popen(Cmds,stdout=subprocess.PIPE, shell = True)
                        time.sleep(5)
                        proc1.kill()
                        proc1.wait()
                        break

        if gCC_RejectNoOfTimes != 0 :
            for i in range(gCC_RejectNoOfTimes) :
                Cmds = 'adb -s ' + MP2_SerialNumber + ' shell am start -a android.intent.action.CALL -d tel:' + MP1_PhoneNumber  
                proc = subprocess.Popen(Cmds,stdout=subprocess.PIPE, shell = True)

                CallRejectDetected = False
                CallAutoEndtDetected = False

                endtime = datetime.datetime.now() + datetime.timedelta(seconds=30)

                time.sleep(20)
                        #Call CTC double touch
                if IsHeadPhoneDevice == True :
                    Cmds = 'adb -s ' + MP1_SerialNumber + ' shell input keyevent 6'
                    proc1 = subprocess.Popen(Cmds,stdout=subprocess.PIPE, shell = True)
                    time.sleep(5)
                    proc1.kill()
                    proc1.wait()
                else :
                    CTC_Control(1,0)


                while 1:
                    Cmds = 'adb -s ' + MP1_SerialNumber + ' logcat -c'
                    proc1 = subprocess.Popen(Cmds,stdout=subprocess.PIPE, shell = True)
                    time.sleep(5)
                    proc1.kill()
                    proc1.wait()

                    Cmds = 'adb -s ' + MP1_SerialNumber + ' logcat  RegiGvnBase:V  CallStateMachine:V *:S -d'
                    print(Cmds)
                    proc1 = subprocess.Popen(Cmds, stdout=subprocess.PIPE, shell = True)

                    for line in proc1.stdout:
                                  #  print(line)
                        if b"CallStateMachine: Enter [EndingCall], errorCode=-1" in line:                            
                            CallRejectDetected = True                
                            print("Incoming Call Rejected")
                            break
                            
                        if b"CallStateMachine: Enter [EndingCall], errorCode=210" in line:                            
                            CallAutoEndtDetected = True
                            print("Call is Ended automatically")
                            break

                    proc1.kill()
                    proc1.wait()                    

                if CallRejectDetected == True:
                    time.sleep(10)
                    NumberOfRejectCallDetected = NumberOfRejectCallDetected + 1
                    CallRejectDetected = False
                    break

                if CallAutoEndtDetected == True :
                    time.sleep(10) 
                    break   

                if datetime.datetime.now() >= endtime :
                    time.sleep(30)
                    Cmds = 'adb -s ' + MP1_SerialNumber + ' shell input keyevent 6'
                    proc1 = subprocess.Popen(Cmds,stdout=subprocess.PIPE, shell = True)
                    time.sleep(5)
                    proc1.kill()
                    proc1.wait()
                    break
                
    while 1:                       
        MicTestAnalyze.expect(["\r\n", pexpect.EOF],timeout = 120)
        out = MicTestAnalyze.before.split("\r\n")
        for line in out :
            print(line)
            if (line.find('Waiting') != -1) :
                TerminateCount = TerminateCount + 1
                MicTestAnalyze.send('1' + "\n")
                print('Sending 1 and Closing App')
                if TerminateCount == 3:
                    break   
        if TerminateCount != 0 :
            time.sleep(30)
            break                    