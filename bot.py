import discord
from discord.ext import commands, tasks
import os

TOKEN = 'NzA1Mjc1MTg4Njk0MDg5NzQ4.XqpVrg.X2hBJE4lXdYJoPTS2y4NoZ0q2ko'

client = commands.Bot(command_prefix = '!')

#                           Events
@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.online, activity=discord.Game('!Help for commands'))
	print('Bot is Online.')

#                          Commands

@client.command()
async def load (ctx, extension):
	client.load_extension(f'cogs.{extension}')

@client.command()
async def unload (ctx, extension):
	client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')

client.run(TOKEN)
