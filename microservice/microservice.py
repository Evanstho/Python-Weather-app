import socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('0.0.0.0', 55441))
serv.listen(5)
#print client connection information
print(socket.gethostname())
#infinite loop to listen for traffic
while True:
  conn, addr = serv.accept()
  print(f"Connection established from {addr}")
  from_client = ''
  while True:
    data = conn.recv(4096)
    if not data: break
    from_client += data.decode('utf8')
    print (from_client)
    #if the data sent from client starts with -0-0-0, this is a request to have search history sent
    if from_client.startswith('-0-0-0'):
      with open('search_history.txt', 'r') as file:
        data = file.readlines()
        #print(data)
        last_ten = data[-10:]
        #print(last_ten)
        to_send = ''.join(last_ten)
        print('Sending to client: ' + to_send)
        conn.send("Sending search history.\n".encode())
        conn.send(str(to_send).encode())
        data = file.read(4096)
    #if the data doesn't start with -0-0-0 it is to be saved as a search
    else:
      with open('search_history.txt', 'a') as file:
        print('Saving to file: ' + from_client)
        conn.send("Saving search entry.\n".encode())
        file.write(from_client + '\n')


  conn.close()

print('client disconnected and shutdown')