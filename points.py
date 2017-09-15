import discord
import asyncio
from discord.ext import commands
#import botobject
import sqlite3
import botobject
import credentials

bot = botobject.bot



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
    
    #return names
    
    for person in names:
        person = str(person.name)
        
        c.execute("INSERT INTO pointTable (name, points) VALUES (?, 0)", [person])
    conn.commit()
    conn.close()
    
    return "Complete"
        


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
    return "Complete"
    #return(data)
    
    
    
def GetPoints(name):
    name = str(name)
    name = name[:-5]
    sqlite_file = 'Database.db'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute("SELECT points FROM pointTable WHERE name = ?", [name])
    return c.fetchone()
    
    
    