import discord
from discord.ext import commands, tasks

TOKEN = 'NzA1Mjc1MTg4Njk0MDg5NzQ4.XqpVrg.X2hBJE4lXdYJoPTS2y4NoZ0q2ko'

client = commands.Bot(command_prefix = '!')

#                           Events
@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.online, activity=discord.Game('!Help for commands'))
	print('Bot is Online.')

#                          Commands

client.run(TOKEN)
