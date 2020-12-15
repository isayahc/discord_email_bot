from os import environ
import requests 


def send_message(message:str)->None:
    """[summary]

    Args:
        data (str): [description]
    """
    # hook_url = environ['']
    hook_url = environ.get('discord_link')
    msg = {
  "content": message
}
    x = requests.post(hook_url, data = msg)


    