#!/usr/bin/python3
import socket
import json
import threading

def start_server(host='127.0.0.1', port=65432):
    """
    Start a server that listens for incoming connections and processes serialized data.
    
    Args:
        host: The host address to bind to
        port: The port number to listen on
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server started on {host}:{port}")
        
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            data = conn.recv(1024)
            if data:
                received_dict = json.loads(data.decode('utf-8'))
                print("\nReceived Dictionary from Client:")
                print(received_dict)

def send_data(data, host='127.0.0.1', port=65432):
    """
    Send serialized data to a server.
    
    Args:
        data: The Python dictionary to send
        host: The server host address
        port: The server port number
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        serialized_data = json.dumps(data).encode('utf-8')
        s.sendall(serialized_data)
