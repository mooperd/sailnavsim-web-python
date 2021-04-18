import socket
import sys


def sendMessage(msg):
    #TODO: Catch some exceptions: https://docs.python.org/3/library/socket.html#exceptions
    server_address = ('localhost', 5001)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(5)
        sock.connect(server_address)
        sock.sendall(msg)
        recv = sock.recv(64)
    return recv

"""
def sendMessage(msg):
    #TODO: Catch some exceptions: https://docs.python.org/3/library/socket.html#exceptions
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)


    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 5001)
    print('connecting to {} port {}'.format(*server_address))
    sock.connect(server_address)
    
    try:
        # Send data
        print('sending {!r}'.format(msg))
        sock.sendall(msg)
        recv = sock.recv(64)

    finally:
        print('closing socket')
        sock.close()
        return recv
"""

def addBoatinCore(name, latitude, longitude, boat_type, boat_flags, boat_id):
    # boatcmd,Boatname,add,lat,long,0,0,0
    msg = f"boatcmd,{name},add,{latitude},{longitude},{boat_type},{boat_flags},{boat_id}\n".encode()
    sendMessage(msg)
    if "ok" in str(msg):
        return True
    else:
        return False


def startBoatinCore(name, boat_id):
    # boatcmd,Boatname,add,lat,long,0,0,0
    msg = f"boatcmd,{name},start,{boat_id}\n".encode()
    sendMessage(msg)
    if "ok" in str(msg):
        return True
    else:
        return False


def setCourseinCore(name, course, boat_id):
    # boatcmd,Boatname,add,lat,long,0,0,0
    msg = f"boatcmd,{name},course,{course},{boat_id}\n".encode()
    sendMessage(msg)
    if "ok" in str(msg):
        return True
    else:
        return False