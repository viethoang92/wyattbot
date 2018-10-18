import discord
from discord.ext import commands

TOKEN = 'NTAyNTkwNjE5MDEzNjExNTQw.DqqQHA.Hn7V8ef9xUcHlvInozZ1YwdMhV4'

client = commands.Bot(command_prefix  = 'wyatt')
prefix = "wyatt"

@client.event
async def on_ready():
    print('Bot is ready.')

'''
#logs the users messages
@client.event
async def on_message(message):
    author = message.author
    content = message.content
    print('{}: {}'.format(author, content))
'''
'''
#reposts message when message is deleted
@client.event
async def on_message_delete(message):
    author = message.author
    content = message.content
    channel = message.channel
    await client.send_message(channel, '{}: {}'.format(author, content))
'''

@client.event
async def on_message(message):
    channel = message.channel
    if message.content.startswith(prefix + ' ping'):
        await client.send_message(channel,  'Pong!')

    if message.content.startswith(prefix + ' say'):
        msg = message.content.split()
        output = ''
        for word in msg[1:]:
            output += word 
            output += ' '
            await client.send_message(channel, output)

client.run(TOKEN)
