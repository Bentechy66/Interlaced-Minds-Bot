#Import libraries
import discord #The Discord API
import asyncio #Used for await and async
from discord.ext import commands #Used to define commands and some other things

#Import other dependencies created by Ben
import credentials #The Bot's Secret Key
import online #The CheckOnlineUsers function
import botobject #The global bot object
import points #The points system
import links #sending specific links
import sys
import os




bot = botobject.bot #import the bot object


bot.loop.create_task(online.CheckOnlineUsers()) #create coroutine

@bot.command()
async def about():
     """About and credits"""
     msgc = await bot.say("**ABOUT / Credits**\nThis bot shows local time in specific timezones and also handles points.\nWritten by BenTechy66 on Discord.\n\n**Credits**\nBen - *wrote the bot*\nMcTrees - *hosting the bot*\nOpen Source Libraries:Discord.py, asyncio, pytz.")
     #await bot.add_reaction(msgc, "tick:326377249223999498")

@bot.command(pass_context=True)
async def debug(ctx):
    """[DEBUG] Do not use unless you know what you're doing"""
    if "-r" in ctx.message.content:
        python = sys.executable
        os.execl(python, python, * sys.argv)
    if "-s" in ctx.message.content:
        await bot.say("If you are receiving this message, then the bot is online.\nLast online update: " + str(online.updateTime) + "GMT")

   
bot.run(credentials.BotSecret) #run bot
