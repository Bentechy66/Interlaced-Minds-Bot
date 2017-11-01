import discord
import asyncio
from discord.ext import commands
import botobject
holiday = []

bot = botobject.bot

@bot.command(pass_context=True)
async def status(ctx, status):
    await bot.say("Setting " + ctx.message.author.mention + "'s status to " + status)
    if status == "holiday":
        holiday.append(str(ctx.message.author))
    elif status == "home":
        holiday.remove(str(ctx.message.author))
    else:
        await bot.say("Valid Statuses:\n'home' and 'holiday'")
        
    #print(holiday)
    
def GetStatus(user):
    print(user)
    if user in holiday:
        return("On Holiday")
    else:
        return("At Home")
		