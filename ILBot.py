#Import libraries
import discord #The Discord API
import asyncio #Used for await and async
from discord.ext import commands #Used to define commands and some other things

#Import other dependencies created by Ben
import credentials #The Bot's Secret Key
import online #The CheckOnlineUsers function
import botobject #The global bot object
import points #The points system




bot = botobject.bot #import the bot object


bot.loop.create_task(online.CheckOnlineUsers()) #create coroutine

    
bot.run(credentials.BotSecret) #run bot
