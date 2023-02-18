#!/bin/python3.9

import socket
import threading
import queue
import irc_utils
from time import sleep as sleep






def main():
    irc = irc_utils.launch_connection()

    #print(irc_utils.get_balance(irc))

    irc.close()




if __name__ == "__main__":
    main()

