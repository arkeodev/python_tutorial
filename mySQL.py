#!/usr/bin/python           # This is server.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12347                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(20)                 # Now wait for client connection.

message = "Thank you for connecting"
while True:
   c, addr = s.accept()     # Establish connection with client.
   print('Got connection from', addr)
   c.send(message.encode())
   c.close()                # Close the connection
