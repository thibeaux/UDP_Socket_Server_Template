"""
Author:     Brandon Thibeaux
Date:       2/11/2023
Brief:      UDP Client Sample
"""

import socket

msgFromClient = "Hello UDP Server"


serverAddressPort = ("127.0.0.1", 20001)

bufferSize = 1024


def main():
    # Create a UDP socket at client side
    udp_client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # Send to server using created UDP socket
    while 1:
        user_input = input("Enter server command:\t")
        if user_input == 'q':
            break
        bytes_to_send = str.encode(user_input)
        udp_client_socket.sendto(bytes_to_send, serverAddressPort)

        msg_from_server = udp_client_socket.recvfrom(bufferSize)

        msg = "Message from Server {}".format(msg_from_server[0])

        print(msg)


if __name__ == '__main__':
    main()
