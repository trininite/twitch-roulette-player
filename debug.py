
import socket
import irc_utils
import json
import get_conf
from time import sleep as sleep


"""
import json

with open('devs_conf.json') as json_file:
    data = json.load(json_file)
    
    
user_info = data["user_info"][0]

print(user_info["nickname"])
"""

def main():

    user_info = get_conf.get_user_info()

    print(user_info)



if __name__ == "__main__":
    main()