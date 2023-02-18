import socket
import threading
import queue
import secrets
import time
from time import sleep as sleep


def randhex(size):
    return secrets.token_hex(size)

def launch_connection(server :str, port :int, nickname :str, token :str, channel :str):
    sock = socket.socket()

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


def get_message_authour(message) -> str():
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


def start_listner(thread_args :tuple) -> None:

    server = thread_args[0]
    port = thread_args[1]
    nickname = thread_args[2]
    token = thread_args[3]
    channel = thread_args[4]
    file_name = thread_args[5]
    pill2kill = thread_args[6]


    open(file_name, "w").close()

    while not pill2kill.wait(1):
        listner_sock = launch_connection(server, port, nickname, token, channel)

        while not pill2kill.wait(1):

            resp = get_messages(listner_sock)

            with open(file_name, "a") as listener:
                listener.write(resp)


def start_threaded_listner(server :str, port :int, nickname :str, token :str, channel :str) -> tuple:

    #if you need just the file name: just_file_name = file_name.split("/")[2] 
    file_name = "./cache/" + randhex(16) + ".log"


    pill2kill = threading.Event()
    

    thread_args = (server, port, nickname, token, channel, file_name, pill2kill)

    #listner_thread = threading.Thread(target = lambda q, arg : q.put(start_listner(arg)), args=(thread_args,))

    listner_thread = threading.Thread(target = start_listner, args=(thread_args,))

    listner_thread.daemon = True

    return (listner_thread, file_name, pill2kill)


def get_balance(sock) -> int:
    
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

