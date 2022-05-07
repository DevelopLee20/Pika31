import discord
from discord.ext import commands

'''variable
app_status : your Application's status
command_word : Application's command word
'''
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