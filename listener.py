from time import gmtime, strftime
import shared_data, colorama

def listener(irc, botnick):
    ConsecutiveErrorCount = 0
    print(colorama.Fore.BLUE, "Listener thread loaded", colorama.Style.RESET_ALL)
    #text = ""
    colorama.init()
    while 1:                        #puts it in a loop
    #    prevText = text
        text = irc.recv(2040).decode("utf-8", "replace")     #receive the text
        
        if text.find('PRIVMSG ') != -1:
            if text.find('PRIVMSG ' + shared_data.channel) != -1:
                InMsg = text.rsplit("\n", 1)[0].split(":", 2)
                user = InMsg[1].split("!", 1)[0]
                print(colorama.Fore.YELLOW, strftime("%Y-%m-%d %H:%M:%S", gmtime()), colorama.Fore.BLUE , f"{shared_data.channel} [{user}] : {colorama.Fore.MAGENTA}{InMsg[2]}{colorama.Style.RESET_ALL}")    #print text to console
        
            elif text.find('PRIVMSG ' + botnick) != -1:     #private message handling
                InMsg = text.rsplit("\n", 1)[0].split(":", 4)
                shared_data.ConvUser = InMsg[1].rsplit("!", 1)[0]
                print(colorama.Fore.YELLOW, strftime("%Y-%m-%d %H:%M:%S", gmtime()), colorama.Fore.BLUE , f"[{shared_data.ConvUser}] -> [Me] : {colorama.Fore.MAGENTA}{InMsg[2]}{colorama.Style.RESET_ALL}")    #print text to console
        
        elif text.find('PING') != -1:                             #check if 'PING' is found
            irc.send(bytearray('PONG\r\n', ("ascii")))   #returnes 'PONG' back to the server (prevents pinging out!)"
        
        elif text.find('JOIN ') != -1: 
            user = text.replace(":", "").split("!", 1)[0]
            channel = text.rsplit("\n", 1)[0].split("JOIN ")[1]
            print(colorama.Fore.YELLOW, strftime("%Y-%m-%d %H:%M:%S", gmtime()), colorama.Fore.BLUE , f"{channel}{colorama.Fore.GREEN} + {user}{colorama.Style.RESET_ALL}")
        
        elif text.find('PART ') != -1: 
            user = text.replace(":", "").split("!", 1)[0]
            channel = text.rsplit("\n", 1)[0].split("PART ")[1]
            print(colorama.Fore.YELLOW, strftime("%Y-%m-%d %H:%M:%S", gmtime()), colorama.Fore.BLUE , f"{channel}{colorama.Fore.RED} - {user}{colorama.Style.RESET_ALL}")
        
#        elif text.find("End of /NAMES list.") != -1:
#            Names = prevText.split(":", 2)[2].split(" ")
#            for i in Names:
#                print(colorama.Fore.YELLOW, strftime("%Y-%m-%d %H:%M:%S", gmtime()), colorama.Fore.BLUE , f"People in the channel : {colorama.Fore.GREEN}{i}{colorama.Style.RESET_ALL}")
#
        elif text.find(':') == -1:      #disconnection handling
            ConsecutiveErrorCount = ConsecutiveErrorCount +1
            if ConsecutiveErrorCount >= 20:
                print("Too many errors. Please restart the programm\r\n")
                shared_data.ListenerRunning = 0
                exit()

        else:
            ConsecutiveErrorCount = 0
            print(colorama.Fore.YELLOW + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + text.rsplit("\n", 1)[0])   #print text to console
