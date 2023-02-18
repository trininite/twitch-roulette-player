
import socket
import irc_utils
import json
import get_conf
import os
import sys
import hashlib
from time import sleep as sleep


"""
import json

with open('devs_conf.json') as json_file:
    data = json.load(json_file)
    
    
user_info = data["user_info"][0]

print(user_info["nickname"])
"""

#shows threaded listner working consitently
def listner_validate():

    #os.system("./clear_cache.sh")

    listner1_args = irc_utils.start_threaded_listner()
    listner2_args = irc_utils.start_threaded_listner()
    listner3_args = irc_utils.start_threaded_listner()



    listner1 = listner1_args[0]
    file1 = listner1_args[1]
    kill_switch1 = listner1_args[2]
    

    listner2 = listner2_args[0]
    file2 = listner2_args[1]
    kill_switch2 = listner2_args[2]
    
    listner3 = listner3_args[0]
    file3 = listner3_args[1]
    kill_switch3 = listner3_args[2] 

    listner1.start()
    listner2.start()
    listner3.start()

    sleep(5)

    kill_switch1.set()
    kill_switch2.set()
    kill_switch3.set()

    listner1.join()
    listner2.join()
    listner3.join()

    #because the listners start one after the othe
    #input("edit files then press enter")

    import binascii
    fileList = [file1, file2, file3]
    hexlist = []


    for file_name in fileList:
        

        # Open the file in binary mode and read its contents
        with open(file_name, 'rb') as filee:
            file_contents = filee.read()

        # Convert the binary data to a hexadecimal string
        hex_string = binascii.hexlify(file_contents).decode('utf-8')

        # Print the hexadecimal string
        hexlist.append(hex_string)

    if hexlist[0] == hexlist[1] and hexlist[1] == hexlist[2]:
        print("valid")
    else:
        print("invalid")



def main():
    listner_validate()

    




if __name__ == "__main__":
    main()