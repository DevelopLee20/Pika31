'''note
discord forum : https://discord.com/developers/applications
version : 1.0.1
latest updated : 2022-05-08 01:28

patch note
1.0.0 : start discord bot
1.0.1 : Add nest_asyncio code
'''

# event loop off in jupyter notebook
import nest_asyncio
nest_asyncio.apply()

import discord
import My_token as token
from discord.ext import commands

'''variable
app_token : Application Token
app_status : your Application's status
command_word : Application's command word
'''
app_token = token.get_token()
app_status = 'Test Mode'
command_word = '!'

'''functions
getting_started : setting bot's status and return bot instance
'''
def getting_started():
    status = discord.Game(app_status)
    return commands.Bot(
        command_prefix=command_word,
        status=discord.Status.online,
        activity=status,
        help_command= None)

'''Main Code
'''
if __name__ == "__main__":
    bot = getting_started()
    print('starting bot')
    bot.run(app_token)