import serial.tools.list_ports #
import requests # package for POST and GET requests

API_ENDPOINT = "your endpoint goes here" #end point 



available_serial_ports = serial.tools.list_ports.comports()
serial_coms_objct= serial.Serial()

portList = [] #empty list of ports to append to

#printing out the ports that are in use 
for onePort in available_serial_ports:
    portList.append(str(onePort))


#input the port you want to connect to
val = input("Select Port by typing its number e.g. if its port3, input 3: COM")


for x in range(1, len(portList)):
    if portList[x].startswith("COM " + str(val)):
        portVar = "COM" + str(val)
        print(portList[x])


serial_coms_objct.baudrate = 9600 #configure the baudrate
serial_coms_objct.port = portVar  # selecting the port number
serial_coms_objct.open() # open port and listen to the incoming data


#we want to listen to incoming data until the user stops sending data through the terminal
if serial_coms_objct.in_waiting:
    data_packet = serial_coms_objct.readline()
    payload = data_packet.decode('utf').rstrip('\n')
    print("Received:", payload) #decoding the data packet coming in from the serial

        # data to be sent to a remote server
    r = requests.post(API_ENDPOINT, data=payload)
    print(r.text)