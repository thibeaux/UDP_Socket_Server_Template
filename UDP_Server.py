"""
Author:     Brandon Thibeaux
Date:       2/11/2023
Brief:      UDP Server Sample
"""
import socket
import time
import ServiceClass

localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024
msgFromServer = "Server Ack to UDP Client"


def create_socket():
    try:
        # Create a datagram socket
        udp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        # Bind to address and ip
        udp_server_socket.bind((localIP, localPort))
        print("UDP server up and listening")
        return udp_server_socket
    except:
        print("fail to create socket")
        return None


def add(num1,num2):
    return num1 + num2

def run_command_1(udp_server_socket):
    service = ServiceClass.Service("Service_1",add)
    active = True
    udp_server_socket.settimeout(.001)
    bytes_to_send_address_pair = []
    last_time = time.time()
    program_input = [0, 0]
    while active:
        # execute service functionality here
        if len(program_input) < 2:  # make sure we have at least two values in buffer
            program_input.append(0)
        res = service.service(int(program_input[0]), int(program_input[1]))
        print(res)

        # check for incoming packets
        try:
            bytes_to_send_address_pair = udp_server_socket.recvfrom(bufferSize)
        except:
            # if timed out, then set buffer to 0
            # print("Timeout")  # debug
            bytes_to_send_address_pair = [b'0', b'0']
            pass
        message = bytes_to_send_address_pair[0]
        message = message.decode()
        # Look for
        if message == 'esc':  # exit command
            active = False
            address = bytes_to_send_address_pair[1]
        elif bytes_to_send_address_pair[1] != b'0':  # if address index is not 0, respond and grab data
            address = bytes_to_send_address_pair[1]
            program_input = message.split(',')
            print("line 53: " + str(address))
            udp_server_socket.sendto(str.encode(service.name + "," + str(service.state)),
                                     address)  # Tell client we are exiting
        #  Debug Info
        now = time.time()
        print("Execution cycle time (seconds): " + str(now - last_time))
        last_time = now
    # Before leaving service, clean up
    service.state = ServiceClass.ServiceState.NOT_ACTIVE
    udp_server_socket.settimeout(None)
    udp_server_socket.sendto(str.encode(service.name+","+str(service.state)), address)  # Tell client we are exiting
    del service

def main():
    udp_server_socket = create_socket()
    bytes_to_send = str.encode(msgFromServer)
    while (True):
        bytes_to_send_address_pair = udp_server_socket.recvfrom(bufferSize)
        message = bytes_to_send_address_pair[0]
        address = bytes_to_send_address_pair[1]
        message = message.decode()
        print(message)
        print(address)

        if message == '1':
            # Sending a reply to client
            udp_server_socket.sendto(str.encode(message), address)
            run_command_1(udp_server_socket)
        elif message == '2':
            # Sending a reply to client
            udp_server_socket.sendto(str.encode(message), address)
        elif message == '3':
            # Sending a reply to client
            udp_server_socket.sendto(str.encode(message), address)
        else:  # -1 means unknown command
            # Sending a reply to client
            udp_server_socket.sendto(str.encode('-1'), address)


if __name__ == '__main__':
    main()
