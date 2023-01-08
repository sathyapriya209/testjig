import socket

serverMACAddress = 'FC:58:FA:F6:27:C1'
port = 3
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((serverMACAddress,port))

print('connected')    
s.send(bytes([0x05,0x5A,0x03,0x00,0xD6,0x0C,0x00]))
response = s.recv(20)
print(len(response))
print(response.hex())  
response = s.recv(20)
print(len(response))
print(response.hex())

s.close()