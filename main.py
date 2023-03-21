import discord
import requests
import json
from mee6_py_api import API
import os
mee6API = API("server id")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Bot is ready')

@client.event
async def on_message(message):

    if message.content.startswith('!rank'):

        args = message.content.split()
        if len(args) != 2:
            await message.channel.send('Invalid arguments. Usage: !rank <id>')
            return
        user_id = args[1]

        details = await mee6API.levels.get_user_details(user_id)

        level = details['level']
        xp = details['xp']
        message_count = details['message_count']
        username = details['username']
        discrimator = details['discriminator']

        print(details)

        await message.channel.send(f'Username: {username}#{discrimator}, Tag: <@{user_id}>, Level: {level}, XP: {xp}, Message Count: {message_count}')

# Replace bot token with your own Discord bot token
token = "bot token"
client.run(token)