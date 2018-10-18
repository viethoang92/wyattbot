import discord
from discord.ext import commands

TOKEN = 'NTAyNTkwNjE5MDEzNjExNTQw.DqqQHA.Hn7V8ef9xUcHlvInozZ1YwdMhV4'

client = commands.Bot(command_prefix  = 'wyatt')

@client.event
async def on_ready():
    print('Bot is ready.')

client.run(TOKEN)