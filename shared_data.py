import socket, colorama

colorama.init()
server = "localhost"       #settings
channel = "#domino"
botnick = "firestorck_bot"
print("Server : ", server)
print("Channel : ", channel)
print("Name : ", botnick)
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #defines the socket  
print ("connecting to: "+server)
irc.connect((server, 6667))  


SenderRunning, ListenerRunning = 1, 1
ConvUser = ""