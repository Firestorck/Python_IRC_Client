import threading, listener, sender, functools, shared_data
from time import sleep

def irc_connect():
    shared_data.irc.send(bytearray("USER "+ shared_data.botnick +" "+ shared_data.botnick +" "+ shared_data.botnick +" :This is a fun bot!\n", ('ascii'))) #user authentication
    shared_data.irc.send(bytearray("NICK "+ shared_data.botnick +"\n", ("utf-8")))        #sets nick
    print("joining channel")
    shared_data.irc.send(bytearray("JOIN "+ shared_data.channel +"\n", ("utf-8")))        #join the chan

def run_parallel(*functions):
    '''
    Run functions in parallel
    '''
    processes = []
    for function in functions:
        proc = threading.Thread(target=function)
#        my_var_name = [ k for k,v in locals().items() if v is function][0]
#        print(my_var_name)
#        proc.name(function.local().items())
        proc.start()
        processes.append(proc)
    for proc in processes:
        proc.join()

if __name__ == "__main__":
    irc_connect()
    irc_sender = functools.partial(sender.sender, shared_data.irc)
    irc_listener = functools.partial(listener.listener, shared_data.irc, shared_data.botnick)
    run_parallel(irc_sender, irc_listener)
    while 1:
        if shared_data.SenderRunning == 0:
            print("An error has occured with the Sending thread. Restarting in 10s.")
            sleep(10)
            irc_connect()
            run_parallel(irc_sender)
            shared_data.SenderRunning = 1
        elif shared_data.ListenerRunning == 0:
            input("An error has occured with the Listening thread. Restarting. Please press enter to restart the connection.")
            #sleep(1)
            run_parallel(irc_listener)
            shared_data.ListenerRunning = 1
#