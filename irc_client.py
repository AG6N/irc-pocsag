import socket
import re

server = "irc.geekshed.net"  # IRC server and channel settings
channel = "#hamfest"
botnick = "QRZZZZZZ"

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Define the socket
print("Connecting to: " + server)
irc.connect((server, 6667))  # Connect to the server

user_message = "USER " + botnick + " " + botnick + " " + botnick + " :This just sends messages to an amateur pager\r\n"
irc.send(user_message.encode("UTF-8"))  # User authentication
irc.send(("NICK " + botnick + "\r\n").encode("UTF-8"))  # Set nick

# Regular expression to match text between ":[ and :"
regex_pattern = r":\[(.*?):"

while True:  # Put it in a loop
    text = irc.recv(2040).decode("UTF-8")  # Receive the text and decode it

    if text.find('PING') != -1:  # Check if 'PING' is found
        irc.send(('PONG ' + text.split()[1] + '\r\n').encode("UTF-8"))  # Return 'PONG' back to the server (prevents pinging out!)

   # print(text)  # Print text to the console

    # Check if the server has welcomed the bot, and then join the channel
    if "End of /MOTD command." in text:
        irc.send(("JOIN " + channel + "\r\n").encode("UTF-8"))  # Join the channel after server welcome

    # Use regular expression to find and print text between ":[ and :"
    matches = re.findall(regex_pattern, text)
    for match in matches:
        print(match)
