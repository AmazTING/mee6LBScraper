import discord
import requests
import json
from mee6_py_api import API
import os

# Replace "ID" with your server ID
mee6API = API("ID")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Bot is ready')

@client.event
async def on_message(message):
    # Check if the message is a command and starts with !rank
    if message.content.startswith('!rank'):
        # Extract the ID from the command arguments
        args = message.content.split()
        if len(args) != 2:
            await message.channel.send('Invalid arguments. Usage: !rank <id>')
            return
        user_id = args[1]

        details = await mee6API.levels.get_user_details(user_id)

        level = details['level']
        xp = details['xp']
        message_count = details['message_count']

        print(details)

        await message.channel.send(f'Level: {level}, XP: {xp}, Message Count: {message_count}')

# Replace bot_token with your own Discord bot token
token = "bot_token"
client.run(token)