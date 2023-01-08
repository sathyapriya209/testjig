# ReachView code is placed under the GPL license.
# Written by Egor Fedorov (egor.fedorov@emlid.com)
# Copyright (c) 2015, Emlid Limited
# All rights reserved.

# If you are interested in using ReachView code as a part of a
# closed source project, please contact Emlid Limited (info@emlid.com).

# This file is part of ReachView.

# ReachView is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# ReachView is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with ReachView.  If not, see <http://www.gnu.org/licenses/>.

import time
import pexpect
import subprocess
import sys

class BluetoothctlError(Exception):
    """This exception is raised, when bluetoothctl fails to start."""
    pass


class Bluetoothctl:
    """A wrapper for bluetoothctl utility."""

    def __init__(self):
        out = subprocess.check_output("rfkill unblock bluetooth", shell = True)
        self.child = pexpect.spawn("bluetoothctl", echo = False)
        
        out = self.get_output("agent off")
        out = self.get_output("agent NoInputNoOutput")
        out = self.get_output("default-agent")
        

    def get_output(self, command, pause = 0):
        """Run a command in bluetoothctl prompt, return output as a list of lines."""
        self.child.send(command + "\n")
        time.sleep(pause)
        #start_failed = self.child.expect(["Rockerz 333 Pro", pexpect.EOF])
        start_failed = self.child.expect(["#", pexpect.EOF])

        if start_failed:
            raise BluetoothctlError("Bluetoothctl failed after running " + command)

        return self.child.before.split(b"\r\n")

                        

    def start_scan(self,DeviceName):
        """Start bluetooth scanning process."""
        try:
            out = self.get_output("menu scan")
            out = self.get_output("clear")
            out = self.get_output("transport bredr")
            out = self.get_output("rssi -50")
            out = self.get_output("pattern " + "\"" + DeviceName + "\"")            
            out = self.get_output("back")
            out = self.get_output("scan on")
            #print(out)
        except e:
            print(e)
            return None
        
    def stop_scan(self):
        """Stop bluetooth scanning process."""
        try:
            out = self.get_output("scan off")
            #print(out)
        except e:
            print(e)
            return None

    def make_discoverable(self):
        """Make device discoverable."""
        try:
            out = self.get_output("discoverable on")
        except e:
            print(e)
            return None

    def parse_device_info(self, info_string):
        """Parse a string corresponding to a device."""
        device = {}
        block_list = [b"[\x1b[0;", b"removed"]
        string_valid = not any(keyword in info_string for keyword in block_list)

        if string_valid:
            try:
                device_position = info_string.rindex(b"Device")
            except ValueError:
                pass
            else:
                if device_position > -1:
                    attribute_list = info_string[device_position:].split(b" ", 2)
                    device = {
                        "mac_address": attribute_list[1],
                        "name": attribute_list[2]
                    }

        return device

    def get_available_devices(self):
        """Return a list of tuples of paired and discoverable devices."""
        try:
            out = self.get_output("devices")
            #print(out)
        except e:
            print(e)
            return None
        else:
            available_devices = []
            for line in out:
                device = self.parse_device_info(line)
                if device:
                    available_devices.append(device)

            return available_devices

    def get_paired_devices(self):
        """Return a list of tuples of paired devices."""
        try:
            out = self.get_output("paired-devices")
            #print(out)
        except e:
            print(e)
            return None
        else:
            paired_devices = []
            for line in out:
                device = self.parse_device_info(line)
                if device:
                    paired_devices.append(device)

            return paired_devices

    def get_discoverable_devices(self):
        """Filter paired devices out of available."""
        available = self.get_available_devices()
        paired = self.get_paired_devices()

        return [d for d in available if d not in paired]

    def get_device_info(self, mac_address):
        """Get device info by mac address."""
        try:
            out = self.get_output("info " + mac_address)
        except ValueError:
            print(e)
            return None
        else:
            return out

    def get_device_trusted_status(self, mac_address):
        """Get device info by mac address."""
        try:
            out = self.get_output("info " + mac_address)
        except ValueError:
            print(e)
            return None
        else:
            for ele in out:                
                string = str(ele,'UTF-8')
                try:
                    device_position = string.index("\tTrusted")  
                except ValueError:
                    pass
                else:
                    if device_position > -1:
                        if string == "\tTrusted: no":
                            return False
                        else :
                            return True
    
    def pair(self, mac_address, trust_value):
        """Try to pair with a device by mac address."""
        
        if trust_value == 1:
            print("Trust the device")
            try:
                out = self.get_output("trust " + mac_address, 4)
            except e:
                print(e)
                return None            
              
        try:
            print("Pair the device")
            out = self.get_output("pair " + mac_address, 4)
        except e:
            print(e)
            return None
        else:
            try:
                res = self.child.expect(["Failed to pair", "Pairing successful", pexpect.EOF])
            
            except pexpect.TIMEOUT:
                res = 0
            except :
                res = 0
                
            success = True if res == 1 else False
            return success

    def remove(self, mac_address):
        """Remove paired device by mac address, return success of the operation."""
        try:
            out = self.get_output("remove " + mac_address, 3)
        except e:
            print(e)
            return None
        else:
            try:
                res = self.child.expect(["not available", "Device has been removed", pexpect.EOF])
            
            except pexpect.TIMEOUT:
                res = 0                
            except :
                res = 0
            
            success = True if res == 1 else False
            return success

    def connect(self, mac_address,trust_value):
        """Try to connect to a device by mac address."""
        if trust_value == 1:
            try:
                out = self.get_output("trust " + mac_address, 4)
            except e:
                print(e)
                return None
            
        try:
            out = self.get_output("connect " + mac_address, 2)
        except :
            print(e)
            return None
        else:
            try:
                res = self.child.expect(["Failed to connect", "Connection successful", pexpect.EOF])
            
            except pexpect.TIMEOUT:
                res = 0                
            except :
                res = 0
            
            success = True if res == 1 else False
            return success

    def disconnect(self, mac_address):
        """Try to disconnect to a device by mac address."""
        try:
            out = self.get_output("disconnect " + mac_address, 2)
        except e:
            print(e)
            return None
        else:
            try:
                res = self.child.expect(["Failed to disconnect", "Successful disconnected", pexpect.EOF])
            
            except pexpect.TIMEOUT:
                res = 0
            except :
                res = 0
            
            success = True if res == 1 else False
            return success
    
    def get_device_paired_status(self, mac_address):
        """Get device info by mac address."""
        try:
            out = self.get_output("info " + mac_address)
            #print(out)
        except ValueError:
            print(e)
            return None
        else:
            for ele in out:                
                string = str(ele,'UTF-8')
                try:
                    device_position = string.index("\tPaired")  
                except ValueError:
                    pass
                else:
                    if device_position > -1:
                        if string == "\tPaired: no":
                            return False
                        else :
                            return True
                        
    def get_device_connected_status(self, mac_address):
        """Get device info by mac address."""
        try:
            out = self.get_output("info " + mac_address)
            #print(out)
        except ValueError:
            print(e)
            return None
        else:
            for ele in out:                
                string = str(ele,'UTF-8')
                try:
                    device_position = string.index("\tConnected")  
                except ValueError:
                    pass
                else:
                    if device_position > -1:
                        if string == "\tConnected: no":
                            return False
                        else :
                            return True
                        
    
    def get_device_rssi_value(self, mac_address):
        """Get device info by mac address."""
        try:
            out = self.get_output("info " + mac_address)
        except ValueError:
            print(e)
            return None
        else:
            for ele in out:                
                string = str(ele,'UTF-8')
                #print(ele)
                try:
                    device_position = string.index("\tRSSI")  
                except ValueError:
                    pass
                else:
                    if device_position > -1:
                        substring = string[device_position+7:device_position+10]
                        return substring
        return "NA"                
            
    def findmac_address(self, devicename):
        print(devicename)
        try:
            out = self.get_output("devices")
            print(out)
        except ValueError:
            print('Failure')
            return None
        else:        
            for line in out:                
                block_list = [b"[\x1b[0;", b"removed"]
                string_valid = not any(keyword in line for keyword in block_list)
                if string_valid:
                    try:
                        device_position = line.index(b"Device")                        
                    except ValueError:
                        pass
                    else:
                        if device_position > -1:
                            attribute_list = line[device_position:].split(b" ", 2)
                            #print(attribute_list[1])
                            #print(attribute_list[2])
                            if str(attribute_list[2],'UTF-8') == devicename:
                                return str(attribute_list[1],'UTF-8')
            return None
        
    def remove_all(self):        
        try:
            cmd = "paired-devices"
            print(cmd)
            out = self.get_output(cmd)
            print(out)
        except ValueError:
            print('Failure')
            return None
        else:        
            for line in out:                
                block_list = [b"[\x1b[0;", b"removed"]
                string_valid = not any(keyword in line for keyword in block_list)
                if string_valid:
                    try:
                        device_position = line.index(b"Device")                        
                    except ValueError:
                        pass
                    else:
                        if device_position > -1:
                            attribute_list = line[device_position:].split(b" ", 2)
                            TempAddress = str(attribute_list[1],'UTF-8')
                            self.remove(TempAddress)                            
            return None
    
    def process_scanresults(self, DeviceName, pause = 10):
        """Run a command in bluetoothctl prompt, return output as a list of lines."""
        self.child.send("scan on" + "\n")        
        #time.sleep(pause)
        substring = None
        timestart = time.time()

                            
        while 1:
            timeend = time.time()        
            hours, rem = divmod(timeend-timestart, 3600)
            minutes, seconds = divmod(rem, 60)
            
            if int(seconds) >= 30: #Wait for 30 sec
                break;            
            try:
                deviceinfo = self.child.readline()
                print(deviceinfo)
                if b"RSSI:" in deviceinfo :
                    device_position = deviceinfo.index(b"RSSI:")                        
                    if device_position > -1:
                        substring = deviceinfo[device_position-18:device_position-1]
                        self.rssiValue = str(deviceinfo[device_position+6:device_position+9],'UTF-8')
                        print(substring)
                        return str(substring,'UTF-8')

                '''elif DeviceName in deviceinfo:
                    device_position = deviceinfo.index(DeviceName)                        
                    if device_position > -1:
                        substring = deviceinfo[device_position-18:device_position-1]
                        print(substring)
                        return str(substring,'UTF-8')'''
                                          
            except :
                pass
        return substring
        '''
        try:
            while 1:
                start_failed = self.child.expect([b"RSSI:", pexpect.EOF])
                if start_failed:
                    raise BluetoothctlError("Bluetoothctl failed after running " + command)

                print(self.child.before.split(b"\r\n"))
            
        except :
            return None
            '''
    
    def ConnectWithDevice(self,DeviceName):        
        try:
            out = self.get_output("menu scan")
            out = self.get_output("clear")
            out = self.get_output("transport bredr")
            #out = self.get_output("rssi -50")
            cmd = "pattern " + "\"" + DeviceName + "\""
            print(cmd)
            out = self.get_output(cmd)            
            out = self.get_output("back")
            Mac = self.process_scanresults(DeviceName)
            out = self.get_output("scan off")
            return Mac
        except :            
            return None
    
    def StartRssiTest(self,DeviceName):        
        try:
            out = self.get_output("menu scan")
            out = self.get_output("clear")
            out = self.get_output("transport bredr")            
            out = self.get_output("pattern " + "\"" + DeviceName + "\"")            
            out = self.get_output("back")
            self.child.send("scan on" + "\n") 
        except :            
            pass
            
    def StopRssiTest(self):    
        try:
            out = self.get_output("scan off")
        except :            
            pass
    
    def GetRssiValue(self):
        try:
            deviceinfo = self.child.readline()
            print(deviceinfo)
            if b"RSSI:" in deviceinfo:
                device_position = deviceinfo.index(b"RSSI:")                        
                if device_position > -1:
                    substring = deviceinfo[device_position-18:device_position-1]
                    self.rssiValue = str(deviceinfo[device_position+6:device_position+9],'UTF-8')
                    #print(substring)
                    out = int(self.rssiValue)
                    return int(out)
                else:
                    out = '0'
                    return int(out)
            else:
                out = '0'
                return int(out)
        except :
            out = '0'
            return int(out)