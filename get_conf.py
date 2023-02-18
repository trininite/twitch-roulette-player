import json


def get_user_info() -> dict:
    with open('devs_conf.json') as json_file:
        data = json.load(json_file)
        
        
        user_info = data["user_info"][0]
        
        return user_info

def get_server_info() -> dict:
    with open('devs_conf.json') as json_file:
        data = json.load(json_file)
        
        
        server_info = data["server_info"][0]
        
        return server_info

def get_bot_info() -> dict:
    with open('devs_conf.json') as json_file:
        data = json.load(json_file)
        
        
        bot_info = data["bot_info"][0]
        
        return bot_info