from dronekit import connect, VehicleMode, LocationGlobalRelative,APIException
from pymavlink import mavutil # Needed for command message definitions
import time
import socket
import exceptions
import math
import argparse 

def connectMYCopter():
    parser = argparse.ArgumentParser(description='Control Copter and send commands in GUIDED mode ')
    parser.add_argument('--connect')
    args = parser.parse_args()   
    
    connection_string = args.connect
    baud_rate = 57600
    
    vehicle = connect(connection_string,baud=baud_rate,wait_ready=True)
    return vehicle
    
def arm():
    while vehicle.is _armable==False:
        print(" Waiting for arming...")
        time.sleep(1)
    print("Taking off!")
    
    vehicle.armed=True
    while vehicle.armed==False:
        print(" Waiting for arming...")
        time.sleep(1)
        
     return None

vehicle = connectMYCopter()
arm()
print("end")