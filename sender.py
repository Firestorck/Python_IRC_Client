from time import gmtime, strftime
import shared_data, colorama

def sender(irc):
    print("Sender threaded loaded")
    while 1:
        try:
            message = input("")
        except:
            shared_data.SenderRunning = 0
            exit()
        if message.startswith("/") == True: #Commands dection
            if message.lower().startswith("/msg ") == True: #True messages
                shared_data.ConvUser, message = message.removeprefix("/msg ").rsplit(" ", 1)
                irc.send(bytearray("PRIVMSG " + shared_data.ConvUser + " " + message + "\r\n", ("utf-8")))
                print(colorama.Fore.YELLOW, strftime("%Y-%m-%d %H:%M:%S", gmtime()), colorama.Fore.BLUE , f"[Me] -> [{shared_data.ConvUser}] : {colorama.Fore.MAGENTA}{message}{colorama.Style.RESET_ALL}")
            elif message.lower().startswith("/r ") == True: #Responses
                message = message.removeprefix("/r ")
                irc.send(bytearray("PRIVMSG " + shared_data.ConvUser + " " + message + "\r\n", ("utf-8")))
                print(colorama.Fore.YELLOW, strftime("%Y-%m-%d %H:%M:%S", gmtime()), colorama.Fore.BLUE , f"[Me] -> [{shared_data.ConvUser}] : {colorama.Fore.MAGENTA}{message}{colorama.Style.RESET_ALL}")
            elif message.lower().startswith(""):
                pass
        #elif irc._closed == True:
        #    print("An error has occured. Please try again.")
        #    exit()
        else:
            irc.send(bytearray(message + "\r\n", ("utf-8")))
            print(colorama.Fore.YELLOW, strftime("%Y-%m-%d %H:%M:%S", gmtime()), colorama.Fore.MAGENTA, message, colorama.Style.RESET_ALL)
