import discord
import asyncio
from discord.ext import commands
import botobject

bot = botobject.bot

@bot.command(pass_context=True)
async def status(status):
    await bot.say("Setting " + ctx.message.author.mention + "'s status to " + status)