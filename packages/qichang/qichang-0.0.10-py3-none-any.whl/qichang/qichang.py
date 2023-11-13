"""
@author: Qichang Zheng
@email: qichangzheng@uchicago.edu
@date: 2023-11-11
@personal website: http://qichangzheng.net
This is a personal API developed by Qichang Zheng. If you have any questions, please feel free to contact me via email.
"""

import requests
from time import sleep
from ping3 import ping

__version__ = '0.0.10'

app_api_dict = {
    "GPT3.5": 'fastgpt-ZadxgXx4pZV4OqSyi7dcYHambSq',
    'GPT4': 'fastgpt-BmDbL0SAmNUcyrRxDK5SF3lApP',
    'stock_api': 'fastgpt-lmiAMrgderiIfidhxQ5HVOD6PJIr3ntpxO4',
    'shannon_test1': 'fastgpt-I8yveuOpvtf5NNjCc4feXkscEQGiKxwH3J'
}

server_dict = {
    'Virginia': '54.159.212.206',
    'Singapore': '47.236.36.36'
}

fastgpt_server = {
    'Virginia': 'http://fastgpt.qichangzheng.net/api/v1/chat/completions',
    'Singapore': 'http://nbgpt.qichangzheng.net/api/v1/chat/completions'
}

class LLM_API:
    def __init__(self):
        self.app_api_dict = {
            "GPT3.5": 'fastgpt-ZadxgXx4pZV4OqSyi7dcYHambSq',
            'GPT4': 'fastgpt-BmDbL0SAmNUcyrRxDK5SF3lApP',
            'stock_api': 'fastgpt-lmiAMrgderiIfidhxQ5HVOD6PJIr3ntpxO4',
            'shannon_test1': 'fastgpt-I8yveuOpvtf5NNjCc4feXkscEQGiKxwH3J',
        }
        self.server_dict = {
            'Virginia': '54.159.212.206',
            'Singapore': '47.236.36.36',
        }
        try:
            self.server = self.select_server()
        except:
            print(f'Auto server selection failed, using default server Virginia, '
                  f'you can also select server manually by setting self.server == "Singapore",'
                  f'available servers: {list(self.server_dict.keys())}')


    def select_server(self):
        # Initialize a dictionary to store ping results
        ping_results = {}

        # Ping each server and store the results
        for server_name, server_ip in server_dict.items():
            ping_result = ping(server_ip)
            if ping_result is not None:
                ping_results[server_name] = ping_result

        # Find the server with the lowest ping
        lowest_ping_server = min(ping_results, key=ping_results.get)
        lowest_ping = ping_results[lowest_ping_server]

        # Print the ping results
        print("Ping")
        for server_name, ping_time in ping_results.items():
            print(f"{server_name}: {ping_time:.2f} ms")

        # Print the server with the lowest ping
        print(f"{lowest_ping_server} with lowest ping ({lowest_ping:.2f} ms) selected.")
        return lowest_ping_server


    def chat(self, app_or_key, message, chatId=None):
        if app_or_key.startswith('fastgpt-'):
            apikey = app_or_key
        else:
            try:
                apikey = app_api_dict[app_or_key]
            except KeyError:
                raise KeyError(f'App {app_or_key} not found, available apps are {list(app_api_dict.keys())}')
        url = fastgpt_server[self.server]
        headers = {
            "Authorization": 'Bearer ' + apikey,
            "Content-Type": "application/json"
        }
        data = {
            "chatId": chatId,
            "stream": False,
            "detail": False,
            "variables": {
                "cTime": "2023/10/18 22:22"
            },
            "messages": [
                {
                    "content": message,
                    "role": "user"
                }
            ]
        }
        while True:
            try:
                response = requests.post(url, headers=headers, json=data).json()['choices'][0]['message']['content']
                break
            except:
                sleep(3)
        return response
