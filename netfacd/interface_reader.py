#!/usr/bin/env python3

import netifaces

print(netifaces.interfaces())

for i in netifaces.interfaces():
    print('\n****** details of interface - ' + i + ' ******')
    try:
        print('MAC: ', end='') # This print statement will always print MAC without an end of line
        print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
        print('IP: ', end='')  # This print statement will always print IP without an end of line
        print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']) # Prints the IP address
    except:          # This is a new line
        print('Could not collect adapter information') # Print an error message

def ip_function(ip="lo"):

    for i in netifaces.interfaces():
        print('\n****** details of interface - IP ' + ip + ' ******')
        try:
            print((netifaces.ifaddresses(ip)[netifaces.AF_INET])[0]['addr']) # Prints the IP address
        except:          # This is a new line
            print('Could not collect adapter information') # Print an error messag
            
def mac_function(mc="lo"):

    for i in netifaces.interfaces():
        print('\n****** details of interface - MAC ' + mc + ' ******')
        try:
            print((netifaces.ifaddresses(mc)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address 
        except:          # This is a new line
            print('Could not collect adapter information') # Print an error messag

def final(f="lo"):

    print('\n****** details of interface - ' + f + ' ******')
    try:
        print('MAC: ', end='') # This print statement will always print MAC without an end of line
        print((netifaces.ifaddresses(f)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
        print('IP: ', end='')  # This print statement will always print IP without an end of line
        print((netifaces.ifaddresses(f)[netifaces.AF_INET])[0]['addr']) # Prints the IP address
    except:          # This is a new line
        print('Could not collect adapter information') # Print an error message

ip_function()
mac_function("ens3")
final("ens3")
