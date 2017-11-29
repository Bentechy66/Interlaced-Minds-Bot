import discord
import asyncio
from discord.ext import commands
#import botobject
import sqlite3
import botobject
import credentials
import datetime


bot = botobject.bot

#defining commands

#Add records
@bot.command(pass_context=True)
async def AddR(ctx):
    """[DEBUG COMMAND] Used to add records to the Bot's SQL when new members join"""
    
    if discord.utils.get(ctx.message.author.roles, name='Moderator'):
        counts = await AddRecords()
        await bot.add_reaction(ctx.message, "tick:326377249223999498")
        bad = counts.split(":")[0]
        good = counts.split(":")[1]
        await bot.say("Successes: " + str(good) + "\nFailed (Duplicate or error): " + str(bad))
        return("Finished with no errors!")
    else:
        await bot.add_reaction(ctx.message, "nope:326377249274068992")
        await asyncio.sleep(3)
        await bot.delete_message(ctx.message)
        return("Finished with no errors!")



#setting points
@bot.command(pass_context=True)
async def setpoints(ctx, mention, pointsv):
    """Sets a user's points to a value (The pointmaster role is required)"""
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
        errorlevel = SetPoints(name, pointsv)
        await bot.add_reaction(ctx.message, "tick:326377249223999498")
        Log(pointsv, name, ctx.message.author.name, " set points to ")
    else:
        await bot.add_reaction(ctx.message, "nope:326377249274068992")
    await asyncio.sleep(3)
    await bot.delete_message(ctx.message)

        
#setting points
@bot.command(pass_context=True)
async def addpoints(ctx, mention, pointsv):
    """Adds a number of points to a user's value (The pointmaster role is required)"""
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
        errorlevel = AddPoints(name, pointsv)
        await bot.add_reaction(ctx.message, "tick:326377249223999498")
        #await bot.send_message(ctx.message.channel, embed=errorlevel)
        Log(pointsv, name, ctx.message.author.name, " added ")
    else:
        await bot.add_reaction(ctx.message, "nope:326377249274068992")
    await asyncio.sleep(3)
    await bot.delete_message(ctx.message)



def CreateTable():
    sqlite_file = "Database.db"
    conn = sqlite3.connect("Database.db")
    c = conn.cursor()
    c.execute("CREATE TABLE pointTable (name TEXT UNIQUE PRIMARY KEY, points INTEGER)")
    

async def AddRecords():
    sqlite_file = "Database.db"
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    names = list(bot.get_all_members()) #Get list of members
    names = list(set(names))
    failed = 0
    added = 0
    
    
    #return names
    
    for person in names:
        person = str(person.name)
        
        try:
            c.execute("INSERT INTO pointTable (name, points) VALUES (?, 0)", [person])
            added = added + 1
        except:
            print("Duplicate or error")
            failed = failed + 1
        
    conn.commit()
    conn.close()
    
    return str(failed) + ":" + str(added)
        


def SetPoints(name, points):
    sqlite_file = 'Database.db'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    
    #c.execute("REPLACE INTO pointTable (name, points) VALUES (?, points + ?)", (name, points))
    
    
    name = name[:-5]
    c.execute('UPDATE pointTable SET points = ? WHERE name = ?;', (points, name)) #get points
    #data = c.fetchall() #get the query
    
    #print(list(data)[0]) #print that

    #c.execute("CREATE TABLE points (key INTEGER PRIMARY KEY, name TEXT UNIQUE, points INTEGER);")

    conn.commit()
    conn.close()
    
    return "Complete"
    Embed(name, points)
    #return(data)

    
def AddPoints(name, points):
    sqlite_file = 'Database.db'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    
    #c.execute("REPLACE INTO pointTable (name, points) VALUES (?, points + ?)", (name, points))
    
    name = name[:-5]
    c.execute('UPDATE pointTable SET points = points + ? WHERE name = ?;', (points, name)) #get points
    #data = c.fetchall() #get the query
    
    #print(list(data)[0]) #print that

    #c.execute("CREATE TABLE points (key INTEGER PRIMARY KEY, name TEXT UNIQUE, points INTEGER);")

    conn.commit()
    conn.close()
    return Embed(name, points)
    
    #return(data)
    
    
    
def GetPoints(name):
    name = str(name)
    name = name[:-5]
    sqlite_file = 'Database.db'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute("SELECT points FROM pointTable WHERE name = ?", [name])
    return c.fetchone()
    
def Embed(name, points):
    embed = discord.Embed(color=0xf7ea31)
    embed.set_author(name="Points Awarded!", icon_url="https://cdn4.iconfinder.com/data/icons/small-n-flat/24/star-256.png")    
    embed.add_field(name="How Many?", value=points)
    embed.add_field(name="Who to?", value=name)
    #await bot.send_message(message.channel, embed=embed)
    return embed
    
def Log(name, pointsv, author, soa):
    file = open('Logs.txt', 'a') 
 
    file.write(author + ": " + soa + name + " for " + pointsv + "\n")
 
    file.close() 
    #print(str(ctx.message.author.name) + ": '" + ctx.message.content + "' at " + str(datetime.datetime.utcnow()) + " UTC")
