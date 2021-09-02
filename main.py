import discord
import os
from replit import db
from keep_alive import keep_alive


client = discord.Client()

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)

@client.event
async def on_message(message):
    if message.author != client.user:
        await message.channel.send(message.content[::-1])

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)