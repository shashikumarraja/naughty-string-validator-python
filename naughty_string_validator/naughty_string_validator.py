import json
import os

# print os.listdir(r'naughty_string_db')
with open(r'naughty_string_db/blns.json', 'r') as f:
    naughty_string_list = json.loads(f.read())
with open(r'naughty_string_db/emoji.json', 'r') as f:
    emoji_list = json.loads(f.read())

def get_naughty_string_list():
    """ Get entire naughty string list """
    return naughty_string_list

def get_emoji_list():
    """ Get entire naughty string list """
    return emoji_list