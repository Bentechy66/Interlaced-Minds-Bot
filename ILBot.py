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



#setting points
@bot.command(pass_context=True)
async def setpoints(ctx, mention, pointsv):
    try:
        name = str(ctx.message.mentions[0])
    except:
        await bot.say("something screwed up, check your formatting")
        return
    print("setting points to " + pointsv + " for " + name)
    
    if "drop" in ctx.message.content.lower():
        await bot.say("really? **REALLY?**")
        return
        
    roles = []
    for role in ctx.message.author.roles:
        roles.append(role.name)
        
        
    if "PointMaster" in roles:
        errorlevel = points.SetPoints(name, pointsv)
        await bot.add_reaction(ctx.message, "tick:326377249223999498")
    else:
        await bot.add_reaction(ctx.message, "nope:326377249274068992")

        
#setting points
@bot.command(pass_context=True)
async def addpoints(ctx, mention, pointsv):
    try:
        name = str(ctx.message.mentions[0])
    except:
        await bot.say("something screwed up, check your formatting")
        return
    print("adding " + pointsv + " points to " + name)
    
    if "drop" in ctx.message.content.lower():
        await bot.say("really? **REALLY?**")
        return
        
    roles = []
    for role in ctx.message.author.roles:
        roles.append(role.name)
        
        
    if "PointMaster" in roles:
        errorlevel = points.AddPoints(name, pointsv)
        await bot.add_reaction(ctx.message, "tick:326377249223999498")
    else:
        await bot.add_reaction(ctx.message, "nope:326377249274068992")
    
    
    

    
bot.run(credentials.BotSecret) #run bot
