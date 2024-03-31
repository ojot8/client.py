# NAME: TAJUDEEN M OJO
# SID: 13146289

import socket
import json

# Define the host and port for the client to connect to
host = '127.0.0.1'
port = 9900

# This function handles the client-side operations
def echo_client(port):

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect the socket to the server
    sock.connect((host, port))

    try:
        # Continuously send messages to the server until an exception occurs
        while True:
        
            # Get the message from the user
            message = raw_input('Enter your text:')
            print("Sending to Server: {} :".format(message))
            
            # Send the message to the server
            sock.sendall(message.encode('utf-8'))
            
            # Receive the response from the server
            data = sock.recv(2048)
            print("Received from Server:", json.loads(data.decode("utf-8")))
    except socket.error as e:
    
        # Handle any socket errors
        print("Socket error: {}".format(str(e)))
    except Exception as e:
    
        # Handle any other exceptions
        print("Other exception: {}".format(str(e)))
    finally:
    
        # Close the connection to the server
        print("Closing connection to the server")
        sock.close()

# If this script is run directly, start the client
if __name__ == '__main__':
    while True:
        echo_client(port)
