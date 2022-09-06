import socket


# cria, mas não associa um socket
# AF_INET = através da internet
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect( ('data.pr4e.org', 80) ) # ('host', port)
