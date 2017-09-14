import discord
import asyncio
from discord.ext import commands
import botobject
import checktz

bot = botobject.bot

def is_me(m):
    return m.author == bot.user

async def CheckOnlineUsers():
    #
    #
    #User defined variables
    #channel id - The channel the bot should send in
    chid = "357557717432401921"
    blacklist = ['BenBot#4911', 'Interlaced Minds Official Bot#1706', 'Rythm#3722']
    # # # # # # # # # # # #
    #
    #
    #
    #Parts after this not user servicable!
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    await bot.wait_until_ready() #wait until bot is initialized
    #handle permissions
    try:
        deleted = await bot.purge_from(bot.get_channel(chid), limit=100, check=is_me) #delete previous messages
    except:
        await bot.send_message(bot.get_channel(chid), "tried to delete previous message but failed.") #failed to delete previous messages
    
    
    message = "none"  #set to none on first run to send message instead of editing it
    print("coroutine began") #Debug info
    
    #
    #Begin loop
    #
    while not bot.is_closed:
        embed = discord.Embed(color=0x2c68b2) #Clear and create embed object
        embed.set_author(name="Online Users", icon_url="https://cdn.discordapp.com/emojis/261471113509339137.png") #Set embed title
        online = [] #Clear and create online list
        members = list(bot.get_all_members()) #Get list of members
        members = list(set(members)) #Remove duplicates
        for member in members: #For each member
            if str(member.status) == 'online' or str(member.status) == 'dnd': #Check if online
                online.append(str(member)) #Add username to online list
                
        for person in blacklist: #blacklist
            online.remove(person)
        
        online = sorted(online)
        
        for user in online: #For each user in online list
            time = await checktz.GetTime(user)
            server = bot.get_server("297674982773882892")
            member = server.get_member_named(str(user))
            embed.add_field(name=str(user), value=time + "\n" + str(member.top_role)) #add them to the embed
        
        
        
        if message == "none":
            message = await bot.send_message(bot.get_channel(chid), embed=embed) #send the message on first run
            
        else:
            message = await bot.edit_message(message, embed=embed) #edit the message on next runs

        await asyncio.sleep(3) #wait 3 seconds before running again