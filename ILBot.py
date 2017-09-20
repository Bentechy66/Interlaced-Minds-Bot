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

@bot.command()
async def about(Aliases:["credits"]):
    msgc = await bot.say("**ABOUT / Credits**\nThis bot shows local time in specific timezones and also handles points.\nWritten by BenTechy66 on Discord.\n\n**Credits**\nBen - *wrote the bot*\nMcTrees - *hosting the bot*\nOpen Source Libraries:Discord.py, asyncio, pytz.")
    await bot.add_reaction(msgc, "tick:326377249223999498")
  
@bot.event
async def on_reaction_add(reaction, user):
    if reaction.me == False:
        await bot.send_message(reaction.message.channel, "you reacted!")
    await bot.send_message(reaction.message.channel, "Reaction.me status @ discord.Object:0x3326f4 " + str(reaction.me))
    


   
bot.run(credentials.BotSecret) #run bot
