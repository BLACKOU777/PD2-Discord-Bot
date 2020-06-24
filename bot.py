import discord
import requests
import json
import re
from discord.ext import commands

live_server = 
Test_server = 
client = commands.Bot(command_prefix = '!')
client.remove_command('help')

@client.command(aliases=('Help', 'commands', 'HELP'))
async def help(ctx):
    embed = discord.Embed(title='Available commands', description='--------------------')
    embed.add_field(name="!guides", value="Some useful guides to take a look at", inline=False)
    embed.add_field(name='!mod', value='How to download the Speedrun Mod', inline=False)
    embed.add_field(name='!leaderboard', value='Links to IL leaderboard on speedrun.com', inline=False)
    embed.add_field(name='!user (Speedrun.com name)', value='Links to speedrun.com profile', inline=False)
    embed.add_field(name='!fly', value='Useful Info about the PBSH Glitch', inline=False)
    embed.add_field(name='!tools', value='Useful tools for strat hunting (UNINSTALL BEFORE RUNNING)', inline=False)
    embed.add_field(name='!downpatch', value='Guide on how to install older versions', inline=False)
    embed.add_field(name='!update', value='List of commonly used manifest IDs', inline=False)
    embed.add_field(name='!rng', value='description of how the settings work', inline=False)
    await ctx.send(content=None, embed=embed)

@client.command(aliases=('Guides', 'GUIDES', 'guide', 'Guide'))
async def guides(ctx):
    embed = discord.Embed(title='Useful Guides', description='--------------------')
    embed.add_field(name="Skips, Glitches and Techniques", value="http://steamcommunity.com/sharedfiles/filedetails/?id=769258277", inline=False)
    embed.add_field(name="Speedrunning: Not so fast guide about being fast", value="https://steamcommunity.com/sharedfiles/filedetails/?id=1874134915", inline=False)
    embed.add_field(name="The Long Guide", value="https://steamcommunity.com/sharedfiles/filedetails/?id=267214370", inline=False)
    embed.add_field(name="Installing and Playing Older PAYDAY 2 Updates", value="type !downpatch for how to install olcer versions", inline=False)
    embed.add_field(name="Accurate Weapon Stats", value="https://docs.google.com/spreadsheets/d/15sW5ujghwxsph0xo89vTZbnS_aD7DbKU3CmAFtRBuUI/edit#gid=819903647", inline=False)
    await ctx.send(content=None, embed=embed)

@client.command(aliases=('Mod', 'MOD'))
async def mod(ctx):
    embed = discord.Embed(title='Speedrun Mod', description='--------------------')
    embed.add_field(name="Install Guide", value="https://docs.google.com/document/d/1hXNqUXQKCsmATVWrh2OHY7dIcJ5-Y5v7", inline=False)
    embed.add_field(name='Download', value='https://drive.google.com/drive/folders/11Rbia_oOsEmRZDpzRAKzjUBrEvhjtd9K', inline=False)
    embed.add_field(name='--------------------', value='Required for runs to be verified', inline=False)
    await ctx.send(content=None, embed=embed)

@client.command(aliases=('Leaderboard', 'LEADERBOARD'))
async def leaderboard(ctx):
    embed = discord.Embed(title='LeaderBoard', description='--------------------')
    embed.add_field(name="Individual levels", value="https://www.speedrun.com/pd2", inline=False)
    embed.add_field(name="Full Game Runs", value="https://www.speedrun.com/pd2/full_game", inline=False)
    await ctx.send(content=None, embed=embed)

@client.command(aliases=('User', 'USER'))
async def user(ctx, content):
    msg = str(content).split()
    name = (str(msg)[2:-2])
    base_url = 'https://www.speedrun.com/api/v1/'
    info = requests.get(base_url + 'users?lookup=' + name)
    info_json = info.json()
    for data in info_json['data']:
        id = data['id']
        prof_link = data["weblink"]
        location = data['location']['country']['names']['international']
        join_date = str(data['signup'][8:10])+ '/' + str(data['signup'][5:7]) + '/' + str(data['signup'][0:4])
    wrs = requests.get(base_url + 'users/' + id + '/personal-bests?top=1/game=m1mm7x12' )
    wrs_json = wrs.json()
    place = []
    for data in wrs_json['data']:
        my_dict = {}
        my_dict['place'] = data.get('place')
        place.append(my_dict)
    wr = len(place)
    runs = requests.get(base_url + 'users/' + id + '/personal-bests?/game=m1mm7x12' )
    runs_json = runs.json()
    place = []
    for data in runs_json['data']:
        my_dict = {}
        my_dict['place'] = data.get('place')
        place.append(my_dict)
    runs = len(place)
    embed = discord.Embed()
    embed.set_author(name=name + "'s Speedrun.com Profile", url="https://www.speedrun.com/user/" + name, icon_url="https://www.speedrun.com/themes/user/" + name + "/image.png?version=")
    embed.add_field(name=("Submited Runs"), value= runs, inline=False)
    embed.add_field(name=("World Records:"), value= wr, inline=False)
    embed.add_field(name=("From"), value= location, inline=False)
    embed.add_field(name=("Speedrunning Since"), value= join_date, inline=False)
    await ctx.send(content=None, embed=embed)

@client.command(aliases=('Fly', 'FLY', 'PBSH', 'pbsh'))
async def fly(ctx):
    embed = discord.Embed(title='PBSH', description='--------------------')
    embed.add_field(name="What is it?", value="A glitch which allows faster movement speeds and longer jumps", inline=False)
    embed.add_field(name='How to do it: Speed boost', value='While on a slope spam ESC to get a speed boost', inline=False)
    embed.add_field(name='How to do it: Longer jumps', value='while jumping spam ESC to be able to jump longer distances', inline=False)
    embed.add_field(name='Example', value='https://www.speedrun.com/pd2/run/yl0q89xy', inline=False)
    embed.add_field(name='Extra info', value='Only works between updates: 181-199', inline=False)
    embed.add_field(name='Limit fps to 30 for maximum effect', value='--------------------', inline=False)
    await ctx.send(content=None, embed=embed)

@client.command(aliases=('Tools', 'TOOLS', 'TOOL', 'tool', 'Tool'))
async def tools(ctx):
    embed = discord.Embed(title='Useful Tools', description='--------------------')
    embed.add_field(name="Freecam Mod", value="https://modworkshop.net/mod/16272", inline=False)
    embed.add_field(name='BeardLib', value='https://modworkshop.net/mod/14924', inline=False)
    embed.add_field(name='BeardLib Editor', value='https://modworkshop.net/mod/16837', inline=False)
    embed.add_field(name='--------------------', value='Make sure to uninstall before running', inline=False)
    await ctx.send(content=None, embed=embed)

@client.command(aliases=('DOWNPATCH', 'DownPatch'))
async def downpatch(ctx):
    embed = discord.Embed(title='How to DownPatch to previous versions', description='--------------------')
    embed.add_field(name="Step 1:", value="Download .NET core from microsoft's website (https://dotnet.microsoft.com/download/dotnet-core)", inline=False)
    embed.add_field(name='Step 2:', value='Download DepotDownloader from github (https://github.com/SteamRE/DepotDownloader/releases)', inline=False)
    embed.add_field(name='Step 3:', value='Open the folder containing "DepotDownloader.dll", type "cmd.exe" into the address bar to open command line', inline=False)
    embed.add_field(name='Step 4:', value='Replace [all this stuff] in the command format with the manifest id you want and your steam details', inline=False)
    embed.add_field(name= 'Command Format:', value='dotnet DepotDownloader.dll -app 218620 -depot 218621 -manifest [manifest] -username [steamname] -password [steampassword]', inline=False)
    embed.add_field(name='Guide video', value='https://www.youtube.com/watch?v=44HBxzC_RTg', inline=False)
    embed.add_field(name='--------------------', value="type !update for a list of commonly used manifest id's", inline=False)
    await ctx.send(content=None, embed=embed)

@client.command(aliases=('Update', 'UPDATE'))
async def update(ctx):
    embed = discord.Embed(title="list of ID's for downpatching", description='--------------------')
    embed.add_field(name="U23", value="967468050757548629", inline=False)
    embed.add_field(name='U34', value=' 6441610674699641116', inline=False)
    embed.add_field(name='U47', value='1661252179542596410', inline=False)
    embed.add_field(name='U93', value='7276563325668227980', inline=False)
    embed.add_field(name='U107.1', value='1844026237622139878', inline=False)
    embed.add_field(name='U118', value='3957512153813192307', inline=False)
    embed.add_field(name='U121.1', value='2696759754534894037', inline=False)
    embed.add_field(name='U134.1', value='8311103612103130127', inline=False)
    embed.add_field(name='U163', value='6711418499316411116', inline=False)
    embed.add_field(name='U198.2', value='5832573493242735729', inline=False)
    embed.add_field(name='--------------------', value='need another update??? check the Steamdb and compare it to the wiki to find which update it is', inline=False)
    embed.add_field(name='Steamdb', value='https://steamdb.info/depot/218621/manifests/', inline=False)
    embed.add_field(name='Update History', value='https://payday.fandom.com/wiki/PC_update_history_(Payday_2)', inline=False)
    await ctx.send(content=None, embed=embed)

@client.command(aliases=('RNG', 'Rng'))
async def rng(ctx):
    embed=discord.Embed(title="Rng Modifier settings", description="--------------------")
    embed.set_thumbnail(url="https://lh3.googleusercontent.com/proxy/mVD5zXWY9H3pxkUBYRHLXNoZO-Gg_qDoRH8fKRKw4WhOLs0wXxdQ40OJAGgFJIu93PPJOyQL52jfLgurxT2XEut3pUIDGChP5nclCzb9T5PeAiZPEiz4QbW-RZuRDBwVbIZLsaT8zLF5nwoNUNoJGqDfmqn5GhtO9pY")
    embed.add_field(name="Random", value='keycard has 10 locations that it can spawn' + '\n' + 'First = will always spawn at the "First" Location' + '\n' + 'Last = will always spawn in "Last" Location' + '\n' + 'and so on' + '\n' + '(Keycards, Electric Boxes, computers, manager, etc..)', inline=False)
    embed.add_field(name="Chance", value="you need to cut 2 wires for the alarm using 100% make you can cut any wire and the alarm will not go off" + '\n' + '(cutting wires, codes, etc...)', inline=False)
    embed.add_field(name="Heist Specific settings", value="Adjust things specific to the heist. (example G.O bank vault open)", inline=False)
    await ctx.send(content=None, embed=embed)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('!help for commands'))
    print('Bot is online')

client.run(live_server)
