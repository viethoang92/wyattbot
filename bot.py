import discord
from discord.ext import commands

TOKEN = 'NTAyNTkwNjE5MDEzNjExNTQw.DqqQHA.Hn7V8ef9xUcHlvInozZ1YwdMhV4'

client = commands.Bot(command_prefix  = 'wyatt')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_message(message):
    author = message.author
    content = message.content
    print('{}: {}'.format(author, content))

@client.event
async def on_message_delete(message):
    author = message.author
    content = message.content
    channel = message.channel
    await client.send_message(channel, '{}: {}'.format(author, content))

client.run(TOKEN)
