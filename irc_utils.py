import socket
import threading
import queue
import secrets
import time
import json
import get_conf
from time import sleep as sleep




def launch_connection():
    sock = socket.socket()

    
    server_info = get_conf.server_info()

    server = server_info["server"]
    port = server_info["port"]

    
    user_info = get_conf.user_info()

    token = user_info["token"]
    nickname = user_info["nickname"]
    channel = server_info["channel"]


    sock.connect((server, port))

    sock.send(f"PASS {token}\n".encode('utf-8'))
    sock.send(f"NICK {nickname}\n".encode('utf-8'))
    sock.send(f"JOIN {channel}\n".encode('utf-8'))
    
    #Primes IRC
    for i in range(2):
        while True:
            try:
                sock.recv(2048).decode('utf-8')
            except ConnectionResetError:
                continue
            break

    return sock


def get_messages(sock) -> str:
    while 1:
        try:
            resp = sock.recv(2048).decode('utf-8')
            return resp
        except ConnectionResetError:
            continue
        break


def get_message_text(message :str) -> str:
    out = message.split(":")[2]

    if out.startswith("ACTION"):
        return out.split("ACTION")[1][1:]
    else:
        return out


def get_message_authour(message) -> str:
    for i in range(len(message)):
        if message[i] == "!":
            return message[1:i]


"""
def log_for_three(sock):
    for i in range(10):
        resp = get_messages(sock)

        if get_message_authour(resp) == "schnozebot" and get_message_text(resp).startswith("trininite"):
            return get_message_text(resp)
            
    return(log_for_three(sock))
"""


def start_listner(file_name, kill_switch, bot_client_filter:bool) -> None:


    server_info = get_conf.server_info()

    server = server_info["server"]
    port = server_info["port"]

    
    user_info = get_conf.user_info()

    token = user_info["token"]
    nickname = user_info["nickname"]
    channel = server_info["channel"]

    bot_info = get_conf.bot_info()
    bot_nickname = bot_info["nickname"]


    #clears log file
    open(file_name, "w").close()

    while not kill_switch.wait(1):
        listner_sock = launch_connection()

        while not kill_switch.wait(1):

            resp = get_messages(listner_sock)

            with open(file_name, "a") as listener:
                if not bot_client_filter:
                    listener.write(resp)
                elif bot_client_filter:
                    #call filter function
                    pass
                    

                

def start_threaded_listner() -> tuple:

    #if you need just the file name: just_file_name = file_name.split("/")[2] 
    file_name = "./cache/" + secrets.token_hex(16) + ".log"


    kill_switch = threading.Event()
    
    bot_client_filter = False

    thread_args = (file_name, kill_switch, bot_client_filter)

    #This used to work, leaving it here just it case
    #listner_thread = threading.Thread(target = lambda q, arg : q.put(start_listner(arg)), args=(thread_args,))

    listner_thread = threading.Thread(target = start_listner, args=(thread_args))

    listner_thread.daemon = True

    return (listner_thread, file_name, kill_switch)


#TODO Refactor this function using new threaded lisneter ^^^ 
def get_balance(sock):

    print("fix the function lazy bastard")
    return
    
    que = queue.Queue()
    background_log = threading.Thread(target = lambda q, arg : q.put(log_for_three(arg)), args=(que, sock))
    background_log.daemon = True
    background_log.start()
    
    while 1:
        try:
            sock.send(f"PRIVMSG #xqc :!userpoints\n".encode('utf-8'))
        except BrokenPipeError:
            continue
        break

    background_log.join()  


    balance = ""
    for c in que.get():
        if c.isdigit():
            balance = balance + c

    balance = int(balance)

    return balance




    


#TODO
def send_bet():
    """
    Send a bet to the channel
    Ask listener if bet has gone through
    
    """
    
    ...

