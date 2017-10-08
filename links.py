import discord
import asyncio
from discord.ext import commands
#import botobject
import botobject


bot = botobject.bot

@bot.command(pass_context=True)
async def link(ctx, link):
    """Get the link for things to do with the team"""
    if "-f" in ctx.message.content:
        if discord.utils.get(ctx.message.author.roles, name='Moderator'):
            force = True
        else:
            await bot.say("You don't have permission to use the -s argument! You must be **Moderator**!")
    else:
        force = False
        
    if link.lower() == "gdrive":
        links = []
        if discord.utils.get(ctx.message.author.roles, name='Composer') or force == True:
            links.append("Audio link: https://drive.google.com/drive/folders/0BzydCYAI71huQWx1c3hGb0FxRGc?usp=sharing")
        if discord.utils.get(ctx.message.author.roles, name='Design Team') or force == True:
            links.append("Design link: https://drive.google.com/drive/folders/0BzydCYAI71huQzE3QWt3VW1ueEE?usp=sharing")
        if discord.utils.get(ctx.message.author.roles, name='Commands') or force == True:
            links.append("Commands link: https://drive.google.com/drive/folders/0BzydCYAI71huNkRMeVpObVVubFE?usp=sharing")
        if discord.utils.get(ctx.message.author.roles, name='Writer') or force == True:
            links.append("Writing link: https://drive.google.com/drive/folders/0BzydCYAI71huNjNwYk9HWXhXSkk?usp=sharing")
        if discord.utils.get(ctx.message.author.roles, name='Modeller') or discord.utils.get(ctx.message.author.roles, name='Texturer') or force == True:
            links.append("Modelling / Texture link: https://drive.google.com/drive/folders/0BzydCYAI71huYy00SGVIcnZ6Z0U?usp=sharing")
        if discord.utils.get(ctx.message.author.roles, name='PvZ') or force == True:
            links.append("PvZ link: https://drive.google.com/drive/folders/0BzydCYAI71huanNwOVdRd0tQMGM?usp=sharing")
        if discord.utils.get(ctx.message.author.roles, name='Moderator') or force == True:
            links.append("PvZ link: https://drive.google.com/drive/folders/0BzydCYAI71huanNwOVdRd0tQMGM?usp=sharing") 
        if discord.utils.get(ctx.message.author.roles, name='Video Editor') or discord.utils.get(ctx.message.author.roles, name='Graphics') or force == True:
            links.append("PvZ link: https://drive.google.com/drive/folders/0BzydCYAI71huUU1SeWNSZUVDY3c?usp=sharing") 
        
            
        await bot.add_reaction(ctx.message, "tick:326377249223999498")
        
        embed = discord.Embed(color=0x2c68b2)
        embed.set_author(name="G Drive Links", icon_url="http://www.freeiconspng.com/uploads/links-icon-1.png")
        
        for link in links:
            parts = link.split(":")
            embed.add_field(name=parts[0], value=parts[1] + ":" + parts[2])
            
        await bot.send_message(ctx.message.author, embed=embed)   
    else:
        await bot.say("Need a link argument (eg !link gdrive)")    
        
    force = False