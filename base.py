import requests,os
class send_dm_base():
    def __init__(self,token):
        self.token=token
    def ez_send(self,message:str,to_id:int):
        headers = {
            'authority': 'discord.com',
            'accept': '*/*',
            'accept-language': 'ja,en-US;q=0.9,en;q=0.8',
            'authorization': self.token,
            'content-type': 'application/json',
            'origin': 'https://discord.com',
            'referer': f"https://discord.com/channels/@me/{str(to_id)}",
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            'x-debug-options': 'bugReporterEnabled',
            'x-discord-locale': 'ja'
        }

        json_data = {
            'content': message,
            'tts': False
        }

        response = requests.post(f"https://discord.com/api/v9/channels/{str(to_id)}/messages", headers=headers, json=json_data)
        if response.status_code!=200:
            print("失敗")
            print(response.status_code)
            print(response.json())
        else:
            None
        #print(to_id)
    
    def e_send(self,to_id:int):
        headers = {
            'accept': '*/*',
            'accept-language': 'ja,en-US;q=0.9,en;q=0.8',
            'authorization': self.token,
            'origin': 'https://discord.com',
            'referer': f"https://discord.com/channels/@me/",
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'content-type': 'application/json',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            'x-debug-options': 'bugReporterEnabled',
            'x-discord-locale': 'ja'
        }
        url = "https://discord.com/api/v9/users/@me/channels"
        data = {
            'recipients': [
                str(to_id),
            ]
        }
        import json
        data=json.dumps(data)
        response = requests.post(url, data=data, headers=headers)
        resp = response.json()
        if response.status_code!=200:
            return("error")
        return(int(resp["id"]))
    
    def typing(self,channel_id:int):
        headers = {
            'authority': 'discord.com',
            'accept': '*/*',
            'accept-language': 'ja,en-US;q=0.9,en;q=0.8',
            'authorization': self.token,
            'origin': 'https://discord.com',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            'x-debug-options': 'bugReporterEnabled',
            'x-discord-locale': 'ja'
        }

        response = requests.post(f"https://discord.com/api/v9/channels/{str(channel_id)}/typing", headers=headers)
        print(f"typing:{response.status_code}")

class send_message():
    def __init__(self,token):
        self.token=token
    def send(self,message:str,send_to_id:int,dm=False):
        if dm==True:
            base_data_send=send_dm_base(self.token)
            base_to_id_data=base_data_send.e_send(send_to_id)
            if base_to_id_data=="error":
                print("IDが間違っています。")
                return
            base_data_send.ez_send(message,base_to_id_data)
        else:
           base_data_send=send_dm_base(self.token)
           base_data_send.ez_send(message,send_to_id)
    
    def typing(self,channel_id:int):
        base_data_typing=send_dm_base(self.token)
        base_data_typing.typing(channel_id)
    
    def get_dm_id(self,user_id:int):
        base_data_get=send_dm_base(self.token)
        base_to_id_data=base_data_get.e_send(user_id)
        if base_to_id_data=="error":
            print("IDが間違っています。")
            return
        return base_to_id_data

class joiner():
    def __init__(self,token):
        self.token=token
    def join(self,invite_code:str):
        invite_code=invite_code.replace("https://discord.gg/","")
        headers = {
            'authority': 'discord.com',
            'accept': '*/*',
            'accept-language': 'ja,en-US;q=0.9,en;q=0.8',
            'authorization': self.token,
            'cookie': f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
            'origin': 'https://discord.com',
            'referer': 'https://discord.com/channels/@me',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            'x-debug-options': 'bugReporterEnabled',
            'x-discord-locale': 'ja'
        }


        response = requests.post(f"https://discord.com/api/v9/invites/{invite_code}",headers=headers, json={})
        print(response.status_code)
        if response.status_code==400:
            print("captcha")
