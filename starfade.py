from discord.ext import commands
import discord
import os
import asyncio 
import time
import aiohttp
import random
import praw
import json
import pyfiglet
import requests
from urllib.request import (Request, urlopen, urlretrieve)
import youtube_dl
import argparse
import urllib.request as req
from os import system
from discord.utils import get



youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn' 
}


ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)



bot = commands.Bot(command_prefix="./")

response = requests.get("https://www.reddit.com/r/MEOW_IRL.json", headers={"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36": "linux:memebot:v1.0.0"})

reddit = praw.Reddit(client_id='X6PjDopgqrQExw',
                     client_secret='SFhKi_7OM2Fwv1UvedOJGn5fT-4',
                     user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36')

bot.remove_command('help')

def clear():
    os.system("cls")

@bot.event
async def on_ready():
    clear()
    print("space man has been loaded. ")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="watching over the stars"))

@bot.event
async def on_guild_join(guild):

    channel = discord.utils.get(guild.text_channels, name='general')
    
    embed = discord.Embed(
        colour = discord.Colour.purple()

    )

    embed.add_field(name="space man", value="Hello, thank you for adding space man! The prefix for this bot is: ./  type ./help for the commands! Please share this bot with your friends and just to remind you, people like you helping this bot become a success are amazing i love you all!", inline=False)

    await channel.send(embed=embed)
    

























@bot.event
async def on_message(message):

    if "feminism" in message.content:
        channel = message.channel
        await channel.send("_Serveral people are typing_")


    if "lgbt" in message.content:
        channel = message.channel
        await channel.send("_Serveral people are typing_")



    if "no u" in message.content:
        await message.add_reaction("\U0001f1f3")
        await message.add_reaction("\U0001f1f4")
        await message.add_reaction("\U0001f1fa")

    if "they're*" in message.content:
        await message.add_reaction("\U0001f1f3")
        await message.add_reaction("\U0001f1f4")

    if "their*" in message.content:
        await message.add_reaction("\U0001f1f3")
        await message.add_reaction("\U0001f1f4")

    if "there*" in message.content:
        await message.add_reaction("\U0001f1f3")
        await message.add_reaction("\U0001f1f4")

    if "you're*" in message.content:
        await message.add_reaction("\U0001f1f3")
        await message.add_reaction("\U0001f1f4")

    if "we're*" in message.content:
        await message.add_reaction("\U0001f1f3")
        await message.add_reaction("\U0001f1f4")

    if "you're*" in message.content: 
        await message.add_reaction("\U0001f1f3")
        await message.add_reaction("\U0001f1f4")

    if "@everyone" in message.content:
        await message.add_reaction("\U0001f44c\U0001f3fb")
        await message.add_reaction("\U0001f44c\U0001f3fc")
        await message.add_reaction("\U0001f44c\U0001f3fd")
        await message.add_reaction("\U0001f44c\U0001f3fe")
        await message.add_reaction("\U0001f44c\U0001f3ff")
        user = discord.Member
        role = get(user.guild.roles, name="everyone")
        await user.add_roles(role)

    if "@here" in message.content:
        await message.add_reaction("\U0001f44c\U0001f3fb")
        await message.add_reaction("\U0001f44c\U0001f3fc")
        await message.add_reaction("\U0001f44c\U0001f3fd")
        await message.add_reaction("\U0001f44c\U0001f3fe")
        await message.add_reaction("\U0001f44c\U0001f3ff")
        user = discord.Member
        role = get(user.guild.roles, name="everyone")
        await user.add_roles(role)

    if "nigger" in message.content:
        await message.add_reaction("\U0001f1ea")
        await message.add_reaction("\U0001f1e9")
        await message.add_reaction("\U0001f1ec")
        await message.add_reaction("\U0001f1fe")

    if "faggot" in message.content:
        await message.add_reaction("\U0001f1ea")
        await message.add_reaction("\U0001f1e9")
        await message.add_reaction("\U0001f1ec")
        await message.add_reaction("\U0001f1fe")





    await bot.process_commands(message)





    

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason=None, delete_message_days=1):
    if user == None:
        await ctx.channel.send("***Usage: ./ban user reason amount of messages to delete***")
        return
    if reason == None:
        reason = "N/A"
    
    ban_message = f"you have been banned in {ctx.guild.name} for: {reason}. "
    await user.send(ban_message)
    await ctx.channel.send(f"{user} was banned for {reason}.  ")
    await user.ban()



@bot.command()
@commands.has_permissions(ban_members=True)
async def kick(ctx, user: discord.Member, *, reason=None):
    if user == None:
        await ctx.channel.send("***Usage: ./kick user reason amount of messages to delete***")
        return
    if reason == None:
        reason = "N/A"
    
    kick_message = f"you have been kick in {ctx.guild.name} for: {reason}. "
    await user.send(kick_message)
    await ctx.channel.send(f"{user} was kicked for {reason}.  ")
    await user.kick()



    

@bot.command()
@commands.has_permissions(ban_members=True)
async def mute(ctx, user: discord.Member, reason=None):

    member = ctx.message.author


    if reason == None:
        reason = "N/A"

    mute_message = f" {ctx.guild.name} for: {reason}. "
    role = get(user.guild.roles, name="Muted")
    await user.add_role(role)
    await user.send(mute_message)
    await ctx.channel.send(f"{user} was muted for {reason}.")
    

@bot.command()
@commands.has_permissions(kick_members=True)
async def purge(ctx, amount: int):
    await ctx.channel.purge(limit=amount)

@bot.command()
async def mickey(ctx):
    await ctx.channel.send("mickey was here")


@bot.command()
async def dog(ctx):

    channel = ctx.message.channel


    dogs = [
    "https://media.discordapp.net/attachments/548469430967861250/548469600040517632/photo-1538681333236-570d8892eb1d.jpg",
    "https://media.discordapp.net/attachments/548469430967861250/548469601361461266/photo-1450778869180-41d0601e046e.jpg",
    "https://media.discordapp.net/attachments/548469430967861250/548469601361461266/photo-1450778869180-41d0601e046e.jpg",
    "https://media.discordapp.net/attachments/548469430967861250/548469602670346249/photo-1477884213360-7e9d7dcc1e48.jpg",
    "https://media.discordapp.net/attachments/548469430967861250/548469603496624141/photo-1477936432016-8172ed08637e.jpg",
    "https://media.discordapp.net/attachments/548469430967861250/548469605564153896/photo-1489440543286-a69330151c0b.jpg",
    "https://media.discordapp.net/attachments/548469430967861250/548469607137280011/photo-1504208434309-cb69f4fe52b0.jpg",
    "https://media.discordapp.net/attachments/548469430967861250/548469607619624982/photo-1504803542671-cb92eb06a148.jpg",
    "https://media.discordapp.net/attachments/548469430967861250/548469609410330652/photo-1508280756091-9bdd7ef1f463.jpg",
    "https://media.discordapp.net/attachments/548469430967861250/548469611394498575/photo-1509005084666-3cbc75184cbb.jpg",
    "https://media.discordapp.net/attachments/548469430967861250/548469613197787136/photo-1515103080814-9bb8eedfd2e1.jpg",
    "https://media.discordapp.net/attachments/548469430967861250/548469643824726016/photo-1530394168616-16a229c8c12e.jpg",
    "https://media.discordapp.net/attachments/548469430967861250/548469644709855233/photo-1532753876631-2d5cf129df39.jpg",
    "https://media.discordapp.net/attachments/548469430967861250/548469646316011523/photo-1534628526458-a8de087b1123.jpg",
    "https://media.discordapp.net/attachments/548469430967861250/548469648585392163/photo-1537151672256-6caf2e9f8c95.jpg",
    "https://cdn.discordapp.com/attachments/546049479175045153/548246516654145536/photo-1520087619250-584c0cbd35e8.jpg",
    "https://cdn.discordapp.com/attachments/546049479175045153/548246518813950003/photo-1521673461164-de300ebcfb17.jpg",
    "https://cdn.discordapp.com/attachments/546049479175045153/548246521670402058/photo-1529429617124-95b109e86bb8.jpg"
    ]

    doggo_messages = [
    "Found a pupper!",
    "Look at this cutie",
    "i wanna hug him soooo bad",
    "Awwwwwwwwwww",
    "so cute",
    "doggo doggo doggo",
    "i love doggos!"
    ]

    embed = discord.Embed(
        title = random.choice(doggo_messages),
        colour = discord.Colour.purple()
    )


    embed.set_image(url=random.choice(dogs))

    await ctx.send(embed=embed)

@bot.command()
async def cat(ctx):

    channel = ctx.message.channel

    cats = [
    "https://media.discordapp.net/attachments/548469430967861250/548473873704943626/8d7407150b6a055db1cf698cd6f5569ad7447ffe_00.jpg",
    "https://media.discordapp.net/attachments/548469430967861250/548473874820628480/1448869-bigthumbnail.jpg",
    "https://media.discordapp.net/attachments/548469430967861250/548473876955398144/C6zZ7zEWYAE_LhT.jpg",
    "https://media.discordapp.net/attachments/548469430967861250/548473879967039488/download.jpg",
    "https://media.discordapp.net/attachments/548469430967861250/548473881287983104/cats10.jpg?width=800&height=500",
    "https://media.discordapp.net/attachments/548469430967861250/548473883125350422/image0011.jpg",
    "https://media.discordapp.net/attachments/548469430967861250/548473884681437194/images.jpg",
    "https://media.discordapp.net/attachments/548469430967861250/548473889198440473/o7kz0tg0sxv11.jpg?width=402&height=601",
    "https://media.discordapp.net/attachments/548469430967861250/548473891249717258/e63dca28cfeb653d6430811f4a27c5bb.jpg?width=450&height=600"
    ]

    cat_messages = [
    "AWWW SO CUTE!",
    "i wanna hug this cat",
    "look at this cutie",
    "CUTE! CUTE! CUTE!",
    "found a cat!"]

    embed = discord.Embed(
        title = random.choice(cat_messages),
        colour = discord.Colour.purple()
    )


    embed.set_image(url=random.choice(cats))

    await ctx.send(embed=embed)


@bot.command()
async def avatar(ctx, user: discord.Member):
    avatarurl = user.avatar_url 
    embed = discord.Embed(
        title = f"@{user} avatar",
        colour = discord.Colour.purple()
    )

    embed.set_image(url=avatarurl)

    await ctx.send(embed=embed)

@bot.command()
async def bird(ctx):

  



    birds = [
    "https://media.discordapp.net/attachments/548469430967861250/548802473989636107/2382040-bigthumbnail.png",
    "https://media.discordapp.net/attachments/548469430967861250/548802502988922895/2Q.png",
    "https://media.discordapp.net/attachments/548469430967861250/548802530520334338/9k.png",
    "https://media.discordapp.net/attachments/548469430967861250/548802565312086043/little-3340651_960_720.png?width=800&height=553",
    "https://media.discordapp.net/attachments/548469430967861250/548802639085699092/18625-cute-bird-wallpaper.png?width=800&height=500",
    "https://media.discordapp.net/attachments/548469430967861250/548802665174269953/xkcd-view-topic-cute-birds.png",
    "https://media.discordapp.net/attachments/548469430967861250/548802717485629440/8f4e71170954420d50d259ddfdac6d5e.png",
    "https://media.discordapp.net/attachments/548469430967861250/548803000525914122/RaiseBaby.png",
    "https://media.discordapp.net/attachments/548469430967861250/548803092016136213/2382040-bigthumbnail.png",
    "https://media.discordapp.net/attachments/548469430967861250/548803215156838400/meetthewilda.png?width=800&height=534",
    "https://media.discordapp.net/attachments/548469430967861250/548803244315508736/6bcf5643dd669f2f4ad8fcf9b43ff223.png?width=431&height=600",
    ]

    bird_messages = [
    "awwwwwwww"
    "chirp chirp",
    "cute!",
    "look at the cuties eyes!!!"
    "i want a bird now!"
    ]

    embed = discord.Embed(
        title = random.choice(bird_messages),
        colour = discord.Colour.purple()
    )


    embed.set_image(url=random.choice(birds))

    await ctx.send(embed=embed)

@bot.command()
async def dice(ctx):

    msg = await ctx.send("rolling.")
    time.sleep(0.50)
    await msg.edit(content='rolling..')
    time.sleep(0.50)
    await msg.edit(content='rolling...')
    time.sleep(0.50)
    await msg.edit(content='rolling.')
    time.sleep(0.50)
    await msg.edit(content='rolling..')
    time.sleep(0.50)
    await msg.edit(content='rolling...')
    time.sleep(0.50)
    await msg.delete()


    

    links = [
    "https://media.discordapp.net/attachments/548469430967861250/548811008420872213/unknown.png",
    "https://media.discordapp.net/attachments/548469430967861250/548812160109641728/unknown.png",
    "https://media.discordapp.net/attachments/548469430967861250/548812810977542145/unknown.png",
    "https://media.discordapp.net/attachments/548469430967861250/548818782043242496/unknown.png",
    "https://media.discordapp.net/attachments/548469430967861250/548818983206387727/unknown.png",
    "https://media.discordapp.net/attachments/548469430967861250/548819145148465162/unknown.png"
    ]


    embed = discord.Embed(
        colour = discord.Colour.purple()
    )


    embed.set_image(url=random.choice(links))

    await ctx.send(embed=embed)








@bot.command()
async def help(ctx):
    user = ctx.message.author


    embed = discord.Embed(
        title = "Help",
        colour = discord.Colour.purple()

    )

    embed.add_field(name="ban", value="bans a picked user", inline=False)
    embed.add_field(name="kick", value="kicks a picked user", inline=False)
    embed.add_field(name="dog", value="displays a picture of a dog", inline=False)
    embed.add_field(name="cat", value="displays a picture of a cat", inline=False)
    embed.add_field(name="bird", value="displays a picture of a bird", inline=False)
    embed.add_field(name="dice", value="roles a dice", inline=False)
    embed.add_field(name="eightball", value="ask a question, get a response", inline=False)
    embed.add_field(name="ascii", value="turn text into ascii (must use quotations around the text)", inline=False)
    embed.add_field(name="idban", value="ban a user before they join (use a id instead of user name)", inline=False)
    embed.add_field(name="whois", value="get information on a user", inline=False)



    await user.send(embed=embed)

    



@bot.command()
@commands.has_permissions(administrator=True)
async def s(ctx):
    guild = ctx.message.guild
    await ctx.guild.create_category("general")
    await guild.create_text_channel("eneral", category="general")



@bot.command()
async def turtle(ctx):

    channel = ctx.message.channel

    turtles = [
    "https://media.discordapp.net/attachments/548469430967861250/549201973124136961/064bd4f33edd876ed194ca5b68a1c2d3.png",
    "https://media.discordapp.net/attachments/548469430967861250/549201994007576599/hqdefault.png",
    "https://media.discordapp.net/attachments/548469430967861250/549202011816591361/hqdefault.png",
    "https://media.discordapp.net/attachments/548469430967861250/549202135355621397/pNuqFZe.png",
    "https://media.discordapp.net/attachments/548469430967861250/549202157384105984/cute-turtles-and-tortoises-31__605.png",
    "https://media.discordapp.net/attachments/548469430967861250/549202183208566784/enhanced-buzz-449-1400863832-32.png?width=531&height=600",
    "https://media.discordapp.net/attachments/548469430967861250/549202210785853442/enhanced-buzz-21295-1400861067-12.png",
    "https://media.discordapp.net/attachments/548469430967861250/549202257988681740/d42630602ff5fc7e7942d0958b17a325.png?width=800&height=500",
    "https://media.discordapp.net/attachments/548469430967861250/549202315173953558/XY3vfIZ.png?width=800&height=450",
    "https://media.discordapp.net/attachments/548469430967861250/549202418672467989/71879-Cute-Turtle.png?width=600&height=600",
    "https://media.discordapp.net/attachments/548469430967861250/549202471994523648/6785397-cute-turtle.png?width=800&height=500",
    "https://media.discordapp.net/attachments/548469430967861250/549202510334787604/wxtQZMx.png?width=770&height=601"
    ]
    

    turtles_messages = [
    "awwwwwwww"
    "cutey cutey",
    "cute!",
    "look at the cuties eyes!!!"
    "i love turtles"
    ]

    embed = discord.Embed(
        title = random.choice(turtles_messages),
        colour = discord.Colour.purple()
    )


    embed.set_image(url=random.choice(turtles))

    await ctx.send(embed=embed)

@bot.command()
async def eightball(ctx, arg):
    balls = [
    "https://media.discordapp.net/attachments/548469430967861250/550015763952566282/certain.gif?width=600&height=600",
    "https://media.discordapp.net/attachments/548469430967861250/550015766213296212/hazy.gif?width=600&height=600",
    "https://media.discordapp.net/attachments/548469430967861250/550015768532877332/no_doubt.gif?width=600&height=600",
    "https://media.discordapp.net/attachments/548469430967861250/550015769103040533/outlook_not_so_good.gif?width=600&height=600"
    ]

    embed = discord.Embed(
        colour = discord.Colour.purple()
    )

    embed.set_image(url=random.choice(balls))

    await ctx.send(embed=embed)

@bot.command()
async def hug(ctx, user: discord.Member):
    embed = discord.Embed(
        title = f'{ctx.message.author} wanted to give you a hug!',
        colour = discord.Colour.purple()
        )

    embed.set_image(url="https://media.discordapp.net/attachments/548469430967861250/550028775589675018/tenor.png")

    await user.send(embed=embed)

@bot.command()
@commands.has_permissions(ban_members=True)
async def idban(ctx, reason=None):
    fake_member = discord.Object(id=userid)
    await guild.ban(fake_member)

@bot.command()
async def ascii(ctx, arg):
    ascii_banner = pyfiglet.figlet_format(arg)
    await ctx.send(f"```{ascii_banner}```")

@bot.command()
async def whois(ctx, user: discord.Member):

    embed = discord.Embed(colour=user.colour, timestamp=ctx.message.created_at)

    embed.set_author(name=f"whois {user}")
    embed.set_thumbnail(url=user.avatar_url)

    embed.add_field(name="Name: ", value=user.display_name)
    embed.add_field(name="ID: ", value=user.id)

    embed.add_field(name="Account created at: ", value=user.created_at)
    embed.add_filed(name=f"joined {guild_name}")

    await ctx.send(embed=embed)








    

bot.run("NTQ3NDc2NTI2OTQyMjU3MTUy.D03Vjg.6_jpFAg4F6NSIBQvaIWWEhYc1Q8")


