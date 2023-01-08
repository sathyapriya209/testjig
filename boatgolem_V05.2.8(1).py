#Project Name : boAt Golem
#Author       : boAt SW - boAt R&D
#Date         : 16th November 2022
#Version      : v5.2.8
#Description  : Automation for Testing the Hearables

#import libraries

#import related to KIVY
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '1100')
Config.set('graphics', 'height', '700')
import kivy
kivy.require("1.9.1")
from kivymd.app import MDApp
import UI
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition, FadeTransition, NoTransition
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import mainthread, Clock

#imports for General libraries
import time
import datetime
import math
import os
import os.path
from os import path
import subprocess
from subprocess import PIPE, Popen
import threading
import socket

#import for other Function specific
from adafruit_servokit import ServoKit
from pynput import keyboard 
from pynput.keyboard import *
import json
import pyautogui

#imports for Audio analysis
import wave
import audioop, numpy as np
import contextlib
import audioop

#imports for BLUETOOTH CONTROL and battery monitoring
from bluetoothctl import *
from battery import *
from queue import Queue

import xlsxwriter

#Global variables
global Device_Name
global MacAddress
global FWVer_Or_CRC
global Logtext
global ctctt

global Lngend
global Bttimes
global BTpairtimes
global RssiDuration
global VolumeControl

global gleftstNoOfTimes
global gleftstInterval
global gleftdtNoOfTimes
global gleftdtInterval
global gleftltNoOfTimes
global gleftltInterval

global grightstNoOfTimes
global grightstInterval
global grightdtNoOfTimes
global grightdtInterval
global grightltNoOfTimes
global grightltInterval

global gCC_AnsEndNoOfTimes
global gCC_RejectNoOfTimes        
global gPC_PlayPauseNoOfTimes
global gPC_NextPrevNoOfTimes
global gPC_VolumeNoOfTimes

global MP1_OsVersion
global MP1_ModelName
global MP1_SerialNumber
global MP1_PhoneNumber
global MP2_SerialNumber

global rightst
global rightdt
global rightlt

global leftst
global leftdt
global leftlt

global callcontrol
global playcontrol

global leftCalibration
global rightCalibration        

global checkLng
global checkBT
global checkctc
global checkAudioTesting
global checkSpeakerTesting
global checkMpTesting
global checkBattery
global checkRssi

global DefaultLngend
global DefaultVolume
global DefaultBttimes
global DefaultBTpairtimes
global DefaultRssiDuration

global gDefaultleftstNoOfTimes
global gDefaultleftstInterval
global gDefaultleftdtNoOfTimes
global gDefaultleftdtInterval
global gDefaultleftltNoOfTimes
global gDefaultleftltInterval

global gDefaultrightstNoOfTimes
global gDefaultrightstInterval
global gDefaultrightdtNoOfTimes
global gDefaultrightdtInterval
global gDefaultrightltNoOfTimes
global gDefaultrightltInterval

global gDefaultCC_AnsEndNoOfTimes
global gDefaultCC_RejectNoOfTimes        
global gDefaultPC_PlayPauseNoOfTimes
global gDefaultPC_NextPrevNoOfTimes
global gDefaultPC_VolumeNoOfTimes

global tapdflag
global Logfile
global DeviceDisconnectCmd
global AirohaBasedProduct
global NB_Product

global TesterName
global ToolVersion

global stop_calibration_flag
global ctc_test_ended

playpause = '<269025073>'
global Keyboard
global PlayPauseStatus
global NumberOfPlayPauseInLngHourPlayback

global Worksheet
global MyWorkbook
global ActualRow
global TestCaseSerialNumber

global RowQueue
global ColumnQueue
global MessageQueue
global LogQueue
global DataFormatQueue

global XlsName
global LogFileName
global DirName

global TimeToWriteInXlsFile
global TimeToWriteInLogFile

global NumberOfAnsCallDetected
global NumberOfEndCallDetected
global NumberOfRejectCallDetected

global gNumberOfPlayDetectedInADB_Control
global gNumberOfPauseDetectedInADB_Control
global gNumberOfNextDetectedInADB_Control
global gNumberOfPrevDetectedInADB_Control

global gNumberOfPlayDetectedInCTC_Control
global gNumberOfPauseDetectedInCTC_Control
global gNumberOfNextDetectedInCTC_Control
global gNumberOfPrevDetectedInCTC_Control

global IsHeadPhoneDevice
global MaxMessagelength
global s

tapdflag = int(0)
TestCaseSerialNumber = int(1)
MaxMessagelength = [-1,-1,-1,-1,-1,-1,-1]

#Default number of times
Lngend=int(60)
Bttimes=int(10)
BTpairtimes=int(10)
RssiDuration=int(30)
StopTesting = False
VolumeControl = int(60)

gleftstNoOfTimes = int(15)
gleftstInterval = int(3)
gleftdtNoOfTimes = int(15)
gleftdtInterval = int(3)
gleftltNoOfTimes = int(15)
gltInterval = int(3)

grightstNoOfTimes = int(15)
grightstInterval = int(3)
grightdtNoOfTimes = int(15)
grightdtInterval = int(3)
grightltNoOfTimes = int(15)
grightltInterval = int(3)

gCC_AnsEndNoOfTimes = int(3)
gCC_RejectNoOfTimes = int(3)        
gPC_PlayPauseNoOfTimes = int(3)
gPC_NextPrevNoOfTimes = int(3)
gPC_VolumeNoOfTimes = int(3)

NumberOfPlayPauseInLngHourPlayback = int(0)

IsHeadPhoneDevice= False        
checkBT=False
checkLng=False
checkctc = False
checkAudioTesting = False
checkBattery = False
checkRssi = False
checkSpeakerTesting = False
checkMpTesting = False

leftst = False
leftdt = False
leftlt = False
rightst = False
rightdt = False
rightlt = False
callcontrol = False
playcontrol = False

leftCalibration = False
rightCalibration = False

#Default number of times
DefaultLngend=int(60)
DefaultVolume=int(60)
DefaultBttimes=int(10)
DefaultBTpairtimes=int(10)
DefaultRssiDuration=int(30)

gDefaultleftstNoOfTimes = int(15)
gDefaultleftstInterval = int(3)
gDefaultleftdtNoOfTimes = int(15)
gDefaultleftdtInterval = int(3)
gDefaultleftltNoOfTimes = int(15)
gDefaultleftltInterval = int(3)

gDefaultrightstNoOfTimes = int(15)
gDefaultrightstInterval = int(3)
gDefaultrightdtNoOfTimes = int(15)
gDefaultrightdtInterval = int(3)
gDefaultrightltNoOfTimes = int(15)
gDefaultrightltInterval = int(3)

gDefaultCC_AnsEndNoOfTimes = int(3)
gDefaultCC_RejectNoOfTimes = int(3)       
gDefaultPC_PlayPauseNoOfTimes = int(3)
gDefaultPC_NextPrevNoOfTimes = int(3)
gDefaultPC_VolumeNoOfTimes = int(3)

NumberOfAnsCallDetected = int(0)
NumberOfEndCallDetected = int(0)
NumberOfRejectCallDetected = int(0)

gNumberOfPlayDetectedInADB_Control = int(0)
gNumberOfPauseDetectedInADB_Control = int(0)
gNumberOfNextDetectedInADB_Control = int(0)
gNumberOfPrevDetectedInADB_Control = int(0)

gNumberOfPlayDetectedInCTC_Control = int(0)
gNumberOfPauseDetectedInCTC_Control = int(0)
gNumberOfNextDetectedInCTC_Control = int(0)
gNumberOfPrevDetectedInCTC_Control = int(0)

MacAddress = None
MP1_OsVersion = None
MP1_ModelName = None
MP1_SerialNumber = None
MP1_PhoneNumber = None
MP2_SerialNumber = None

TesterName = None
ToolVersion = None
DirName = None
XlsName = None
LogFileName = None
Worksheet = None
Logfile = None
DeviceDisconnectCmd = False
AirohaBasedProduct = False
NB_Product = False
Logtext=""
ctctt = 0
ActualRow = int(0)
RowQueue = Queue()
ColumnQueue = Queue()
MessageQueue = Queue()
LogQueue = Queue()
DataFormatQueue = Queue()

Keyboard = Controller()
TimeToWriteInXlsFile = int(0)
TimeToWriteInLogFile = int(0)

s = None
PlayPauseStatus = False
# Class declaration
class LnghrConfig(BoxLayout):
    pass
class Lng_BT_Config(BoxLayout):
    pass
class BtConfig(BoxLayout):
    pass
class RssiConfig(BoxLayout):
    pass
class ctcConfig(BoxLayout):
    pass
class LogConfig(BoxLayout):
    pass
class Main(Screen):
    pass
class Progressscreen(Screen):
    pass

class CtcDialogLeftStConfig(BoxLayout):
    pass
class CtcDialogLeftDtConfig(BoxLayout):
    pass
class CtcDialogLeftLtConfig(BoxLayout):
    pass
class CtcDialogRightStConfig(BoxLayout):
    pass
class CtcDialogRightDtConfig(BoxLayout):
    pass
class CtcDialogRightLtConfig(BoxLayout):
    pass

class CallControlDialog(BoxLayout):
    pass
class PlayControlDialog(BoxLayout):
    pass
#First screen
class Logo(Screen,FloatLayout):
    secs = 0

    def __init__(self, **kwargs):
        super(Logo, self).__init__(**kwargs)
        self.orientation = "vertical"
        Clock.schedule_interval(self.update_time, 1)

    def update_time(self, sec):
        self.secs = self.secs + 1
        if self.secs == 1:
            self.manager.current = 'BT setting'
    def on_enter(self):
        self.ids.gif.anim_delay = 0.10
    pass

bl = Bluetoothctl()

#Get the BT device MAC address using Device name
def GetMacAddress(MyDeviceName):   
    return bl.findmac_address(MyDeviceName);

#Get the BT device connected/paired status using MAC address 
def DeviceStatusbyMacAddress(Inquery,MyMacAddress):
    global s
    if Inquery == 1:
        print('DeviceStatusbyMacAddress, Inquery == 1')
        if bl.get_device_connected_status(MyMacAddress) == True :
            return True        
    elif Inquery == 2:
        print('DeviceStatusbyMacAddress, Inquery == 2')
        if bl.get_device_paired_status(MyMacAddress) == True :
            return True
    
    if s != None:
        s.close()
        s = None
    return False

#Get the BT device RSSI value using MAC address
def GetDeviceDetails(MyMacAddress):
    app = MDApp.get_running_app()
    time.sleep(1)    
    Value = bl.rssiValue    
    app.Log("Rssi: " + str(Value) + " dB")

#Get the BT device MAC address using Device name
def GetMacAddress1(DeviceName):
    MacAdd = None
    app = MDApp.get_running_app()
    time.sleep(1)    
    cmd = "bluetoothctl devices | grep \"" + DeviceName + "\""
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell = True)
    for line in proc.stdout:
        DeviceInfo = str(line,'UTF-8')
        if DeviceName in DeviceInfo:
            try:
                device_position = DeviceInfo.index(DeviceName)                        
            except ValueError:
                    pass
            else:
                if device_position > 21:
                    MacAdd = DeviceInfo[device_position-18:device_position-1]
            proc.kill()
            break                            
    proc.wait()    
    return (MacAdd)

#Get the Battery percentage of the connected device
def GetBatteryPercentage(MyMacAddress):
    global AirohaBasedProduct
    global NB_Product
    app = MDApp.get_running_app()    
    time.sleep(1)
    global s
    
    #Getting the Battery percentage for the Airoha based BT devices
    if AirohaBasedProduct == True:
        port = 3
        if s == None:
            s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
            s.connect((MyMacAddress,port))
        
        s.send(bytes([0x05,0x5A,0x03,0x00,0xD6,0x0C,0x00]))
        response = s.recv(20)
        response = s.recv(20)
        MyValue = response.hex()    
        Value1 = MyValue[len(MyValue)-2:len(MyValue)]
        Value = Value1
        
        if NB_Product == True:
            #s.close()        
            return int(Value,16)
    
        s.send(bytes([0x05,0x5A,0x03,0x00,0xD6,0x0C,0x01]))
        response = s.recv(20)
        ValidateResponse = response.hex()
        resp = ValidateResponse[len(ValidateResponse)-2:len(ValidateResponse)]
        print(resp)
        if resp != "ff":
            print("Patner")
            response = s.recv(20)
            MyValue = response.hex()    
            Value2 = MyValue[len(MyValue)-2:len(MyValue)]            
            if Value2 < Value1 :
                Value = Value2
        
        #s.close()        
        return int(Value,16)
    
    #Getting the battery percentage for other chipset deives
    else :
        try:
            query = BatteryStateQuerier(MyMacAddress)
        except:
            Value = -1
            return Value
        Value = int(query)
        del query
        return Value

#Connecting to a device using MAC address
def DeviceConnectbyMacAddress(Inquery,MyMacAddress, SkipDeviceDetails):        
    if SkipDeviceDetails == False:
        GetDeviceDetails(MyMacAddress)
    if Inquery == 1:        
        ret = bl.get_device_trusted_status(MyMacAddress)
        if ret == False:
            bl.connect(MyMacAddress,1)
        else :
            bl.connect(MyMacAddress,0)
    elif Inquery == 2:        
        bl.pair(MyMacAddress,1)
        time.sleep(1)
        bl.connect(MyMacAddress,0)
    return DeviceStatusbyMacAddress(1,MyMacAddress)

#Disconnecting a device using MAC address
def DeviceDisConnectbyMacAddress(Inquery,MyMacAddress):    
    if Inquery == 1:
        bl.disconnect(MyMacAddress)
        return DeviceStatusbyMacAddress(1,MyMacAddress)
    elif Inquery == 2:
        return DeviceUnPairbyMacAddress(MyMacAddress)

#Unpairing the device using MAC address
def DeviceUnPairbyMacAddress(MyMacAddress):
    bl.remove(MyMacAddress)
    return DeviceStatusbyMacAddress(1,MyMacAddress)

def CTC_Control(left,Single):    
    try:
        kit = ServoKit(channels=16)
        Right_Motor = 0
        Left_Motor = 15
        Right_Motor_Initial_Angle = 45
        Left_Motor_Initial_Angle = 120
        
        kit.servo[Left_Motor].angle = Left_Motor_Initial_Angle
        kit.servo[Right_Motor].angle = Right_Motor_Initial_Angle
    except:
        print('Servo is not connected')
        return
    
    time.sleep(1)

    if left == 1 :
        #left CTC touch 
        if Single == 1 :
            kit.servo[Left_Motor].angle = Left_Motor_Initial_Angle -35
            time.sleep(0.25)
            kit.servo[Left_Motor].angle = Left_Motor_Initial_Angle
        else :
            kit.servo[Left_Motor].angle = Left_Motor_Initial_Angle -35
            time.sleep(0.15)
            kit.servo[Left_Motor].angle = Left_Motor_Initial_Angle
            time.sleep(0.15)
            kit.servo[Left_Motor].angle = Left_Motor_Initial_Angle -35
            time.sleep(0.15)
            kit.servo[Left_Motor].angle = Left_Motor_Initial_Angle
            
    else :
        if Single == 1 :
            kit.servo[Right_Motor].angle = Right_Motor_Initial_Angle + 35
            time.sleep(0.25)
            kit.servo[Right_Motor].angle = Right_Motor_Initial_Angle
        else :
            kit.servo[Right_Motor].angle = Right_Motor_Initial_Angle + 35
            time.sleep(0.15)
            kit.servo[Right_Motor].angle = Right_Motor_Initial_Angle
            time.sleep(0.15)
            kit.servo[Right_Motor].angle = Right_Motor_Initial_Angle + 35
            time.sleep(0.15)
            kit.servo[Right_Motor].angle = Right_Motor_Initial_Angle
    
    
def DeviceControlMobilePhone(DeviceName, MacAddress):
    
    global callcontrol
    global playcontrol
    
    global NumberOfAnsCallDetected
    global NumberOfEndCallDetected
    global NumberOfRejectCallDetected
    
    global gNumberOfPlayDetectedInADB_Control
    global gNumberOfPauseDetectedInADB_Control
    global gNumberOfNextDetectedInADB_Control
    global gNumberOfPrevDetectedInADB_Control
    
    global gNumberOfPlayDetectedInCTC_Control
    global gNumberOfPauseDetectedInCTC_Control
    global gNumberOfNextDetectedInCTC_Control
    global gNumberOfPrevDetectedInCTC_Control

    global bTest
    global gCC_AnsEndNoOfTimes
    global gCC_RejectNoOfTimes        
    global gPC_PlayPauseNoOfTimes
    global gPC_NextPrevNoOfTimes
    global gPC_VolumeNoOfTimes
    
    global MP1_OsVersion
    global MP1_ModelName
    global MP1_SerialNumber
    global MP1_PhoneNumber
    global MP2_SerialNumber
    global IsHeadPhoneDevice
    global CTC_TestInProgress
    
        
    app = MDApp.get_running_app()    
    time.sleep(1)    
              
    
    if callcontrol != True and playcontrol != True :
        return 

    SearchMac = MacAddress[12:17]
    SearchDevName = DeviceName + '_' + MacAddress[12:14] +  MacAddress[15:17]
    print(SearchDevName)
    
    TerminateCount = int(0)
    TerminateLoop = False    
    MicTestAnalyze = pexpect.spawn("java -jar Connection1.0.4.jar", encoding='utf-8',echo=False)
    DeviceConnectedInPhone = False
                               
    while 1:
        try:                          
            MicTestAnalyze.expect(["\r\n", pexpect.EOF],timeout = 120)
            out = MicTestAnalyze.before.split("\r\n")
                               
            for line in out :
                print(line)
                if (line.find('Device Version') != -1) :
                    MicTestAnalyze.send(MP1_OsVersion + "\n")            
                elif (line.find('Device Model Name') != -1) :            
                    MicTestAnalyze.send(MP1_ModelName + "\n")
                elif (line.find('your Connected Device') != -1) :            
                    MicTestAnalyze.send(MP1_SerialNumber + "\n")            
                elif (line.find('Enter Last 4 digit of Mac Adress') != -1) :            
                    MicTestAnalyze.send(SearchMac + "\n")
                elif (line.find('Device name from the list') != -1) :            
                    MicTestAnalyze.send(SearchDevName + "\n")
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
                    print('Testing is going to be started')
                    DeviceConnectedInPhone = True
        
        except pexpect.TIMEOUT:
            print('Script is not responding')
            TerminateLoop = True
            break
        except :
            print('Something went wrong')
            TerminateLoop = True
            break
            
        if TerminateLoop == True or DeviceConnectedInPhone == True:
            print('Continuing')
            break
        
    if TerminateLoop == True :
        return
        
    if playcontrol == True :    
        if gPC_PlayPauseNoOfTimes != 0 and gPC_NextPrevNoOfTimes != 0 :            
            
            gNumberOfPlayDetectedInADB_Control = int(0)
            gNumberOfPauseDetectedInADB_Control = int(0)
            gNumberOfNextDetectedInADB_Control = int(0)
            gNumberOfPrevDetectedInADB_Control = int(0)
            
            gNumberOfPlayDetectedInCTC_Control = int(0)
            gNumberOfPauseDetectedInCTC_Control = int(0)
            gNumberOfNextDetectedInCTC_Control = int(0)
            gNumberOfPrevDetectedInCTC_Control = int(0)
            
            State = 0
            ActionCount = (gPC_PlayPauseNoOfTimes*2)
            bTest = False
            CTC_TestInProgress = False
            
            if gPC_PlayPauseNoOfTimes == 0:
                State = 1
                ActionCount = gPC_NextPrevNoOfTimes        
            
            BreakPlayControlLoop = False
            
            while BreakPlayControlLoop == False:                    
                
                NumberOfPlayDetected = int(0)
                NumberOfPauseDetected = int(0)
                NumberOfNextDetected = int(0)
                NumberOfPrevDetected = int(0)
                BreakPlayControlLoop = False
                 
                while State != 3:   # Execute if State != 3 , 0 - Play/Pause; 1 - Next; 2 - Prev;
                
                     #Clear logs 	
                    Cmds = 'adb -s ' + MP1_SerialNumber + ' logcat -c'
                    proc1 = subprocess.Popen(Cmds,stdout=subprocess.PIPE, shell = True)
                    time.sleep(5)
                    proc1.kill()
                    proc1.wait()
                        
                    if CTC_TestInProgress == False :
                        CommandGiven = False
                        while CommandGiven != True:
                            MicTestAnalyze.expect(["\r\n", pexpect.EOF],timeout = 120)
                            out = MicTestAnalyze.before.split("\r\n")       
                            for line in out :                        
                                if (line.find('Enter a number') != -1) :
                                    CommandGiven = True   
                                    if State == 0 :
                                        if bTest == False :
                                            MicTestAnalyze.send("0"+ "\n")
                                            bTest = True
                                        else :
                                            MicTestAnalyze.send("1"+ "\n")
                                            bTest = False
                                    elif State == 1 :
                                        MicTestAnalyze.send("2"+ "\n")
                                    elif State == 2 :    
                                        MicTestAnalyze.send("3"+ "\n")
                                        
                                    break # break for for loop 
                             
                    else:
                        print("entering ctc")
                        CommandGiven = True
                        if State == 0 :                            
                            if bTest == False :
                                bTest = True
                                CTC_Control(1,1)                
                            else :
                                CTC_Control(0,1)
                                bTest = False
                        elif State == 1 :
                            CTC_Control(0,0)
                        elif State == 2 :    
                            CTC_Control(1,0)
                            time.sleep(2)
                            CTC_Control(1,0)
                        
                    time.sleep(15)
                    
                    if State == 0:
                        Cmds ='adb -s ' +  MP1_SerialNumber + ' logcat  APM_AudioPolicyManager:V *:S -d'                         
                    else :
                        Cmds ='adb -s ' +  MP1_SerialNumber + ' logcat FaceWidgetMediaSessionManager:V *:S -d'                    
            
                    proc1 = subprocess.Popen(Cmds, stdout=subprocess.PIPE, shell = True)
                    for line in proc1.stdout:
                        print(line)
                        if b"startOutput" in line and State == 0 :                            
                            NumberOfPlayDetected = NumberOfPlayDetected + 1
                            print( " Song Played successfully " ) 
                            break                                        
                        if b"stopOutput" in line and State == 0 :                            
                            NumberOfPauseDetected = NumberOfPauseDetected + 1             
                            print( " Song Paused successfully " )
                            break 
                        if b"onMetadataChanged()" in line and State == 1:                            
                            NumberOfNextDetected = NumberOfNextDetected + 1            
                            print( " Next Song Played Sucessfully " )
                            break
                        if b"onMetadataChanged()" in line and State == 2:                            
                            NumberOfPrevDetected = NumberOfPrevDetected + 1           
                            print( " Prev Song Played successfully " )
                            break

                    proc1.kill()
                    proc1.wait()
            
                
                    ActionCount = ActionCount - 1
                    if ActionCount == 0:
                        State = State + 1
                        ActionCount = gPC_NextPrevNoOfTimes
                        
                        if State == 3:
                        
                            print(NumberOfPlayDetected)
                            print(NumberOfPauseDetected)
                            print(NumberOfNextDetected)
                            print(NumberOfPrevDetected)
                            
                            if CTC_TestInProgress == True:
                                MicTestAnalyze.send("5"+ "\n")
                                print("sent 5")
                                gNumberOfPlayDetectedInCTC_Control = NumberOfPlayDetected
                                gNumberOfPauseDetectedInCTC_Control = NumberOfPauseDetected
                                gNumberOfNextDetectedInCTC_Control = NumberOfNextDetected
                                gNumberOfPrevDetectedInCTC_Control = NumberOfPrevDetected
                                
                                BreakPlayControlLoop = True
                                break
                            else :                            
                                if IsHeadPhoneDevice == True :
                                    MicTestAnalyze.send("4"+ "\n")      # Terminate PlayControl CTC                                  
                                    MicTestAnalyze.send("5"+ "\n")      # Terminate PlayControl CTC  
                                    BreakPlayControlLoop = True
                                else :
                                    
                                    gNumberOfPlayDetectedInADB_Control = NumberOfPlayDetected
                                    gNumberOfPauseDetectedInADB_Control = NumberOfPauseDetected
                                    gNumberOfNextDetectedInADB_Control = NumberOfNextDetected
                                    gNumberOfPrevDetectedInADB_Control = NumberOfPrevDetected
                                    
                                    MicTestAnalyze.send("5"+ "\n")
                                    
                                    print("CTC cycle")
                                    CTC_TestInProgress = True
                                    State = 0
                                    ActionCount = (gPC_PlayPauseNoOfTimes*2)
                                    bTest = False
                            
                '''if BreakPlayControlLoop == True:
                    MicTestAnalyze.send("5"+ "\n")
                    break'''
           
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
                            proc1.kill()
                            proc1.wait()
                        else :
                            CTC_Control(1,0)
                            time.sleep(10)

                    Cmds = 'adb -s ' + MP1_SerialNumber + ' logcat  RegiGvnBase:V *:S -d'
                    proc1 = subprocess.Popen(Cmds, stdout=subprocess.PIPE, shell = True)

                    for line in proc1.stdout:
                        
                        if b"RegiGvnBase: onCallStatus: event=EVENT_CALL_LAST_CALL_END" in line:
                            CallEndDetected = True
                            print("Call is Ended")
                            break
                        
                        if b"RegiGvnBase: onCallStatus: event=EVENT_CALL_ESTABLISHED" in line:                            
                            CallAcceptanceDetected = True                
                            print("Incoming Call Answered")
                            continue
                        
                    proc1.kill()
                    proc1.wait()                                                        

                    if CallAcceptanceDetected == True:
                        print('CallAcceptDetected')
                        time.sleep(30)
                        NumberOfAnsCallDetected = NumberOfAnsCallDetected + 1
                        CallAcceptanceDetected = False
                        ContinueInCall = True
                        continue
                                                            
                    if CallEndDetected == True :
                        print('CallEndDetected')
                        time.sleep(30)
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
                time.sleep(5)
                proc.kill()
                proc.wait()
                    
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
#                     print(Cmds)
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
                        print('CallRejectDetected')
                        time.sleep(30)
                        NumberOfRejectCallDetected = NumberOfRejectCallDetected + 1
                        CallRejectDetected = False                        
                        break

                    if CallAutoEndtDetected == True :
                        print('CallAutoEndtDetected')
                        time.sleep(30) 
                        break   

                    if datetime.datetime.now() >= endtime :
                        print('datetime.datetime.now()')
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
            if ((line.find('Waiting') != -1) or (line.find('Enter a number ') != -1)) : 
                TerminateCount = TerminateCount + 1
                MicTestAnalyze.send("7" + "\n")                
                MicTestAnalyze.send("9" + "\n")
                print("Sending 7 and Closing App")
                if TerminateCount == 3:
                    break        
        if TerminateCount == 3 :
            time.sleep(30)
            break                            
    
def MyWriteXls():
    global Worksheet
    global MyWorkbook
    global XlsName
    global RowQueue
    global ColumnQueue
    global MessageQueue
    global DataFormatQueue
    global DirName
    global MaxMessagelength
    global ActualRow
        
    if XlsName == None :
        return
        
    isExist = os.path.exists(DirName)

    if not isExist:
            # Create a new directory because it does not exist 
        os.makedirs(DirName)
            
    MyWorkbook = xlsxwriter.Workbook(XlsName)
    Worksheet = MyWorkbook.add_worksheet()
        
    data_format1 = MyWorkbook.add_format({'border':1,'align':'left'})
    data_format2 = MyWorkbook.add_format({'border':1,'align':'center','bold':True})
    
    data_format3 = MyWorkbook.add_format({'border':1,'align':'center','bold':True,'bg_color':'yellow'})
    data_format4 = MyWorkbook.add_format({'border':1,'align':'center','bg_color':'green'})
    data_format5 = MyWorkbook.add_format({'border':1,'align':'center','bg_color':'red'})
    
    
    for i in range(len(MaxMessagelength)):
        if MaxMessagelength[i] != -1 :
            Worksheet.set_column(i, i, MaxMessagelength[i] + 2)

    for i in range(2, 10):
        for j in range(2, 4):
            Worksheet.write(i,j,'',data_format1)

    if ActualRow >11:
        for i in range(11,(ActualRow + 2)):
            for j in range(1, 6):
                Worksheet.write(i,j,'',data_format1)
    
        
    while RowQueue.empty() != True :
        dataformat = DataFormatQueue.get()
        if dataformat == 1:
            Worksheet.write(RowQueue.get(),ColumnQueue.get(),MessageQueue.get(),data_format1)
        elif dataformat == 2:
            Worksheet.write(RowQueue.get(),ColumnQueue.get(),MessageQueue.get(),data_format2)
        elif dataformat == 3:
            Worksheet.write(RowQueue.get(),ColumnQueue.get(),MessageQueue.get(),data_format3)
        elif dataformat == 4:
            Worksheet.write(RowQueue.get(),ColumnQueue.get(),MessageQueue.get(),data_format4)
        elif dataformat == 5:
            Worksheet.write(RowQueue.get(),ColumnQueue.get(),MessageQueue.get(),data_format5)
        else:
            Worksheet.write(RowQueue.get(),ColumnQueue.get(),MessageQueue.get(),data_format1)
        
    MyWorkbook.close()
    Worksheet = None
    

#@mainthread    
def MyLogFile():
    global Logfile
    global LogFileName
    global LogQueue
    global DirName

    dt = datetime.datetime.now()
    
    isExist = os.path.exists(DirName)
    if not isExist:
        # Create a new directory because it does not exist 
        os.makedirs(DirName)
        
    if Logfile == None :
        Logfile = open(LogFileName, "a")

    while LogQueue.empty() != True :
        Logfile.write(LogQueue.get())
        
    Logfile.flush()
    Logfile.close()
    Logfile = None
    
#To log the message into LogFile
#@mainthread
def LogFile(message):
    global Device_Name
    global MacAddress
    global LogFileName
    global LogQueue
    global TimeToWriteInLogFile
    global DirName

    dt = datetime.datetime.now()
    
    #print(os.path.dirname(os.getcwd()))
    
    if LogFileName == None :
        DirName = str(os.path.dirname(os.getcwd())) + "/Reports/" + (dt.strftime("%Y_%m_%d/"))
        LogFileName = str(DirName) +"logfile_" + Device_Name.replace(" ","_").replace("/","_") + "_" + MacAddress.replace(":","_") + "_" + (dt.strftime("%H_%M_%S")) + ".txt"
        
    LogQueue.put((dt.strftime("%Y-%m-%d %H:%M:%S")) + " :  " + message + "\n")
    TimeToWriteInLogFile += 1
    if TimeToWriteInLogFile == 20:
        TimeToWriteInLogFile = 0
        MyLogFile()
        
#Get the checkbox enabled / disabled status of each test case
class TESTScreen(Screen):
    def checkbox_click_lnghr(self, instance, value,text):
        global checkLng
        checkLng = value
        
    def checkbox_click_bt(self, instance, value,text):
        global checkBT        
        checkBT = value       
       
    def checkbox_click_ctc(self, instance, value,text):
        global checkctc
        checkctc = value
        
    def checkbox_click_battery(self, instance, value,text):
        global checkBattery
        checkBattery = value
        
    def checkbox_click_rssi(self, instance, value,text):
        global checkRssi
        checkRssi = value    
    
    def checkbox_click_audiotesting(self, instance, value,text):
        global checkAudioTesting
        checkAudioTesting = value
        
    def checkbox_click_mpcontrol(self, instance, value,text):
        global checkMpTesting
        checkMpTesting = value
    
    def checkbox_click_speakertesting(self, instance, value,text):
        global checkSpeakerTesting
        checkSpeakerTesting = value

#Class declartion for Calibration configuration screen and getting the status of check boxes
class Calibration_ConfigurationScreen(Screen):
    def checkbox_click_leftCali(self, instance, value,text):
        global rightCalibration
        global leftCalibration
        leftCalibration = value
        if leftCalibration == True:
            rightCalibration = False
        
    def checkbox_click_rightCali(self, instance, value,text):
        global rightCalibration
        global leftCalibration
        rightCalibration = value
        if rightCalibration == True:
            leftCalibration = False    

#Class declartion for CTC test cases selection screen and getting the status of check boxes
class CTC_ConfigurationScreen(Screen):
    def checkbox_click_leftst(self, instance, value,text):
        global leftst
        leftst = value
        
    def checkbox_click_leftdt(self, instance, value,text):
        global leftdt
        leftdt = value
        
    def checkbox_click_leftlt(self, instance, value,text):
        global leftlt
        leftlt = value
        
    def checkbox_click_rightst(self, instance, value,text):
        global rightst
        rightst = value
        
    def checkbox_click_rightdt(self, instance, value,text):
        global rightdt
        rightdt = value
        
    def checkbox_click_rightlt(self, instance, value,text):
        global rightlt
        rightlt = value

class MPC_ConfigurationScreen(Screen):  
    def checkbox_click_CallControl(self, instance, value,text):
        global callcontrol
        callcontrol = value
        
    def checkbox_click_PlayControl(self, instance, value,text):
        global playcontrol
        playcontrol = value
        
####################  Main  ########################
class MainApp(MDApp):
    dialog = None

    #Start the Tool with the title and Home screen
    def build(self):
        global DeviceDisconnectCmd        
        self.help_string = Builder.load_string(UI.UI)
        self.help_string.current = 'BT setting'
        DeviceDisconnectCmd = False 
        self.title = 'boAt Golem Automation tool (V05.2.8)'
        return self.help_string
    
    #To log the message into LogFile as well as Text box in tool
    @mainthread
    def Log(self,message):
        LogFile(message)
        self.LogTextbox(message)
    
    
    def WriteXls(self,Row,Column,Message,DataFormat):

        global Device_Name
        global MacAddress
        global ActualRow
        global TestCaseSerialNumber
        global RowQueue
        global ColumnQueue
        global MessageQueue
        global XlsName
        global TimeToWriteInXlsFile
        global DirName
        global DataFormatQueue
        global MaxMessagelength
        
        dt = datetime.datetime.now()
        
        if XlsName == None :
            DirName = str(os.path.dirname(os.getcwd())) + "/Reports/" + (dt.strftime("%Y_%m_%d/"))
            XlsName = str(DirName) +"TestReport_" + Device_Name.replace(" ","_") + "_" + MacAddress.replace(":","_") + "_" + (dt.strftime("%H_%M_%S")) + ".xlsx"
            ActualRow = int(0)
            TestCaseSerialNumber = int(1)
        
        if Row == 0:
            FinalRow = ActualRow + 1
            ActualRow = FinalRow
        elif Row == -1:
            FinalRow = ActualRow
        else :
            ActualRow = Row
            FinalRow = Row

        RowQueue.put(FinalRow)
        ColumnQueue.put(Column)
        MessageQueue.put(Message)
        DataFormatQueue.put(DataFormat)
    
        if MaxMessagelength[Column] < len(Message) :
            MaxMessagelength[Column] = len(Message)
        
        TimeToWriteInXlsFile += 1
        if TimeToWriteInXlsFile == 10 :
            TimeToWriteInXlsFile = 0
           
       
    #To log the message into Text box in tool
    #@mainthread
    def LogTextbox(self,message):
        global Logtext
        dt = datetime.datetime.now()
        logsumry = str(dt.strftime("%Y-%m-%d %H:%M:%S")) + " :  " + message
        Logtext += "\n" + logsumry
        self.help_string.get_screen('Test').ids.sumtext.text = str(Logtext)
       
    ############# BT Pairing, Connection and Disconnection ########################
    #Disconnect the BT device
    #@mainthread
    def Disconnect(self):
        # Take user defined device name
        global MacAddress
        global Logtext
        global DeviceDisconnectCmd
        global XlsName
        global LogFileName
        global s
        
        if s != None:
            s.close()
            s = None
        
        result = DeviceStatusbyMacAddress(1,MacAddress)
        if result == True:
            DeviceDisConnectbyMacAddress(2,MacAddress)
            DeviceDisconnectCmd = True 
            GetDeviceDetails(MacAddress)
        
        MyLogFile()
        MyWriteXls()
        Logtext = ''
        XlsName = None        
        MacAddress = None
        '''self.help_string.get_screen('Test').ids.sumtext.text = str(Logtext)        
        self.help_string.current = 'BT setting'        '''
        @mainthread
        def updater():
            self.help_string.get_screen('Test').ids.sumtext.text = str(Logtext)        
            self.help_string.current = 'BT setting'
        updater()
    
    #Connect the BT device
    def connect(self):
        global Device_Name
        global FWVer_Or_CRC
        Device_Name = str(self.help_string.get_screen('BT setting').ids.DeviceName.text)
        FWVer_Or_CRC = str(self.help_string.get_screen('BT setting').ids.Firmware_or_CRC.text)
        print(Device_Name)
        
        if Device_Name == "":
            def show_alert_dialog(self):
                self.dialog = MDDialog(
                    text="Please Enter device Name")
                self.dialog.open()
            show_alert_dialog(self)
            def dia(dt):
                self.dialog.dismiss(force=True)
            Clock.schedule_once(dia, 3)
        else:
            self.BtPair()
    
    #Pair and connect to BT device
    def BtPair(self):
        global MacAddress
        global AirohaBasedProduct
        global FWVer_Or_CRC
        global Device_Name
        global TesterName
        global ToolVersion
        global IsHeadPhoneDevice
        global s

        connected_dev=False
        IsHeadPhoneDevice = False
        bl.remove_all()
        time.sleep(3)
        
        MacAddress = bl.ConnectWithDevice(Device_Name)        
        if MacAddress == None:
            print('Mac address is not found')
            connected_dev = False
        else :
            print(MacAddress)            
            self.Log(Device_Name)
            self.Log(MacAddress)
            self.Log("Default Codec : SBC")
            self.Log("FW Version/CRC: " + FWVer_Or_CRC)
            AirohaBasedProduct = False    
            RetryCount = 0
            while RetryCount < 3:
                result = DeviceConnectbyMacAddress(2,MacAddress,False)
                if result == True:
                    break
                RetryCount += 1
                
            if result == False:
                connected_dev = False
            else:
                connected_dev = True
                    
        if connected_dev == True:
            self.Log("Device is connected") 
            self.help_string.current = 'Test'            
            
            Search = Device_Name.find('Rockerz')
            if Search != -1 :
                IsHeadPhoneDevice = True
            
            self.LoadTestConfiguration()
            self.LoadOtherDetails()
            self.LoadMobilePhoneDetails()
            
            AirohaBasedProduct = self.IsDeviceAirohaBased(Device_Name)
            BatteryValue = GetBatteryPercentage(MacAddress)            
            self.Log("Current Battery Value : " + str(BatteryValue))
            if s != None:
                s.close()
                s = None
            
            self.WriteXls(2,2,'Tester',2)        
            self.WriteXls(2,3,TesterName,1)
        
            self.WriteXls(3,2,'Tool Version',2)
            self.WriteXls(3,3,ToolVersion,1)
        
            self.WriteXls(4,2,'DeviceName',2)        
            self.WriteXls(4,3,Device_Name,1)
        
            self.WriteXls(5,2,'Mac Address',2)        
            self.WriteXls(5,3,MacAddress,1)
        
            self.WriteXls(6,2,'Firmware Version',2)        
        
            self.WriteXls(7,2,'Firmware CRC',2)
            self.WriteXls(7,3,FWVer_Or_CRC,1)
        
            self.WriteXls(8,2,'Test Results',2)        
        
            self.WriteXls(11,1,'S.No',3) 
            self.WriteXls(11,2,'Test Cases',3)
            self.WriteXls(11,3,'Test Data',3)             
            self.WriteXls(11,4,'Pass Criteria',3)
            self.WriteXls(11,5,'Test Results',3)
            
        else:
            print('Device is NOT connected')
            def show_alert_dialog(self):
                self.dialog = MDDialog(
                    text="Device is not connetced, Please check device name and retry",
                    buttons=[
                        MDFlatButton(
                            text="OK", text_color=self.theme_cls.primary_color, on_release=self.closeDialogConnect
                            ),
                        ]
                 )
                self.dialog.open()                
            show_alert_dialog(self)
    
    #CTC Calibration
    #CTC calibration UI management
    def CTC_Calibration(self): 
            global rightCalibration
            global leftCalibration
            self.help_string.current = 'Calibration'
            self.help_string.get_screen('Calibration').ids.StartCalibration.disabled = True
            self.help_string.get_screen('Calibration').ids.StopCalibration.disabled = True
            self.help_string.get_screen('Calibration').ids.LeftEarbudCaliCheck.active = False
            self.help_string.get_screen('Calibration').ids.RightEarbudCaliCheck.active = False
            leftCalibration = False
            rightCalibration = False
        
    def LeftEarbudCalibrationCheck(self):
        if leftCalibration == True:
            self.help_string.get_screen('Calibration').ids.StartCalibration.disabled = False
            self.help_string.get_screen('Calibration').ids.RightEarbudCaliCheck.active = False
        else :
            self.help_string.get_screen('Calibration').ids.StartCalibration.disabled = True

    def RightEarbudCalibrationCheck(self):
         if rightCalibration == True:
            self.help_string.get_screen('Calibration').ids.StartCalibration.disabled = False
            self.help_string.get_screen('Calibration').ids.LeftEarbudCaliCheck.active = False
         else :
             self.help_string.get_screen('Calibration').ids.StartCalibration.disabled = True
    
    #Executing CTC calibration
    def StartCalibration(self):
        global rightCalibration
        global leftCalibration
        
        self.help_string.get_screen('Calibration').ids.StartCalibration.disabled = True
        self.help_string.get_screen('Calibration').ids.CancelCalibration.disabled = True
        self.help_string.get_screen('Calibration').ids.StopCalibration.disabled = False
        
        print("Starting the calibration")
        kit = ServoKit(channels=16)
        Right_Motor = 0
        Left_Motor = 15
        
        Right_Motor_Initial_Angle = 45
        Left_Motor_Initial_Angle = 120
        

        #Initial positions of Servomotors 
        kit.servo[Right_Motor].angle = Right_Motor_Initial_Angle
        kit.servo[Left_Motor].angle = Left_Motor_Initial_Angle
        duration_bw_2_Single_taps = 6
        
        p = subprocess.Popen(['vlc', '/home/pi/Desktop/Golem/Test Song/sample.xspf'])
               
        #Execute the Left side CTC calibration
        def left_touch_cali():
            global stop_calibration_flag
            stop_calibration_flag = False
            repeat = 15           
            while (repeat):
                kit.servo[Left_Motor].angle = Left_Motor_Initial_Angle
                time.sleep(duration_bw_2_Single_taps)
                kit.servo[Left_Motor].angle = Left_Motor_Initial_Angle - 35
                time.sleep(0.25)
                repeat = repeat - 1
                if stop_calibration_flag == True:
                    break
            p = subprocess.Popen(['pkill', 'vlc'])
            p.communicate()
            kit.servo[Left_Motor].angle = Left_Motor_Initial_Angle
            self.help_string.get_screen('Calibration').ids.CancelCalibration.disabled = False
            self.help_string.get_screen('Calibration').ids.StartCalibration.disabled = False
            self.help_string.get_screen('Calibration').ids.StopCalibration.disabled = True 
        
        #Execute the Left side CTC calibration
        def Right_touch_cali():
            global stop_calibration_flag
            stop_calibration_flag = False
            repeat = 15           
            while (repeat):
                kit.servo[Right_Motor].angle = Right_Motor_Initial_Angle
                time.sleep(duration_bw_2_Single_taps)
                kit.servo[Right_Motor].angle = Right_Motor_Initial_Angle + 35
                time.sleep(0.25)
                repeat = repeat - 1
                if stop_calibration_flag == True:                        
                    break
            p = subprocess.Popen(['pkill', 'vlc'])
            p.communicate()
            kit.servo[Right_Motor].angle = Right_Motor_Initial_Angle
            self.help_string.get_screen('Calibration').ids.CancelCalibration.disabled = False
            self.help_string.get_screen('Calibration').ids.StartCalibration.disabled = False
            self.help_string.get_screen('Calibration').ids.StopCalibration.disabled = True 
                
        if leftCalibration == True:
            print('Left Calibration')
            left_cali_thread = threading.Thread(target = left_touch_cali)
            left_cali_thread.start()
            
        elif rightCalibration == True:
            print('Right Calibration')
            Right_cali_thread = threading.Thread(target = Right_touch_cali)
            Right_cali_thread.start()        
    
    #Stop the CTC calibration                
    def StopCalibration(self):
        global stop_calibration_flag
        self.help_string.get_screen('Calibration').ids.CancelCalibration.disabled = False
        self.help_string.get_screen('Calibration').ids.StartCalibration.disabled = False
        self.help_string.get_screen('Calibration').ids.StopCalibration.disabled = True
        stop_calibration_flag = True
        print("Stop calibration")

    def CancelCalibration(self):        
        self.help_string.current = 'Test'

    def OpenCTC(self):
        if checkctc == True:
            self.help_string.current = 'CTC'
    
    def OpenMobilePhoneControl(self):
        if checkMpTesting == True:
            self.help_string.current = 'MobilePhoneControl'
    
    #Dialog for Left single tap input
    def ctc_leftst_configration(self):
        global leftst        
        global ctctt

        if leftst == True:
            ctctt = 1
            self.dialog = MDDialog(
                title="Left Earbud Play/Pause Operation Configuration:",
                type="custom",
                content_cls=CtcDialogLeftStConfig(),
                buttons=[
                    MDFlatButton(
                        text="Cancel", text_color=self.theme_cls.primary_color, on_release=self.closeDialogCtcLeftSt
                    ),
                    MDFlatButton(
                        text="Submit", text_color=self.theme_cls.primary_color, on_release=self.saveCtcconfig
                    ),
                ],
            )
            self.dialog.open()
            
            
    #Dialog for Left double tap input
    def ctc_leftdt_configration(self): 
        global leftdt
        global ctctt
         
        if leftdt == True:
            ctctt = 3
            self.dialog = MDDialog(
                title="Left Earbud Previous Operation Configuration:",
                type="custom",
                content_cls=CtcDialogLeftDtConfig(),
                buttons=[
                    MDFlatButton(
                        text="Cancel", text_color=self.theme_cls.primary_color, on_release=self.closeDialogCtcLeftDt
                    ),
                    MDFlatButton(
                        text="Submit", text_color=self.theme_cls.primary_color, on_release=self.saveCtcconfig
                    ),
                ],
            )
            self.dialog.open()
            
    #Dialog for Right single tap input
    def ctc_rightst_configration(self):
        global rightst
        global ctctt

        if rightst == True:
            ctctt = 2
            self.dialog = MDDialog(
                title="Right Earbud Play/Pause Operation Configuration:",
                type="custom",
                content_cls=CtcDialogRightStConfig(),
                buttons=[
                    MDFlatButton(
                        text="Cancel", text_color=self.theme_cls.primary_color, on_release=self.closeDialogCtcRightSt
                    ),
                    MDFlatButton(
                        text="Submit", text_color=self.theme_cls.primary_color, on_release=self.saveCtcconfig
                    ),
                ],
            )
            self.dialog.open()

    #Dialog for Right double tap input
    def ctc_rightdt_configration(self):
        global rightdt
        global ctctt
        if rightdt == True:
            ctctt = 4
            self.dialog = MDDialog(
                title="Right Earbud Next Operation Configuration:",
                type="custom",
                content_cls=CtcDialogRightDtConfig(),
                buttons=[
                    MDFlatButton(
                        text="Cancel", text_color=self.theme_cls.primary_color, on_release=self.closeDialogCtcRightDt
                    ),
                    MDFlatButton(
                        text="Submit", text_color=self.theme_cls.primary_color, on_release=self.saveCtcconfig
                    ),
                ],
            )
            self.dialog.open()

    def ctc_callcontrol_configration(self):
        global callcontrol        

        if callcontrol == True:
            self.dialog = MDDialog(
                title="Call Control Configuration:",
                type="custom",
                content_cls=CallControlDialog(),
                buttons=[
                    MDFlatButton(
                        text="Cancel", text_color=self.theme_cls.primary_color, on_release=self.closeDialogCallControl
                    ),
                    MDFlatButton(
                        text="Submit", text_color=self.theme_cls.primary_color, on_release=self.saveMpconfig
                    ),
                ],
            )
            self.dialog.open()
            
            
    #Dialog for Left double tap input
    def ctc_playcontrol_configration(self): 
        global playcontrol
        
        if playcontrol == True:
            self.dialog = MDDialog(
                title="Play Control Configuration:",
                type="custom",
                content_cls=PlayControlDialog(),
                buttons=[
                    MDFlatButton(
                        text="Cancel", text_color=self.theme_cls.primary_color, on_release=self.closeDialogPlayControl
                    ),
                    MDFlatButton(
                        text="Submit", text_color=self.theme_cls.primary_color, on_release=self.saveMpconfig
                    ),
                ],
            )
            self.dialog.open()
    
    #Function for saving the CTC inputs
    def saveCtcconfig(self,inst):
        global gleftstNoOfTimes
        global gleftstInterval
        global gleftdtNoOfTimes
        global gleftdtInterval
        global gleftltNoOfTimes
        global gleftltInterval

        global grightstNoOfTimes
        global grightstInterval
        global grightdtNoOfTimes
        global grightdtInterval
        global grightltNoOfTimes
        global grightltInterval
        
        global gDefaultleftstNoOfTimes
        global gDefaultleftstInterval
        global gDefaultleftdtNoOfTimes
        global gDefaultleftdtInterval
        global gDefaultleftltNoOfTimes
        global gDefaultleftltInterval

        global gDefaultrightstNoOfTimes
        global gDefaultrightstInterval
        global gDefaultrightdtNoOfTimes
        global gDefaultrightdtInterval
        global gDefaultrightltNoOfTimes
        global gDefaultrightltInterval        
        global ctctt

        app = MDApp.get_running_app()

        if leftst == True:
            ctctt = 1
            try:
                gleftstNoOfTimes = int(app.leftstNoOfTimes)                
            except:
                gleftstNoOfTimes = gDefaultleftstNoOfTimes
                
            try:                
                gleftstInterval = int(app.leftstInterval)
            except:                
                gleftstInterval = gDefaultleftstInterval
                pass                

        if leftdt == True:
            ctctt = 3
            try:
                gleftdtNoOfTimes = int(app.leftdtNoOfTimes)                
            except:
                gleftdtNoOfTimes = gDefaultleftdtNoOfTimes                
            try:                
                gleftdtInterval = int(app.leftdtInterval)
            except:                
                gleftdtInterval = gDefaultleftdtInterval
                pass

        if leftlt == True:
            try:
                gleftltNoOfTimes = int(app.leftltNoOfTimes)                
            except:
                gleftltNoOfTimes = gDefaultleftltNoOfTimes                
            try:                
                gleftltInterval = int(app.leftltInterval)
            except:                
                gleftltInterval = gDefaultleftltInterval
                pass

        if rightst == True:
            ctctt = 2
            try:
                grightstNoOfTimes = int(app.rightstNoOfTimes)
            except:
                grightstNoOfTimes = gDefaultrightstNoOfTimes
            try:            
                grightstInterval = int(app.rightstInterval)
            except:                
                grightstInterval = gDefaultrightstInterval
                pass

        if rightdt == True:
            ctctt = 4
            try:
                grightdtNoOfTimes = int(app.rightdtNoOfTimes)
            except:
                grightdtNoOfTimes = gDefaultrightdtNoOfTimes                
            try:                
                grightdtInterval = int(app.rightdtInterval)
            except:                
                grightdtInterval = gDefaultrightdtInterval
                pass

        if rightlt == True:
            try:
                grightltNoOfTimes = int(app.rightltNoOfTimes)                
            except:
                grightltNoOfTimes = gDefaultrightltNoOfTimes                
            try:                
                grightltInterval = int(app.rightltInterval)
            except:                
                grightltInterval = gDefaultrightltInterval
                pass
        self.dialog.dismiss()
        
    def saveMpconfig(self,inst):
        global gCC_AnsEndNoOfTimes
        global gCC_RejectNoOfTimes        
        global gPC_PlayPauseNoOfTimes
        global gPC_NextPrevNoOfTimes
        global gPC_VolumeNoOfTimes
        
        global gDefaultCC_AnsEndNoOfTimes
        global gDefaultCC_RejectNoOfTimes        
        global gDefaultPC_PlayPauseNoOfTimes
        global gDefaultPC_NextPrevNoOfTimes
        global gDefaultPC_VolumeNoOfTimes
        global callcontrol
        global playcontrol
        
        app = MDApp.get_running_app()

        if callcontrol == True:
            try:
                gCC_AnsEndNoOfTimes = int(app.CallAns_EndNoOfTimes)                
            except:
                gCC_AnsEndNoOfTimes = gDefaultCC_AnsEndNoOfTimes
                
            try:                
                gCC_RejectNoOfTimes = int(app.CallRejectNoOfTimes)
            except:                
                gCC_RejectNoOfTimes = gDefaultCC_RejectNoOfTimes
                pass     
        
        if playcontrol == True:
            try:
                gPC_PlayPauseNoOfTimes = int(app.PlayControlPlayPauseNoOfTimes)                
            except:
                gPC_PlayPauseNoOfTimes = gDefaultPC_PlayPauseNoOfTimes
            
            try:
                gPC_NextPrevNoOfTimes = int(app.PlayControlNextPrevNoOfTimes)                
            except:
                gPC_NextPrevNoOfTimes = gDefaultPC_NextPrevNoOfTimes
                
            try:                
                gPC_VolumeNoOfTimes = int(app.PlayControlVolumeUpDownNoOfTimes)
            except:                
                gPC_VolumeNoOfTimes = gDefaultPC_VolumeNoOfTimes
                pass 
        self.dialog.dismiss()

    def doCtcTest(self):
        self.help_string.current = 'Test'
        self.help_string.get_screen('Test').ids.start.disabled = False
        
    def doMobilePhoneControlTest(self):
        self.help_string.current = 'Test'
        self.help_string.get_screen('Test').ids.start.disabled = False
                                
    def configration1(self):
        self.help_string.get_screen('Test').ids.CTCcheck.active = False
        self.help_string.current = 'Test'
    
    def configration2(self):
        self.help_string.get_screen('Test').ids.MPControlcheck.active = False
        self.help_string.current = 'Test'

    def AudioTestingconfigration(self):
        self.help_string.get_screen('Test').ids.start.disabled = False

    def BatteryLifeTestingconfigration(self):
        self.help_string.get_screen('Test').ids.start.disabled = False
        self.help_string.get_screen('Test').ids.stoptest.disabled = True
    
    #Dialog for taking input for RSSI test case
    def rssiconfigration(self):
        global checkRssi
        if checkRssi == True:
            self.dialog = MDDialog(
                title="Rssi Configuration:",
                type="custom",
                content_cls=RssiConfig(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL", text_color=self.theme_cls.primary_color, on_release=self.closeDialogBt
                    ),
                    MDFlatButton(
                        text="SUBMIT", text_color=self.theme_cls.primary_color, on_release=self.saveconfig
                    ),
                ],
            )
            self.dialog.open()
            
    #Dialog for taking input for Long hour test case    
    def LongHourconfigration(self):
        global checkLng
    
        if checkLng == True:
            self.dialog = MDDialog(
                title="Long Hour Configuration:",
                type="custom",
                content_cls=LnghrConfig(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL", text_color=self.theme_cls.primary_color, on_release=self.closeDialogLongHr
                    ),
                    MDFlatButton(
                        text="SUBMIT", text_color=self.theme_cls.primary_color, on_release=self.saveconfig
                    ),
                ],
            )
            self.dialog.open()
            
    #Dialog for taking input for Connectivity test case            
    def Connectivityconfigration(self):                                   
        global checkConnectivity
    
        if checkBT == True:
            self.dialog = MDDialog(
                title="Bluetooth Connectivity Configuration:",
                type="custom",
                content_cls=BtConfig(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL", text_color=self.theme_cls.primary_color, on_release=self.closeDialogBt
                    ),
                    MDFlatButton(
                        text="SUBMIT", text_color=self.theme_cls.primary_color, on_release=self.saveconfig
                    ),
                ],
            )
            self.dialog.open()        
    
    #Funciton for saving Long hour, Connectivity and RSSI test cases selections and their inputs
    def saveconfig(self,inst):    
        global checkLng
        global checkBT
        global checkRssi

        global Lngend
        global VolumeControl
        global Bttimes
        global BTpairtimes
        global RssiDuration
        
        global DefaultLngend
        global DefaultBttimes
        global DefaultBTpairtimes
        global DefaultRssiDuration
        
        app = MDApp.get_running_app()

        if checkLng == True:
            try:
                Lngend = int(app.Lnghr)
            except:
                Lngend = DefaultLngend
            try:
                VolumeControl = int(app.Lnghrvolume)                
            except:                
                VolumeControl = DefaultVolume                
            
            
        if checkBT == True:
            try:
                BTpairtimes = int(app.btpair)
            except:                
                BTpairtimes = DefaultBTpairtimes
                
            try:
                Bttimes=int(app.bt)
            except:
                Bttimes=DefaultBttimes
            
        if checkRssi == True:
            try:
                RssiDuration=int(app.rssiduration)               
            except:
                RssiDuration=DefaultRssiDuration
            
        self.dialog.dismiss()        
        self.help_string.get_screen('Test').ids.start.disabled = False
    
    def Start_vlc(self):
        global VolumeControl
        global PlayPauseStatus
        p = subprocess.Popen(['vlc', '/home/pi/Desktop/Golem/Test Song/sample.xspf'])
        time.sleep(5)
        for i in range(25):
            pyautogui.press('down') 

        time.sleep(2)                        
        for i in range(int(VolumeControl)//5):
            pyautogui.press('up')
        PlayPauseStatus = False
        

    def Stop_vlc(self):
        p = subprocess.Popen(['pkill', 'vlc'])
    
##################################################### Test Case ##########################################################################
    #@mainthread
    def GolemStartTest(self):
        global checkLng
        global checkBT
        global checkctc
        global checkAudioTesting
        global checkSpeakerTesting
        global checkBattery
        global checkRssi
        global checkMpTesting

        if checkLng == False and checkBT == False and checkctc == False and checkSpeakerTesting == False and checkAudioTesting == False and checkBattery == False and checkRssi == False and checkMpTesting == False:
            def show_alert_dialog(self):
                self.dialog = MDDialog(
                    text="Please select test case and then  click on start test")
                self.dialog.open()
            show_alert_dialog(self)
            def dia(dt):
                self.dialog.dismiss(force=True)
            Clock.schedule_once(dia, 3)
        else:
            global StopTesting
            StopTesting = False

            self.help_string.get_screen('Test').ids.stoptest.disabled = False
            self.help_string.get_screen('Test').ids.back.disabled = True
            self.help_string.get_screen('Test').ids.Clear.disabled = True

            self.help_string.get_screen('Test').ids.start.disabled = True
            self.help_string.get_screen('Test').ids.Lngcheck.disabled = True
            self.help_string.get_screen('Test').ids.rssicheck.disabled = True
            self.help_string.get_screen('Test').ids.AudioTestingcheck.disabled = True
            self.help_string.get_screen('Test').ids.MPControlcheck.disabled = True
            self.help_string.get_screen('Test').ids.Speakercheck.disabled = True
            self.help_string.get_screen('Test').ids.BatteryLifecheck.disabled = True
            self.help_string.get_screen('Test').ids.CTCcheck.disabled = True
            self.help_string.get_screen('Test').ids.ConnectivityCheck.disabled = True
            
            #Function for Executing all the test cases one by one in the below order based on selection
            #@mainthread
            def DoAllTests():
                global checkLng
                global checkBT
                global checkctc
                global checkAudioTesting
                global checkSpeakerTesting
                global checkBattery
                global checkRssi
                global Logtext
                global TestCaseSerialNumber
                global XlsName
                global LogFileName
                global checkMpTesting
                global MacAddress
                
                if checkSpeakerTesting == True:
                    #Speaker test starts here
                    def DoSpeakerTest():
                        global Logtext
                        global StopTesting
                        global speaker_test_ended
                        global TestCaseSerialNumber
                        global MacAddress
                        
                        speaker_test_ended = False
                        CurrentBatteryValue = GetBatteryPercentage(MacAddress)
                        
                        if StopTesting == True or CurrentBatteryValue < 60:
                            print('Not continuing DoSpeakerTest')
                            return
                        
                        self.Log("Speaker Test Started")
                        
                        SPEAKER_TEST_OUTPUT_FILENAME = "speaker_test_mic_recording.wav"
                        #Finding the RMS without Sound. This is the reference
                        empty_record = subprocess.Popen(['arecord', '-d', '10', '-f', 'S16_LE', '-r', '44100', 'empty_recording.wav'])
                        time.sleep(12)
                        empty_record.kill()
                        if StopTesting == True:
                            print('Not continuing DoSpeakerTest')
                            return
                        
                        with contextlib.closing(wave.open('empty_recording.wav','r')) as f1:

                            frames = f1.getnframes()
                            rate = f1.getframerate()
                            duration = frames / float(rate)
                            width = f1.getsampwidth()
                            print (width)
                            channel = f1.getnchannels()
                            size = width*channel
                            wav = f1.readframes(f1.getnframes())
                        MeasuredLoudness_No_audio = audioop.rms(wav, width)    
                        print(MeasuredLoudness_No_audio)
                        
                        #Function for recording the speaker output using MiniDSP Mic
                        def speaker_test_recording():
                            global speaker_test_ended
                            s_record = subprocess.Popen(['arecord', '-d', '10', '-f', 'S16_LE', '-r', '44100', 'speaker_test_mic_recording.wav'])
                            while (True):
                                if StopTesting == True :
                                    s_record.kill()
                                    return
                                if speaker_test_ended == True :
                                    break                            
                            s_record.kill()
                        
                        #Function for playing sound only in Left channel
                        def Left_speaker_test_play_sound():
                            global speaker_test_ended
                            Left_play = subprocess.Popen(['aplay','Left_Channel.wav'])
                            while (True):
                                if StopTesting == True :
                                    Left_play.kill()
                                    return
                                if speaker_test_ended == True :
                                    break
                            Left_play.kill()
                            
                        #Function for playing sound only in Right channel
                        def Right_speaker_test_play_sound():
                            global speaker_test_ended
                            Right_play = subprocess.Popen(['aplay','Right_Channel.wav'])
                            while (True):
                                if StopTesting == True :
                                    Right_play.kill()
                                    return
                                if speaker_test_ended == True :
                                    break
                            Right_play.kill()
                        
                        #Left Speaker Test starts
                        t1 = threading.Thread(target = speaker_test_recording)
                        t2 = threading.Thread(target = Left_speaker_test_play_sound)
                        t1.start()
                        t2.start()
                        time.sleep(12)
                        with contextlib.closing(wave.open(SPEAKER_TEST_OUTPUT_FILENAME,'r')) as f:

                            frames = f.getnframes()
                            rate = f.getframerate()
                            duration = frames / float(rate)
                            width = f.getsampwidth()
                            print (width)
                            channel = f.getnchannels()
                            size = width*channel
                            wav = f.readframes(f.getnframes())
                        Left_MeasuredLoudness = audioop.rms(wav, width)    
                        print(Left_MeasuredLoudness)
                        if StopTesting == True:
                            print('Not continuing DoSpeakerTest')
                            return
                        else:
                            self.WriteXls(0,1,str(TestCaseSerialNumber),1)
                            TestCaseSerialNumber += 1
                            self.WriteXls(-1,2,'Speaker Test',2)                            
                            message = 'Loudness @ Left - ' + str(Left_MeasuredLoudness)
                            self.WriteXls(-1,3,message,2)
                            
                            if (Left_MeasuredLoudness - MeasuredLoudness_No_audio)  > 100:
                                self.WriteXls(-1,5,'Pass',4)
                                message = "Left Speaker : PASS"
                                self.Log(message)
                                message = "Left Speaker Measured Loudness : " + str(Left_MeasuredLoudness)
                                self.Log(message)
                            else:
                                self.WriteXls(-1,5,'Fail',5)
                                message = "Left Speaker : FAIL"
                                self.Log(message)
                                message = "Left Speaker Measured Loudness : " + str(Left_MeasuredLoudness)
                                self.Log(message)
                            print('Left Speaker test done')
                            self.WriteXls(-1,4,'Loudness - NoAudio > 100',1)
                        #Right speaker test starts
                        t1 = threading.Thread(target = speaker_test_recording)
                        t2 = threading.Thread(target = Right_speaker_test_play_sound)
                        t1.start()
                        t2.start()
                        time.sleep(12)
                        with contextlib.closing(wave.open(SPEAKER_TEST_OUTPUT_FILENAME,'r')) as f:

                            frames = f.getnframes()
                            rate = f.getframerate()
                            duration = frames / float(rate)
                            width = f.getsampwidth()
                            print (width)
                            channel = f.getnchannels()
                            size = width*channel
                            wav = f.readframes(f.getnframes())
                        Right_MeasuredLoudness = audioop.rms(wav, width)    
                        print(Right_MeasuredLoudness)
                        
                        if StopTesting == True:
                            print('Not continuing DoSpeakerTest')
                            return
                        else:
                            message = 'Loudness @ Right - ' + str(Right_MeasuredLoudness)                            
                            self.WriteXls(0,3,message,1)
                            if (Right_MeasuredLoudness - MeasuredLoudness_No_audio)  > 100:
                                self.WriteXls(-1,5,'Pass',4)
                                message = "Right Speaker : PASS"
                                self.Log(message)
                                message = "Right Speaker Measured Loudness : " + str(Right_MeasuredLoudness)
                                self.Log(message)
                            else:
                                self.WriteXls(-1,5,'Fail',5)
                                message = "Right Speaker : FAIL"
                                self.Log(message)
                                message = "Right Speaker Measured Loudness : " + str(Right_MeasuredLoudness)
                                self.Log(message)
                            self.WriteXls(-1,4,'Loudness - NoAudio > 100',1)
                            print('Right Speaker test done')
                            speaker_test_ended = True                        
                        self.Log("Speaker testing is done")                    
                    DoSpeakerTest()

                if checkctc == True:
                    #CTC Test starts Here
                    def DoCTCTest():
                        global Logtext
                        global StopTesting
                        global MacAddress
                        
                        CurrentBatteryValue = GetBatteryPercentage(MacAddress)
                        if StopTesting == True or IsHeadPhoneDevice == True or CurrentBatteryValue < 60:
                            print('Not continuing DoCTCTest')
                            return                    
                        self.Log("CTC Test Started")                         
                        global gleftstNoOfTimes
                        global gleftstInterval
                        global gleftdtNoOfTimes
                        global gleftdtInterval
                        global gleftltNoOfTimes
                        global gleftltInterval

                        global grightstNoOfTimes
                        global grightstInterval
                        global grightdtNoOfTimes
                        global grightdtInterval
                        global grightltNoOfTimes
                        global grightltInterval
                        global ctctt
                        global tapdflag

                        global Measuredrightst
                        global Measuredrightdt
                        global Measuredrightlt

                        global Measuredleftst
                        global Measuredleftdt
                        global Measuredleftlt
                        global TestCaseSerialNumber
                        
                        global ctc_test_ended
                        ctc_test_ended = False
                        
                        Measuredrightst = int(0)
                        Measuredrightdt = int(0)
                        Measuredrightlt = int(0)
                        Measuredleftst = int(0)
                        Measuredleftdt = int(0)
                        Measuredleftlt = int(0)
                        
                        sum_ctc_inputs = 0
                        sum_measured_ctc_responses = 0

                        ServoNotConnected = False
                        try:
                            kit = ServoKit(channels=16)
                            Right_Motor = 0
                            Left_Motor = 15
                            
                            Right_Motor_Initial_Angle = 45
                            Left_Motor_Initial_Angle = 120
        
                            #Initial positions of Servomotors 
                            kit.servo[Right_Motor].angle = Right_Motor_Initial_Angle
                            kit.servo[Left_Motor].angle = Left_Motor_Initial_Angle
                        except :
                            ServoNotConnected = True
                        
                        
                        
                        def playvideo():
                            global ctc_test_ended
                            global StopTesting
                            
                            p = subprocess.Popen(['vlc', '/home/pi/Desktop/Golem/Test Song/sample.xspf'])
                            while (True):
                                time.sleep(3)
                                result = DeviceStatusbyMacAddress(1,MacAddress);
                                if result == False:
                                    StopTesting = True
                                    
                                if StopTesting == True :
                                    p.kill()
                                    return
                                if ctc_test_ended == True :
                                    return
                        
                        
                        t1 = threading.Thread(target = playvideo)
                        t2 = threading.Thread(target = self.stetaupdate)
                        
                        t1.start()
                        time.sleep(3)
                        t2.start()
                        
                        if ServoNotConnected == False:
                            TouchTestPass = True
                            self.WriteXls(0,1,str(TestCaseSerialNumber),1)
                            TestCaseSerialNumber += 1
                            self.WriteXls(-1,2,'CTC',2)
                            self.WriteXls(-1,3,'Input/Observed',2)                                                    
                            
                            ctctt = 0
                            #Function for Left Motor control for Single tap
                            if leftst == True and StopTesting == False:                           
                                ctctt = 1
                                temp = 1
                                self.Log("Left Single Tap in progress")
                                for i in range(gleftstNoOfTimes):
                                    print("Left Single Tap No : ", i + 1)
                                    kit.servo[Left_Motor].angle = Left_Motor_Initial_Angle -35
                                    time.sleep(0.25)
                                    kit.servo[Left_Motor].angle = Left_Motor_Initial_Angle
                                    time.sleep(gleftstInterval)
                                    if StopTesting == True:
                                        kit.servo[Left_Motor].angle = Left_Motor_Initial_Angle
                                        self.Log("CTC test interrupted")
                                        break
                                kit.servo[Left_Motor].angle = Left_Motor_Initial_Angle
                                self.Log("Left Single tap completed")
                                
                                message = "Left Single  " + str(gleftstNoOfTimes) + "  " + str(Measuredleftst)
                                sum_ctc_inputs = sum_ctc_inputs + i + 1
                                sum_measured_ctc_responses = sum_measured_ctc_responses + Measuredleftst                            
                                self.WriteXls(0,2,'Left Single Tap',1)
                                message = 'Input - ' + str(gleftstNoOfTimes) + "/ Observed - " + str(Measuredleftst)
                                self.WriteXls(-1,3,message,1)
                                
                                if (gleftstNoOfTimes != Measuredleftst) :
                                    TouchTestPass = False
                                self.Log(message)
                            
                            
                            ctctt = 0
                            #Function for Left Motor control for Double tap
                            if leftdt == True and StopTesting == False:
                                ctctt = 3
                                temp = 3
                                self.Log("Left Double Tap in progress")
                                for i in range(gleftdtNoOfTimes):
                                    print("Left Double Tap No : ", i + 1)                                   
                                    
                                    kit.servo[Left_Motor].angle = Left_Motor_Initial_Angle -35
                                    time.sleep(0.15)
                                    kit.servo[Left_Motor].angle = Left_Motor_Initial_Angle
                                    time.sleep(0.15)
                                    kit.servo[Left_Motor].angle = Left_Motor_Initial_Angle -35
                                    time.sleep(0.15)
                                    kit.servo[Left_Motor].angle = Left_Motor_Initial_Angle
                                    time.sleep(gleftdtInterval)
                                    if StopTesting == True:
                                        kit.servo[Left_Motor].angle = Left_Motor_Initial_Angle
                                        self.Log("CTC test interrupted")
                                        break
                                    
                                kit.servo[Left_Motor].angle = Left_Motor_Initial_Angle
                                self.Log("Left Double tap completed")
                                
                                message = "Left Double  " + str(gleftdtNoOfTimes) +  "  " + str(Measuredleftdt)
                                sum_ctc_inputs = sum_ctc_inputs + i+1
                                sum_measured_ctc_responses = sum_measured_ctc_responses + Measuredleftdt
                                self.WriteXls(0,2,'Left Double Tap',1)
                                message = 'Input - ' + str(gleftdtNoOfTimes) + '/ Observed - ' + str(Measuredleftdt)
                                self.WriteXls(-1,3,message,1)                                                     
                                
                                if gleftdtNoOfTimes != Measuredleftdt : 
                                    TouchTestPass = False
                                self.Log(message)
                            
                                
                            ctctt = 0
                            #Function for Right Motor control for Single tap
                            if rightst == True and StopTesting == False:
                                ctctt = 2
                                temp = 2
                                self.Log("Right Single Tap in progress")
                                for i in range(grightstNoOfTimes):
                                    print("Right Single Tap No : ", i + 1)
                                    kit.servo[Right_Motor].angle = Right_Motor_Initial_Angle + 35
                                    time.sleep(0.25)
                                    kit.servo[Right_Motor].angle = Right_Motor_Initial_Angle
                                    time.sleep(grightstInterval)
                                    if StopTesting == True:
                                        kit.servo[Right_Motor].angle = Right_Motor_Initial_Angle
                                        self.Log("CTC test interrupted")
                                        break
                                    
                                kit.servo[Right_Motor].angle = Right_Motor_Initial_Angle
                                self.Log("Right Single tap completed")
                                
                                message = "Right Single  " + str(grightstNoOfTimes) +  "  " + str(Measuredrightst)
                                sum_measured_ctc_responses = sum_measured_ctc_responses + Measuredrightst
                                sum_ctc_inputs = sum_ctc_inputs + i+1
                                
                                self.WriteXls(0,2,'Right Single Tap',1)
                                message = 'Input - ' + str(grightstNoOfTimes) + '/ Observed - ' + str(Measuredrightst)
                                self.WriteXls(-1,3,message,1)                                
                                               
                                
                                if (grightstNoOfTimes != Measuredrightst) :
                                    TouchTestPass = False
                                self.Log(message)
                            
                            ctctt = 0
                            #Function for Right Motor control for Double tap
                            if rightdt == True and StopTesting == False:
                                ctctt = 4
                                temp = 4
                                self.Log("Right Double Tap in progress")
                                for i in range(grightdtNoOfTimes):
                                    print("Right Double Tap No : ", i + 1)                                    
                                    
                                    kit.servo[Right_Motor].angle = Right_Motor_Initial_Angle + 35
                                    time.sleep(0.15)
                                    kit.servo[Right_Motor].angle = Right_Motor_Initial_Angle
                                    time.sleep(0.15)
                                    kit.servo[Right_Motor].angle = Right_Motor_Initial_Angle + 35
                                    time.sleep(0.15)
                                    kit.servo[Right_Motor].angle = Right_Motor_Initial_Angle
                                    time.sleep(grightdtInterval)
                                    if StopTesting == True:
                                        kit.servo[Right_Motor].angle = Right_Motor_Initial_Angle
                                        self.Log("CTC test interrupted")
                                        break
                                kit.servo[Right_Motor].angle = Right_Motor_Initial_Angle
                                self.Log("Right Double tap completed")
                                
                                message = "Right Double  " + str(grightdtNoOfTimes) +  "  " + str(Measuredrightdt)
                                sum_ctc_inputs = sum_ctc_inputs + i + 1
                                sum_measured_ctc_responses = sum_measured_ctc_responses + Measuredrightdt
                                
                                self.WriteXls(0,2,'Right Double Tap',1)
                                message = 'Input - ' + str(grightdtNoOfTimes) + '/ Observed - ' + str(Measuredrightdt)
                                self.WriteXls(-1,3,message,1)                                
                                
                                if grightdtNoOfTimes != Measuredrightdt :
                                    TouchTestPass = False
                                
                                self.Log(message)
                               
                            ctctt = 0     
                            if leftlt == True:
                                ctctt = 1
                                temp = 5
                                                                
                            ctctt = 0 
                            if rightlt == True:
                                ctctt = 2
                                temp = 6
                        else :
                            time.sleep(30)
                        
                        self.Log("CTC testing is done")
                        self.Log("Touch Entered Measured")
                        ctc_test_ended = True
                        
                        time.sleep(2)
                        p = subprocess.Popen(['pkill', 'vlc'])
                        p.communicate()
                                                
                        #Calculating the accuracy of CTC Test
                        if sum_ctc_inputs != 0:
                            ctc_accuracy = (sum_measured_ctc_responses / sum_ctc_inputs) * 100
                            message = "CTC Accuracy: " + str(ctc_accuracy) + "%"
                            self.Log(message)
                            if (ctc_accuracy >= 95):
                                TouchTestPass = True
                                self.Log("CTC Test - PASS")
                                self.WriteXls(0,5,'Pass',4)
                            else:
                                TouchTestPass = False
                                self.Log("CTC Test - FAIL")
                                self.WriteXls(0,5,'Fail',5)
                        else :
                            self.Log("CTC Test - FAIL")
                            self.WriteXls(0,5,'Fail',5)
                        
                        self.WriteXls(-1,4,'ctc_accuracy >= 95',1)
                    DoCTCTest()
                                                        
                if checkAudioTesting == True:
                    def DoAudioTest():
                        global Logtext
                        global StopTesting
                        global TestCaseSerialNumber
                        global MacAddress
                        
                        CurrentBatteryValue = GetBatteryPercentage(MacAddress)
                        
                        print('Mic Testing - It has not been supported')
                        return

                        if StopTesting == True or CurrentBatteryValue < 60:
                            print('Not continuing DoAudioTest')
                            return

                        def np_audioop_rms(data, width):
                            """audioop.rms() using numpy; avoids another dependency for app"""
                            if len(data) == 0: return None
                            fromType = (np.int8, np.int16, np.int32)[width//2]
                            d = np.frombuffer(data, fromType).astype(np.float)
                            rms = np.sqrt( np.mean(d**2) )
                            return int( rms )
                        
                        WAVE_OUTPUT_FILENAME = "output.wav"
                        global rf
                        global frames1

                        def recording(side):
                            p_record = subprocess.Popen(['arecord', '-d', '10', 'output.wav'])
                            p_record.communicate()
                            print("Mic Recording Done")
                            p_record.kill()
                        
                        def play_sound():
                            p_play = subprocess.Popen(['aplay', '-D', 'hw:0,0,0','input.wav'])
                            p_play.communicate()
                            print("Playing Done")
                            p_play.kill()
                        
                        command_sound_cards = "pacmd list-cards | grep -e 'index:' -e 'device.string'"
                        p_find_sound_card_index = subprocess.Popen(command_sound_cards, stdout=subprocess.PIPE, shell = True)
                        sound_cards_token_list = []
                        
                        Mac_Address_for_finding_index = '"' + MacAddress + '"'
                        flag = int(0)
                        
                        for line in p_find_sound_card_index.stdout:
                            card_index = str(line, 'UTF-8')
                            print(card_index)
                            for i in card_index.split():
                                sound_cards_token_list.append(i)       
                        print (sound_cards_token_list)
                        
                        for token_list_index in sound_cards_token_list:
                            flag = flag + 1
                            if token_list_index == Mac_Address_for_finding_index:
                                print("Device Found for setting default Mic")
                                break
                        sound_card_index = int(sound_cards_token_list[flag -4])
                        print(sound_card_index)
                        
                        cmd = "pacmd set-card-profile" + " "+ str(sound_card_index) + " " + "headset_head_unit"
                        print(cmd)
                        p_set_default_BT_sound_card = subprocess.Popen(cmd, shell=True)
                        print("Default mic setting is done")
                        t1 = threading.Thread(target = recording, args=("RIGHT",))
                        t2 = threading.Thread(target = play_sound)
                        t1.start()
                        t2.start()
                        
                        with contextlib.closing(wave.open(WAVE_OUTPUT_FILENAME,'r')) as f:

                            frames = f.getnframes()
                            rate = f.getframerate()
                            duration = frames / float(rate)
                            width = f.getsampwidth()
                            channel = f.getnchannels()
                            size = width*channel
                            wav = f.readframes(f.getnframes())
                        MeasuredLoudness = audioop.rms(wav, 2)
                        print(MeasuredLoudness)
                        
                        if MeasuredLoudness> 100:
                            message = "Mic is in good condition, Measured Loudness : " + str(MeasuredLoudness)
                        else:
                            message = "Mic is NOT in good condition, Measured Loudness : " + str(MeasuredLoudness)
                        
                        self.Log("Mic testing is done")
                        self.Log(message)         
                        
                    DoAudioTest()
                if checkBattery == True:
                    def DoBatteryTest():
                        global StopTesting
                        global Logtext
                        global TestCaseSerialNumber
                        global s
                        
                        print('DoBatteryTest - It has not been supported')
                        return
                        
                        if StopTesting == True:
                            print('Not continuing DoBatteryTest')
                            return                        
                        
                        self.Log("Battery Test Started")
                        
                        BatteryValueBefore = GetBatteryPercentage(MacAddress)
                        print(BatteryValueBefore)                                                       
                        
                                
                        p = subprocess.Popen(['vlc','/home/pi/Desktop/Golem/Test Song/sample.xspf'])
                        time.sleep(5)
                        for i in range(25):
                            pyautogui.press('down') 

                        time.sleep(2)
                        
                        for i in range(20):
                            pyautogui.press('up')
                            
                        start = time.time() 
                                
                        while 1:                            
                            result = DeviceStatusbyMacAddress(1,MacAddress);
                            if result == False:
                                self.Log("Battery Test - FAIL")                                                                
                                break
                                
                            time.sleep(3)
                            if StopTesting == True:
                                self.Log("Battery Test - Interrupted") 
                                break
                            end = time.time()
                            hours, rem = divmod(end-start, 3600)
                            minutes, seconds = divmod(rem, 60)                            
                            hours1, minutes1 = divmod(Lngend, 60)
                            
                             #Play for 5 min
                            if int(minutes) == 5:
                                self.Log("Playback for 5min is completed") 
                                break
                            
                        p = subprocess.Popen(['pkill', 'vlc'])         
                                
                        BatteryValueAfter = GetBatteryPercentage(MacAddress)
                        print(BatteryValueAfter)
                        if s != None:
                            s.close()
                            s = None
                        
                        self.Log("Before : " + str(BatteryValueBefore) + "%" )
                        self.Log("After : " + str(BatteryValueAfter) + "%" )
                        total_discharge = BatteryValueAfter - BatteryValueBefore
                        self.Log("Total Discharge in 5min : " + str(total_discharge) + "%" )
                              
                        if BatteryValueAfter < (BatteryValueBefore - 10 ) :
                            self.Log("Battery life test - FAIL")
                        else :                            
                            self.Log("Battery life test - PASS")
                        self.Log("Battery life test is done")
                            
                    DoBatteryTest()
                    
                if checkBT == True:
                    def DoConnectivityTest():
                        global StopTesting
                        global Logtext
                        global TestCaseSerialNumber
                        if StopTesting == True:
                            print('Not continuing DoConnectivityTest')
                            return
                        
                        self.Log("Connectivity Test Started")
                        
                        PairedTimes = 0
                        UnPairedTimes = 0
                        self.Log("Pairing/Unpairing test in progress")
                        
                        self.WriteXls(0,1,str(TestCaseSerialNumber),1)
                        TestCaseSerialNumber += 1
                        self.WriteXls(-1,2,'Connectivity',2)
                        self.WriteXls(-1,3,'Input/Actual/Number Of Retries',2)                        
                        TotalNumberOfRetries = 0
                        
                        for i in range(BTpairtimes):
                            if StopTesting == True:
                                break
                            self.Log("Pairing Test InProgress: " + str(i+1) )
                            
                            RetryCount = 0
                            while RetryCount < 3:
                                result = DeviceUnPairbyMacAddress(MacAddress)
                                if result == False:
                                    break
                                self.Log("Retrying - Unpair")
                                RetryCount += 1  
                                TotalNumberOfRetries += 1                                
                            
                            if RetryCount == 3 :
                                StopTesting = True
                            
                            if result == False:
                                UnPairedTimes = UnPairedTimes + 1
                                self.Log("Pairing Test InProgress - UnPaired: " + str(UnPairedTimes) )
                                for j in range(5):
                                    time.sleep(1)
                                    if StopTesting == True:
                                        break
                                
                                RetryCount = 0
                                while RetryCount < 3:
                                    result = DeviceConnectbyMacAddress(2,MacAddress,True)
                                    if result == True:
                                        break
                                    RetryCount += 1
                                    TotalNumberOfRetries += 1
                                    self.Log("Retrying - pair")
                                
                                if RetryCount == 3 :
                                    StopTesting = True
                                
                                if result == True:
                                    PairedTimes = PairedTimes + 1
                                    self.Log("Pairing Test InProgress - Paired: " + str(PairedTimes) )
                                    for j in range(5):
                                        time.sleep(1)
                                        if StopTesting == True:
                                            break
                            else :
                                break
                        self.Log("Pairing/Unpairing test completed")
                        self.Log("Paired Times: " + str(PairedTimes) )
                        self.Log("UnPaired Times: " + str(UnPairedTimes) )
                        
                        message = 'Input - ' + str(BTpairtimes) + "/ Paired Times - " + str(PairedTimes)  + ", UnPaired Times - " +  str(UnPairedTimes) + " / Retry -" + str(TotalNumberOfRetries) 
                        
                        self.WriteXls(0,2,'Pair & UnPair',1)                        
                        self.WriteXls(-1,3,message,1)                        
                        
                        if (PairedTimes+1) >= UnPairedTimes and TotalNumberOfRetries < 10:
                            self.Log("Pairing Test: PASS")
                            self.WriteXls(-1,5,'Pass',4)
                            self.Log("Connectivity/Disconnectivity test in progress")
                        else :
                            StopTesting = True
                            self.WriteXls(-1,5,'Fail',5)
                            self.Log("Pairing Test: FAIL")
                            
                        self.WriteXls(-1,4,'Paired = UnPaired & NumberOfRetry < 10',1)    
                        
                        TotalNumberOfRetries = 0
                        ConnectedTimes = 0
                        DisConnectedTimes = 0                        
                        for i in range(Bttimes):
                            if StopTesting == True:
                                break
                            
                            self.Log("Connectivity Test InProgress: " + str(i+1) )
                            
                            RetryCount = 0
                            while RetryCount < 3:
                                result = DeviceDisConnectbyMacAddress(1,MacAddress)
                                if result == False:
                                    break
                                RetryCount += 1 
                                TotalNumberOfRetries += 1
                                self.Log("Retrying - Disconnect")
                            
                            if RetryCount == 3 :
                                StopTesting = True
                            
                            if result == False:
                                DisConnectedTimes = DisConnectedTimes + 1
                                self.Log("Connectivity Test InProgress - DisConnected: " + str(DisConnectedTimes) )
                                
                                for j in range(5):
                                    time.sleep(1)
                                    if StopTesting == True:
                                        break
                                
                                RetryCount = 0
                                while RetryCount < 3:
                                    result = DeviceConnectbyMacAddress(1,MacAddress,True)
                                    if result == True:
                                        break
                                    RetryCount += 1
                                    TotalNumberOfRetries += 1
                                    self.Log("Retrying - Connect")
                                                                    
                                if RetryCount == 3 :
                                    StopTesting = True
                                
                                if result == True:
                                    ConnectedTimes = ConnectedTimes + 1
                                    self.Log("Connectivity Test InProgress - Connected: " + str(ConnectedTimes) )
                                    for j in range(5):
                                        time.sleep(1)
                                        if StopTesting == True:
                                            break
                            else :
                                break
                        self.Log("Connectivity/Disconnectivity test completed")
                        self.Log("Connected Times: " + str(ConnectedTimes) )
                        self.Log("DisConnected Times: " + str(DisConnectedTimes) )
                        
                        message = 'Input - ' + str(Bttimes) + "/ Connected -" + str(ConnectedTimes)  + ", Disconnected - " +  str(DisConnectedTimes) + " / Retry -" + str(TotalNumberOfRetries)  
                        
                        self.WriteXls(0,2,'Connect & DisConnect',1)                        
                        self.WriteXls(-1,3,message,1)                        
                        
                        
                        if (ConnectedTimes+1) >= DisConnectedTimes and TotalNumberOfRetries < 10:
                            self.Log("Connectivity Test: PASS")
                            self.WriteXls(-1,5,'Pass',4)
                        else :
                            StopTesting = True
                            self.Log("Connectivity Test: FAIL")
                            self.WriteXls(-1,5,'Fail',5)
                            
                        self.WriteXls(-1,4,'Connected = Disconnected & NumberOfRetry < 10',1)    
                        self.Log("Connectivity testing is done")
                        
                    DoConnectivityTest()
                    
                if checkMpTesting == True:
                    def DoMobilePhoneControlTest():
                        global StopTesting
                        global Logtext
                        global TestCaseSerialNumber
                        global MacAddress
                        
                        CurrentBatteryValue = GetBatteryPercentage(MacAddress)
                        
                        if StopTesting == True or IsHeadPhoneDevice == True or CurrentBatteryValue < 60:
                            print('Not continuing Mobile Phone Control Test')
                            return
                        
                        global gCC_AnsEndNoOfTimes
                        global gCC_RejectNoOfTimes        
                        global gPC_PlayPauseNoOfTimes
                        global gPC_NextPrevNoOfTimes
                        global gPC_VolumeNoOfTimes
                        global Device_Name                        
                        global callcontrol
                        global playcontrol
                        
                        global NumberOfAnsCallDetected
                        global NumberOfEndCallDetected
                        global NumberOfRejectCallDetected
                        
                        global gNumberOfPlayDetectedInADB_Control
                        global gNumberOfPauseDetectedInADB_Control
                        global gNumberOfNextDetectedInADB_Control
                        global gNumberOfPrevDetectedInADB_Control

                        global gNumberOfPlayDetectedInCTC_Control
                        global gNumberOfPauseDetectedInCTC_Control
                        global gNumberOfNextDetectedInCTC_Control
                        global gNumberOfPrevDetectedInCTC_Control
                        
                        if callcontrol == True or playcontrol == True :
                            self.Log("MobilePhone Control Test Started")
                            
                            self.WriteXls(0,1,str(TestCaseSerialNumber),1)
                            TestCaseSerialNumber += 1
                            self.WriteXls(-1,2,'Mobile Phone Control',1)
                            self.WriteXls(-1,3,'Times/Actual/Observed',1)                            
                            
                            result = DeviceDisConnectbyMacAddress(1,MacAddress)
                            
                            SetUpIssue = DeviceControlMobilePhone(Device_Name, MacAddress)
                            
                            if SetUpIssue == True:
                                self.Log("MobilePhone Control Test SetUp issue")                                
                                result = DeviceConnectbyMacAddress(1,MacAddress,True)                                
                            else : 
                                time.sleep(30)
                                
                                result = DeviceConnectbyMacAddress(1,MacAddress,True)
                                self.Log("MobilePhone Control Test Completed")
                                
                                if playcontrol == True :
                                    self.WriteXls(0,2,'PlayerControl',1)
                                    
                                    self.WriteXls(0,2,'Play Control - ADB',1)
                                    message = "Input - " + str(gPC_PlayPauseNoOfTimes) + "/ Observed - " + str(gNumberOfPlayDetectedInADB_Control)                                    
                                    self.WriteXls(-1,3,message,1)                                                                    
                                    
                                    self.Log('NumberOfPlayControl - Done' + str(gPC_PlayPauseNoOfTimes))
                                    self.Log('NumberOfPlayControl - Observed' + str(gNumberOfPlayDetectedInADB_Control))
                                    
                                    if gPC_PlayPauseNoOfTimes == gNumberOfPlayDetectedInADB_Control :
                                        self.WriteXls(-1,5,'Pass',4)
                                        self.Log('PlayerControl - Play Control Pass')
                                    else : 
                                        self.WriteXls(-1,5,'Fail',5)
                                        self.Log('PlayerControl - Play Control Fail')
                                        
                                    self.WriteXls(0,2,'Pause Control - ADB',1)
                                    message = "Input - " + str(gPC_PlayPauseNoOfTimes) + "/ Observed - " + str(gNumberOfPauseDetectedInADB_Control)                                    
                                    self.WriteXls(-1,3,message,1)                                                                    
                                    
                                    self.Log('NumberOfPauseControl - Done' + str(gPC_PlayPauseNoOfTimes))
                                    self.Log('NumberOfPauseControl - Observed' + str(gNumberOfPauseDetectedInADB_Control))
                                    
                                    if gPC_PlayPauseNoOfTimes == gNumberOfPauseDetectedInADB_Control :
                                        self.WriteXls(-1,5,'Pass',4)
                                        self.Log('PlayerControl - Pause Control Pass')
                                    else : 
                                        self.WriteXls(-1,5,'Fail',5)
                                        self.Log('PlayerControl - Pause Control Fail')
                                    
                                    self.WriteXls(0,2,'Next Control - ADB',1)
                                    message = "Input - " + str(gPC_NextPrevNoOfTimes) + "/ Observed - " + str(gNumberOfNextDetectedInADB_Control)                                    
                                    self.WriteXls(-1,3,message,1)                                                                    
                                    
                                    self.Log('NumberOfNextControl - Done' + str(gPC_NextPrevNoOfTimes))
                                    self.Log('NumberOfNextControl - Observed' + str(gNumberOfNextDetectedInADB_Control))
                                    
                                    if gPC_NextPrevNoOfTimes == gNumberOfNextDetectedInADB_Control :
                                        self.WriteXls(-1,5,'Pass',4)
                                        self.Log('PlayerControl - Next Control Pass')
                                    else : 
                                        self.WriteXls(-1,5,'Fail',5)
                                        self.Log('PlayerControl - Next Control Fail')
                                    
                                    self.WriteXls(0,2,'Previous Control - ADB',1)
                                    message = "Input - " + str(gPC_NextPrevNoOfTimes) + "/ Observed - " + str(gNumberOfPrevDetectedInADB_Control)                                    
                                    self.WriteXls(-1,3,message,1)                                                                    
                                    
                                    self.Log('NumberOfPreviousControl - Done' + str(gPC_NextPrevNoOfTimes))
                                    self.Log('NumberOfPreviousControl - Observed' + str(gNumberOfPrevDetectedInADB_Control))
                                    
                                    if gPC_NextPrevNoOfTimes == gNumberOfPrevDetectedInADB_Control :
                                        self.WriteXls(-1,5,'Pass',4)
                                        self.Log('PlayerControl - Previous Control Pass')
                                    else : 
                                        self.WriteXls(-1,5,'Fail',5)
                                        self.Log('PlayerControl - Previous Control Fail')
                                        
                                    self.WriteXls(0,2,'Play Control - CTC',1)
                                    message = "Input - " + str(gPC_PlayPauseNoOfTimes) + "/ Observed - " + str(gNumberOfPlayDetectedInCTC_Control)                                    
                                    self.WriteXls(-1,3,message,1)                                                                    
                                    
                                    self.Log('NumberOfPlayControl - Done' + str(gPC_PlayPauseNoOfTimes))
                                    self.Log('NumberOfPlayControl - Observed' + str(gNumberOfPlayDetectedInCTC_Control))
                                    
                                    if gPC_PlayPauseNoOfTimes == gNumberOfPlayDetectedInCTC_Control :
                                        self.WriteXls(-1,5,'Pass',4)
                                        self.Log('PlayerControl - Play Control Pass')
                                    else : 
                                        self.WriteXls(-1,5,'Fail',5)
                                        self.Log('PlayerControl - Play Control Fail')
                                        
                                    self.WriteXls(0,2,'Pause Control - CTC',1)
                                    message = "Input - " + str(gPC_PlayPauseNoOfTimes) + "/ Observed - " + str(gNumberOfPauseDetectedInCTC_Control)                                    
                                    self.WriteXls(-1,3,message,1)                                                                    
                                    
                                    self.Log('NumberOfPauseControl - Done' + str(gPC_PlayPauseNoOfTimes))
                                    self.Log('NumberOfPauseControl - Observed' + str(gNumberOfPauseDetectedInCTC_Control))
                                    
                                    if gPC_PlayPauseNoOfTimes == gNumberOfPauseDetectedInCTC_Control :
                                        self.WriteXls(-1,5,'Pass',4)
                                        self.Log('PlayerControl - Pause Control Pass')
                                    else : 
                                        self.WriteXls(-1,5,'Fail',5)
                                        self.Log('PlayerControl - Pause Control Fail')
                                    
                                    self.WriteXls(0,2,'Next Control - CTC',1)
                                    message = "Input - " + str(gPC_NextPrevNoOfTimes) + "/ Observed - " + str(gNumberOfNextDetectedInCTC_Control)                                    
                                    self.WriteXls(-1,3,message,1)                                                                    
                                    
                                    self.Log('NumberOfNextControl - Done' + str(gPC_NextPrevNoOfTimes))
                                    self.Log('NumberOfNextControl - Observed' + str(gNumberOfNextDetectedInCTC_Control))
                                    
                                    if gPC_NextPrevNoOfTimes == gNumberOfNextDetectedInCTC_Control :
                                        self.WriteXls(-1,5,'Pass',4)
                                        self.Log('PlayerControl - Next Control Pass')
                                    else : 
                                        self.WriteXls(-1,5,'Fail',5)
                                        self.Log('PlayerControl - Next Control Fail')
                                    
                                    self.WriteXls(0,2,'Previous Control - CTC',1)
                                    message = "Input - " + str(gPC_NextPrevNoOfTimes) + "/ Observed - " + str(gNumberOfPrevDetectedInCTC_Control)                                    
                                    self.WriteXls(-1,3,message,1)                                                                    
                                    
                                    self.Log('NumberOfPreviousControl - Done' + str(gPC_NextPrevNoOfTimes))
                                    self.Log('NumberOfPreviousControl - Observed' + str(gNumberOfPrevDetectedInCTC_Control))
                                    
                                    if gPC_NextPrevNoOfTimes == gNumberOfPrevDetectedInCTC_Control :
                                        self.WriteXls(-1,5,'Pass',4)
                                        self.Log('PlayerControl - Previous Control Pass')
                                    else : 
                                        self.WriteXls(-1,5,'Fail',5)
                                        self.Log('PlayerControl - Previous Control Fail')
                                    
                                
                                if callcontrol == True :
                                    self.WriteXls(0,2,'CallControl',1)
                                    
                                    self.WriteXls(0,2,'Ans Control',1)
                                    message = "Input - " + str(gCC_AnsEndNoOfTimes) + "/ Observed - " + str(NumberOfAnsCallDetected)                                    
                                    self.WriteXls(-1,3,message,1)                                                                    
                                    
                                    self.Log('NumberOfAnsCall - Done' + str(gCC_AnsEndNoOfTimes))
                                    self.Log('NumberOfAnsCall - Observed' + str(NumberOfAnsCallDetected))
                                    
                                    if gCC_AnsEndNoOfTimes == NumberOfAnsCallDetected :
                                        self.WriteXls(-1,5,'Pass',4)
                                        self.Log('Call Control - Answer Call Pass')
                                    else : 
                                        self.WriteXls(-1,5,'Fail',5)
                                        self.Log('Call Control - Answer Call Fail')
                                        
                                    self.WriteXls(0,2,'End Control',1)
                                    message = "Input - " + str(gCC_AnsEndNoOfTimes) + "/ Observed - " + str(NumberOfEndCallDetected)                                  
                                    self.WriteXls(-1,3,message,1)                                                                    
                                    
                                    self.Log('NumberOfEndCall - Done' + str(gCC_AnsEndNoOfTimes))
                                    self.Log('NumberOfEndCall - Observed' + str(NumberOfEndCallDetected))
                                   
                                    if gCC_AnsEndNoOfTimes == NumberOfEndCallDetected :
                                        self.WriteXls(-1,5,'Pass',4)
                                        self.Log('Call Control - End Call Pass')
                                    else : 
                                        self.WriteXls(-1,5,'Fail',5)
                                        self.Log('Call Control - Answer Call Fail')
                                                    
                                    self.WriteXls(0,2,'Reject Control',1)
                                    message = "Input - " + str(gCC_RejectNoOfTimes) + "/ Observed - " + str(NumberOfRejectCallDetected)                                  
                                    self.WriteXls(-1,3,message,1)                                
                                    
                                    self.Log('NumberOfRejectCall - Done' + str(gCC_RejectNoOfTimes))
                                    self.Log('NumberOfRejectCall - Observed' + str(NumberOfRejectCallDetected))
                                   
                                    if gCC_RejectNoOfTimes == NumberOfRejectCallDetected :
                                        self.WriteXls(-1,5,'Pass',4)
                                        self.Log('Call Control - Reject Call Pass')
                                    else : 
                                        self.WriteXls(-1,5,'Fail',5)
                                        self.Log('Call Control - Reject Call Fail')
                        
                        else :
                            self.Log("Options are not selected in Mobile Phone control")
                            
                    DoMobilePhoneControlTest()
                    
                if checkRssi == True:
                    def DoRssiTest():
                        global StopTesting
                        global Device_Name
                        global TestCaseSerialNumber
                        global MacAddress
                        
                        CurrentBatteryValue = GetBatteryPercentage(MacAddress)
                        
                        if StopTesting == True or CurrentBatteryValue < 60:
                            return
                        self.Log("RSSI Test Started")
                        
                        result = DeviceUnPairbyMacAddress(MacAddress)
                        if result == False:                            
                            for j in range(5):
                                time.sleep(1)
                                if StopTesting == True:
                                    break
                            
                            bl.StartRssiTest(Device_Name)
                            start = time.time()
                            rssiQueue = Queue()
                            
                            hours1, minutes1 = divmod(RssiDuration, 60)                            
                            hours1, rem1 = divmod(RssiDuration, 3600)
                            minutes1, seconds1 = divmod(rem1, 60)
                            Sum = int(0)
                            TotalCount = int(0)
                            rssilist = ''
                            
                            while 1:                            
                                out = bl.GetRssiValue()         
                                if out != 0:
                                    Strout = 'Current RSSI value is ' + str(out)
                                    rssilist = rssilist + "," +str(out)
                                    self.Log(Strout)
                                    Sum = Sum + out
                                    TotalCount += 1
                                    
                                end = time.time()
                                hours, rem = divmod(end-start, 3600)
                                minutes, seconds = divmod(rem, 60)                                
                                if int(hours) == int(hours1) and int(minutes) == int(minutes1) and int(seconds) >= int(seconds1):
                                    
                                    self.WriteXls(0,1,str(TestCaseSerialNumber),1)
                                    TestCaseSerialNumber += 1
                                    self.WriteXls(-1,2,'RSSI Test',2)                                    
                                    Average = Sum/TotalCount
                                    message = 'Duration - ' + str(RssiDuration) + " seconds / Values -" + str(rssilist) + " / Average -" + str(Average)
                                    self.WriteXls(-1,3,message,1)
                                    
                                    if Average > -58 :                                    
                                        self.WriteXls(-1,5,'Pass',4)
                                    else :
                                        self.WriteXls(-1,5,'Fail',5)
                                    self.WriteXls(-1,4,'-58 >',1)
                                    
                                    self.Log("Rssi Test - Completed") 
                                    break                                    
                                if StopTesting == True:
                                    self.Log("Rssi Test - Interrupted") 
                                    break
                                time.sleep(1)                            
                            bl.StopRssiTest()                                   
                            result = DeviceConnectbyMacAddress(2,MacAddress,True)
                            if result == True:                                
                                for j in range(5):
                                    time.sleep(1)
                                    if StopTesting == True:
                                        break                                                    
                        self.Log("Rssi Testing is completed")                        
                    DoRssiTest()
                    
                if checkLng == True:
                    def DoLongHourTest():                        
                        global Logtext                    
                        global StopTesting
                        global MacAddress
                        global VolumeControl
                        global PlayPauseStatus
                        global NumberOfPlayPauseInLngHourPlayback
                        global TestCaseSerialNumber
                        global s
                        
                        if StopTesting == True:
                            return                        
                        if Lngend == 0:
                            message = "Infinite playback started with "+ str(VolumeControl) +"% volume"                                
                            self.WriteXls(0,1,str(TestCaseSerialNumber),1)
                            TestCaseSerialNumber += 1
                            self.WriteXls(-1,2,'Long Hour play back',2)
                            self.WriteXls(-1,3,'Battery Drain Info/Discharge Time',2)                                                    
                            
                        else :
                            message = str(Lngend) + " " + "Minutes playback started with " + str(VolumeControl) + "% volume"                                               
                        self.Log(message)                        
                        start = time.time()
                        t = time.time()     
                        
                        t2 = threading.Thread(target = self.stetaupdate)
                        t2.start()
                        NumberOfPlayPauseInLngHourPlayback = int(0)
                        
                        self.Start_vlc()  
                            
                        start1 = time.time()
                        DeviceConnectedInLongHour = True
                        NumberOfConnectionLost = 0
                        PreviousBatteryLevel = GetBatteryPercentage(MacAddress)
                        
                        if PreviousBatteryLevel == -1:
                            self.Log("Problems in getting battery level - Longhour playback stopped")
                        else :    
                            BatteryLevelAtStart = PreviousBatteryLevel
                            MeasureBatteryLevelCount = 0
                            
                            if PreviousBatteryLevel%10 == 0:
                                TargetBatteryLevel =  PreviousBatteryLevel - 10
                            else :                            
                                TargetBatteryLevel =  math.floor(PreviousBatteryLevel/10)*10
                            
                            PlayStatusCount = 0
                            
                            while 1:                            
                                result = DeviceStatusbyMacAddress(1,MacAddress);
                                if result == False:
                                    self.Log("Device is disconnected and Longhour playback stopped ")
                                    self.Stop_vlc()
                                    if s != None:
                                        s.close()
                                        s = None
                                        
                                    DeviceConnectedInLongHour = False
                                    # Wait for 5 min
                                    for i in range(10) :
                                        time.sleep(30)
                                        result = DeviceConnectbyMacAddress(1,MacAddress,True)
                                        if result == True:
                                            self.Log("Device is reconnected and started to continue Longhour ")
                                            self.Start_vlc() 
                                            DeviceConnectedInLongHour = True
                                            NumberOfConnectionLost = NumberOfConnectionLost + 1
                                            break;
                                    
                                if DeviceConnectedInLongHour == False :
                                    self.Log("Device is disconnected and Turned OFF")
                                    break
                                end1 = time.time() 
                                time.sleep(3)
                                MeasureBatteryLevelCount = MeasureBatteryLevelCount+1
                                
                                if MeasureBatteryLevelCount == 20: # Measure Battery level for every 1 min
                                    NewBatteryLevel = GetBatteryPercentage(MacAddress)
                                    print('Current battery level is ' +str(NewBatteryLevel))
                                    if NewBatteryLevel == TargetBatteryLevel:
                                        CurrentT = time.time()
                                        hours2, rem2 = divmod(CurrentT-t, 3600)
                                        minutes2, seconds2 = divmod(rem2, 60)  
                                        message1 = "Between " + str(PreviousBatteryLevel) + " and "+ str (TargetBatteryLevel) + " :"
                                        self.Log(message1)
                                        
                                        
                                        
                                        message2 = "{:0>2}H:{:0>2}M:{:0>2}S".format(int(hours2),int(minutes2),int(seconds2))                                        
                                        self.Log(message2)
                                        message = message1 + message2
                                        
                                        if Lngend == 0:
                                            self.WriteXls(0,3,message,1)
                                        
                                                             
                                        hours3, rem3 = divmod(CurrentT-start, 3600)
                                        minutes3, seconds3 = divmod(rem3, 60)  
                                        message = "Total Discharge till now from " + str(BatteryLevelAtStart) + " and "+ str (TargetBatteryLevel) + " :"
                                        self.Log(message)
                                        self.Log("{:0>2}H:{:0>2}M:{:0>2}S".format(int(hours3),int(minutes3),int(seconds3)))
                                        PreviousBatteryLevel = TargetBatteryLevel
                                        TargetBatteryLevel = NewBatteryLevel - 10
                                        
                                        t = time.time()
                                    MeasureBatteryLevelCount  = 0
                                    if PlayPauseStatus == True:
                                        PlayStatusCount += 1
                                    else :
                                        PlayStatusCount = 0
                                if StopTesting == True:
                                    self.Log("Long Hour Playback Test - Interrupted") 
                                    break
                                
                                #Time Ends
                                if Lngend == 0:
                                    continue
                                end = time.time()
                                hours, rem = divmod(end-start, 3600)
                                minutes, seconds = divmod(rem, 60)                            
                                hours1, minutes1 = divmod(Lngend, 60)
                                
                                if int(hours) == int(hours1) and int(minutes) == int(minutes1):
                                    self.Log("Long Hour Playback Test - PASS") 
                                    break
                                
                                if PlayStatusCount == 3:
                                    self.Log("Long Hour Playback Test - Player is paused for 3 min") 
                                    break
                            
                        self.Stop_vlc()
                        if s != None:
                            s.close()
                            s = None
                        end = time.time()
                        hours, rem = divmod(end-start, 3600)
                        minutes, seconds = divmod(rem, 60)
                        message = "Played duration:{:0>2}H:{:0>2}M:{:0>2}S".format(int(hours),int(minutes),int(seconds)) 
                        self.Log(message)
                        self.WriteXls(0,3,message,1)
                        message = "Number Of Disconnections-Connections : " + str(NumberOfConnectionLost)
                        self.WriteXls(0,3,message,1)
                        self.Log(message)
                        message = "Number Of Play-Pause during Long hour Playback : " + str(NumberOfPlayPauseInLngHourPlayback)
                        self.Log(message)
                        self.WriteXls(0,3,message,1)
                        self.Log("Long Hour back is completed")                     
                    DoLongHourTest()
                
                
                    
                self.help_string.get_screen('Test').ids.stoptest.disabled = True
                self.help_string.get_screen('Test').ids.back.disabled = False                
                self.help_string.get_screen('Test').ids.Clear.disabled = False                
                self.help_string.get_screen('Test').ids.start.disabled = False
                self.help_string.get_screen('Test').ids.Lngcheck.disabled = False
                self.help_string.get_screen('Test').ids.rssicheck.disabled = False
                self.help_string.get_screen('Test').ids.AudioTestingcheck.disabled = False
                self.help_string.get_screen('Test').ids.MPControlcheck.disabled = False
                self.help_string.get_screen('Test').ids.Speakercheck.disabled = False
                self.help_string.get_screen('Test').ids.BatteryLifecheck.disabled = False
                self.help_string.get_screen('Test').ids.CTCcheck.disabled = False
                self.help_string.get_screen('Test').ids.ConnectivityCheck.disabled = False
                
                self.Disconnect()
                
                '''result = DeviceStatusbyMacAddress(1,MacAddress)
                if result == False:
                    MyLogFile()      
                    MyWriteXls()                  
                    Logtext = ''
                    XlsName = None
                    LogFileName = None
                    MacAddress = None
                    @mainthread
                    def updater():
                        self.help_string.get_screen('Test').ids.sumtext.text = str(Logtext)        
                        self.help_string.current = 'BT setting'
                    updater()'''
                                                 
                print('Testing is done')
            threading.Thread(target=DoAllTests).start()
    
    def stetaupdate (self):        
        global tapdflag        
        #Key Input capturing for counting the number of Key inputs 
        def on_press(key):
            global Measuredrightst
            global Measuredrightdt
            global Measuredrightlt
            global Measuredleftst
            global Measuredleftdt
            global Measuredleftlt
            global PlayPauseStatus
            global NumberOfPlayPauseInLngHourPlayback
            global Keyboard
                                        
            receivedkey = format(key)                          
            if key == keyboard.Key.media_play_pause:
                if ctctt == 1:
                    Measuredleftst = Measuredleftst + 1
                    print(key)
                    print("Left Play/Pause Detected : ", Measuredleftst)
                elif ctctt == 2:
                    Measuredrightst = Measuredrightst + 1
                    print("Right Play/Pause Detected : ", Measuredrightst)
                elif ctctt == 3:
                    print("Left Double tap detected as Left Single tap")
                elif ctctt == 4:
                    print("Right Double tap detected as Right single tap")
                if PlayPauseStatus == True :
                    PlayPauseStatus = False
                else :
                    NumberOfPlayPauseInLngHourPlayback += 1
                    PlayPauseStatus = True                                
                
            if key == keyboard.Key.media_next:
                print("Next track started")
                Measuredrightdt = Measuredrightdt + 1
            if key == keyboard.Key.media_previous:
                print("Previous track started")
                Measuredleftdt = Measuredleftdt + 1
                
            if receivedkey == playpause:
                if ctctt == 1:
                    Measuredleftst = Measuredleftst - 1
                elif ctctt == 2:
                    Measuredrightst = Measuredrightst - 1
                Keyboard.press(Key.media_play_pause)
                Keyboard.release(Key.media_play_pause)
        
        if (tapdflag == 0):
            tapdflag = 1            
            with keyboard.Listener(on_press=on_press) as listener:
                listener.join()
                

     
    def Stop_test(self):                                                                   # stop button fun
        self.dialog = MDDialog(
            title="Testing is in Progress..Do you really want to stop the test ?",
            type="custom",
            buttons=[
                MDFlatButton(
                text="CANCEL", text_color=self.theme_cls.primary_color, on_release=self.closeDialogBt
                ),
                MDFlatButton(
                text="YES", text_color=self.theme_cls.primary_color, on_release=self.stoptest
                ),
            ],
        )
        self.dialog.open()

    def stoptest(self,dt):
        self.dialog.dismiss()
        global StopTesting
        StopTesting = True
        self.Log("Testing is Stopped Manually")        
        self.help_string.get_screen('Test').ids.start.disabled = False        
        self.help_string.get_screen('Test').ids.back.disabled = False                
        self.help_string.get_screen('Test').ids.Clear.disabled = False                
        self.help_string.get_screen('Test').ids.stoptest.disabled = True
        self.help_string.get_screen('Test').ids.Lngcheck.disabled = False
        self.help_string.get_screen('Test').ids.rssicheck.disabled = False
        self.help_string.get_screen('Test').ids.AudioTestingcheck.disabled = False
        self.help_string.get_screen('Test').ids.MPControlcheck.disabled = False
        self.help_string.get_screen('Test').ids.Speakercheck.disabled = False
        self.help_string.get_screen('Test').ids.BatteryLifecheck.disabled = False
        self.help_string.get_screen('Test').ids.CTCcheck.disabled = False
        self.help_string.get_screen('Test').ids.ConnectivityCheck.disabled = False                

    def closeDialogConnect(self, inst):        
        self.dialog.dismiss()

    def closeDialogBt(self, inst):
        self.help_string.get_screen('Test').ids.ConnectivityCheck.active = False
        self.dialog.dismiss()

    def closeDialogLongHr(self, inst):
        self.help_string.get_screen('Test').ids.Lngcheck.active = False
        self.dialog.dismiss()
        
    def closeDialogCtcLeftSt(self, inst):
        self.help_string.get_screen('CTC').ids.LeftEarbudSTCheck.active = False
        self.dialog.dismiss()

    def closeDialogCtcLeftDt(self, inst):
        self.help_string.get_screen('CTC').ids.LeftEarbudDTCheck.active = False
        self.dialog.dismiss()

    def closeDialogCtcLeftLt(self, inst):
        self.help_string.get_screen('CTC').ids.LeftEarbudLTCheck.active = False
        self.dialog.dismiss()
        
    def closeDialogCtcRightSt(self, inst):
        self.help_string.get_screen('CTC').ids.RightEarbudSTCheck.active = False
        self.dialog.dismiss()

    def closeDialogCtcRightDt(self, inst):
        self.help_string.get_screen('CTC').ids.RightEarbudDTCheck.active = False
        self.dialog.dismiss()

    def closeDialogCtcRightLt(self, inst):
        self.help_string.get_screen('CTC').ids.RightEarbudLTCheck.active = False
        self.dialog.dismiss()
   
    def closeDialogCallControl(self, inst):
        self.help_string.get_screen('MobilePhoneControl').ids.CallControlCheck.active = False
        self.dialog.dismiss()
        
    def closeDialogPlayControl(self, inst):
        self.help_string.get_screen('MobilePhoneControl').ids.PlayControlCheck.active = False
        self.dialog.dismiss()
   

    def IsDeviceAirohaBased(self,DeviceName):
        global NB_Product
        Value = False
        with open('data.json') as json_file:
            data = json.load(json_file)
            Dic = data['Airoha']
            SupportingDeviceList = Dic['TWS_Devices']
            print(SupportingDeviceList)
            for d in SupportingDeviceList :
                if DeviceName == d :
                    print(d)
                    Value = True
                    break
                    
            if Value == False :
                SupportingDeviceList = Dic['NB_Devices']
                print(SupportingDeviceList)
                for d in SupportingDeviceList :
                    if DeviceName == d :
                        print(d)
                        NB_Product = True
                        Value = True
                        break
        return Value

    def LoadMobilePhoneDetails(self):
        global MP1_OsVersion
        global MP1_ModelName
        global MP1_SerialNumber
        global MP1_PhoneNumber
        global MP2_SerialNumber
        
        with open('data.json') as json_file:
            data = json.load(json_file)
            MobilePhone = data['MobileInformation']
            MP1_ModelName = MobilePhone['MobilePhone1_ModelName']
            MP1_OsVersion = MobilePhone['MobilePhone1_OsVersion']
            MP1_SerialNumber = MobilePhone['MobilePhone1_SerialNumber']
            MP1_PhoneNumber = MobilePhone['MobilePhone1_PhoneNumber']
            MP2_SerialNumber = MobilePhone['MobilePhone2_SerialNumber']


    def LoadOtherDetails(self):
        global TesterName
        global ToolVersion
        
        with open('data.json') as json_file:
            data = json.load(json_file)
            TesterName = data['TesterName']
            ToolVersion = data['ToolVersion']
        
    def LoadTestConfiguration(self):        
        global Lngend
        global VolumeControl
        global Bttimes
        global BTpairtimes
        global RssiDuration

        global gleftstNoOfTimes
        global gleftstInterval
        global gleftdtNoOfTimes
        global gleftdtInterval
        global gleftltNoOfTimes
        global gleftltInterval

        global grightstNoOfTimes
        global grightstInterval
        global grightdtNoOfTimes
        global grightdtInterval
        global grightltNoOfTimes
        global grightltInterval

        global gCC_AnsEndNoOfTimes
        global gCC_RejectNoOfTimes        
        global gPC_PlayPauseNoOfTimes
        global gPC_NextPrevNoOfTimes
        global gPC_VolumeNoOfTimes

        #counting the events
        global rightst
        global rightdt
        global rightlt

        global leftst
        global leftdt
        global leftlt
        
        global checkLng
        global checkBT
        global checkctc
        global checkAudioTesting
        global checkSpeakerTesting
        global checkBattery
        global checkRssi
        global checkMpTesting
        
        global DefaultLngend
        global DefaultBttimes
        global DefaultBTpairtimes
        global DefaultRssiDuration

        global gDefaultleftstNoOfTimes
        global gDefaultleftstInterval
        global gDefaultleftdtNoOfTimes
        global gDefaultleftdtInterval
        global gDefaultleftltNoOfTimes
        global gDefaultleftltInterval

        global gDefaultrightstNoOfTimes
        global gDefaultrightstInterval
        global gDefaultrightdtNoOfTimes
        global gDefaultrightdtInterval
        global gDefaultrightltNoOfTimes
        global gDefaultrightltInterval
        
        global gDefaultCC_AnsEndNoOfTimes
        global gDefaultCC_RejectNoOfTimes        
        global gDefaultPC_PlayPauseNoOfTimes
        global gDefaultPC_NextPrevNoOfTimes
        global gDefaultPC_VolumeNoOfTimes
        
        # Opening JSON file
        with open('data.json') as json_file:
            data = json.load(json_file)
            Dic = data['Airdopes']
            if Dic['EnableConnectivity'] == 'Yes':
                self.help_string.get_screen('Test').ids.ConnectivityCheck.active = True
                checkBT = True
            if Dic['EnableCTC'] == 'Yes':
                self.help_string.get_screen('Test').ids.CTCcheck.active = True
                checkctc = True                
            if Dic['EnableBatteryLife'] == 'Yes':
                self.help_string.get_screen('Test').ids.BatteryLifecheck.active = True
                checkBattery = True
            if Dic['EnableMicTesting'] == 'Yes':
                self.help_string.get_screen('Test').ids.AudioTestingcheck.active = True
                checkAudioTesting = True
            if Dic['EnableMobilePhoneTesting'] == 'Yes':
                self.help_string.get_screen('Test').ids.MPControlcheck.active = True
                checkMpTesting = True                 
            if Dic['EnableSpeakerTesting'] == 'Yes':
                self.help_string.get_screen('Test').ids.Speakercheck.active = True
                checkSpeakerTesting = True 
            if Dic['EnableLongHourTesting'] == 'Yes':
                self.help_string.get_screen('Test').ids.Lngcheck.active = True
                checkLng = True
            if Dic['EnableRssiTesting'] == 'Yes':
                self.help_string.get_screen('Test').ids.rssicheck.active = True
                checkRssi = True
                
            DefaultLngend = int(Dic['LongHour'])
            VolumeControl = int(Dic['VolumeControl'])
            DefaultBttimes = int(Dic['ConnectionTimes'])
            DefaultBTpairtimes = int(Dic['PairingTimes'])
            DefaultRssiDuration = int(Dic['RssiObservationDuration'])

            CTC_Config = Dic['CTC']
            if CTC_Config['LeftSTCheckEnable'] == 'Yes':
                self.help_string.get_screen('CTC').ids.LeftEarbudSTCheck.active = True
                leftst = True
            if CTC_Config['LeftDTCheckEnable'] == 'Yes':
                self.help_string.get_screen('CTC').ids.LeftEarbudDTCheck.active = True
                leftdt = True                
            if CTC_Config['LeftLTCheckEnable'] == 'Yes':
                leftlt = True
            if CTC_Config['RightSTCheckEnable'] == 'Yes':
                self.help_string.get_screen('CTC').ids.RightEarbudSTCheck.active = True
                rightst = True
            if CTC_Config['RightDTCheckEnable'] == 'Yes':
                self.help_string.get_screen('CTC').ids.RightEarbudDTCheck.active = True
                rightdt = True                
            if CTC_Config['RightLTCheckEnable'] == 'Yes':
                rightlt = True
                        
            gDefaultleftstNoOfTimes = int(CTC_Config['LeftSingleNoOfTimes'])
            gDefaultleftstInterval = int(CTC_Config['LeftSingleInterval'])
            gDefaultleftdtNoOfTimes = int(CTC_Config['LeftDoubleNoOfTimes'])
            gDefaultleftdtInterval = int(CTC_Config['LeftDoubleInterval'])
            gDefaultleftltNoOfTimes = int(CTC_Config['LeftLongNoOfTimes'])
            gDefaultleftltInterval = int(CTC_Config['LeftLongInterval'])

            gDefaultrightstNoOfTimes = int(CTC_Config['RightSingleNoOfTimes'])
            gDefaultrightstInterval = int(CTC_Config['RightSingleInterval'])
            gDefaultrightdtNoOfTimes = int(CTC_Config['RightDoubleNoOfTimes'])
            gDefaultrightdtInterval = int(CTC_Config['RightDoubleInterval'])
            gDefaultrightltNoOfTimes = int(CTC_Config['RightLongNoOfTimes'])
            gDefaultrightltInterval = int(CTC_Config['RightLongInterval'])  
            
            Control_Config = Dic['Control']
            if Control_Config['CallControlEnable'] == 'Yes':
                self.help_string.get_screen('MobilePhoneControl').ids.CallControlCheck.active = True
                callcontrol = True
            if Control_Config['PlayControlEnable'] == 'Yes':
                self.help_string.get_screen('MobilePhoneControl').ids.PlayControlCheck.active = True
                playcontrol = True

            gDefaultCC_AnsEndNoOfTimes = int(Control_Config['AnswerEndNoOfTimes'])
            gDefaultCC_RejectNoOfTimes = int(Control_Config['RejectNoOfTimes'])
            gDefaultPC_PlayPauseNoOfTimes = int(Control_Config['PlayPauseNoOfTimes'])
            gDefaultPC_NextPrevNoOfTimes = int(Control_Config['NextPrevNoOfTimes'])
            gDefaultPC_VolumeNoOfTimes = int(Control_Config['VolumeUpDownNoOfTimes'])
            
        Lngend = DefaultLngend
        Bttimes = DefaultBttimes
        BTpairtimes = DefaultBTpairtimes
        RssiDuration = DefaultRssiDuration

        gleftstNoOfTimes = gDefaultleftstNoOfTimes
        gleftstInterval = gDefaultleftstInterval
        gleftdtNoOfTimes = gDefaultleftdtNoOfTimes
        gleftdtInterval = gDefaultleftdtInterval
        gleftltNoOfTimes = gDefaultleftltNoOfTimes
        gleftltInterval = gDefaultleftltInterval

        grightstNoOfTimes = gDefaultrightstNoOfTimes
        grightstInterval = gDefaultrightstInterval
        grightdtNoOfTimes = gDefaultrightdtNoOfTimes
        grightdtInterval = gDefaultrightdtInterval
        grightltNoOfTimes = gDefaultrightltNoOfTimes
        grightltInterval = gDefaultrightltInterval
       
        gCC_AnsEndNoOfTimes = gDefaultCC_AnsEndNoOfTimes
        gCC_RejectNoOfTimes = gDefaultCC_RejectNoOfTimes
        gPC_PlayPauseNoOfTimes = gDefaultPC_PlayPauseNoOfTimes
        gPC_NextPrevNoOfTimes = gDefaultPC_NextPrevNoOfTimes
        gPC_VolumeNoOfTimes = gDefaultPC_VolumeNoOfTimes
        
        if checkLng == False and checkBT == False and checkctc == False and checkSpeakerTesting == False and checkAudioTesting == False and checkBattery == False and checkMpTesting == False:
            self.help_string.get_screen('Test').ids.stoptest.disabled = False
            self.help_string.get_screen('Test').ids.start.disabled = True
        else : 
            self.help_string.get_screen('Test').ids.stoptest.disabled = True
            self.help_string.get_screen('Test').ids.start.disabled = False

    def ClearAllConfiguration(self):
        # Opening JSON file        
        global Lngend
        global Bttimes
        global BTpairtimes
        global RssiDuration

        global gleftstNoOfTimes
        global gleftstInterval
        global gleftdtNoOfTimes
        global gleftdtInterval
        global gleftltNoOfTimes
        global gleftltInterval

        global grightstNoOfTimes
        global grightstInterval
        global grightdtNoOfTimes
        global grightdtInterval
        global grightltNoOfTimes
        global grightltInterval
       
        self.help_string.get_screen('Test').ids.ConnectivityCheck.active = False
        self.help_string.get_screen('Test').ids.CTCcheck.active = False
        self.help_string.get_screen('Test').ids.BatteryLifecheck.active = False
        self.help_string.get_screen('Test').ids.AudioTestingcheck.active = False
        self.help_string.get_screen('Test').ids.MPControlcheck.active = False
        
        self.help_string.get_screen('Test').ids.Speakercheck.active = False
        self.help_string.get_screen('Test').ids.Lngcheck.active = False
        self.help_string.get_screen('Test').ids.rssicheck.active = False
        checkBT = False
        checkctc = False                
        checkBattery = False
        checkAudioTesting = False                
        checkLng = False
        checkSpeakerTesting = False
        checkMpTesting = False

        self.help_string.get_screen('CTC').ids.LeftEarbudSTCheck.active = False
        leftst = False

        self.help_string.get_screen('CTC').ids.LeftEarbudDTCheck.active = False
        leftdt = False
        leftlt = False
        self.help_string.get_screen('CTC').ids.RightEarbudSTCheck.active = False
        rightst = False
        self.help_string.get_screen('CTC').ids.RightEarbudDTCheck.active = False
        rightdt = False
        rightlt = False

        self.help_string.get_screen('Test').ids.stoptest.disabled = False
        self.help_string.get_screen('Test').ids.start.disabled = True

        Lngend=int(60)
        Bttimes=int(10)
        BTpairtimes=int(10)
        RssiDuration = int(30)
        StopTesting = False

        gleftstNoOfTimes = int(15)
        gleftstInterval = int(3)
        gleftdtNoOfTimes = int(15)
        gleftdtInterval = int(3)
        gleftltNoOfTimes = int(15)
        gleftltInterval = int(3)

        grightstNoOfTimes = int(15)
        grightstInterval = int(3)
        grightdtNoOfTimes = int(15)
        grightdtInterval = int(3)
        grightltNoOfTimes = int(15)
        grightltInterval = int(3)
        
        gCC_AnsEndNoOfTimes = int(3)
        gCC_RejectNoOfTimes = int(3)        
        gPC_PlayPauseNoOfTimes = int(3)
        gPC_NextPrevNoOfTimes = int(3)
        gPC_VolumeNoOfTimes = int(3)
            
############################################################################################################################
MainApp().run()

if MacAddress != None:
    subprocess.Popen(['pkill', 'vlc'])
    MyLogFile()
    MyWriteXls()
    
print('\nGolem Exit..')   
sys.exit()
Window.close() 