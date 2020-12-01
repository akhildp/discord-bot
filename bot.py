import os
from os.path import join, dirname

import discord
from dotenv import load_dotenv
from ath import *

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    for channel in guild.text_channels:
        if channel.name == 'ath-alerts':
            await client.get_channel(channel.id).send(f"Test alert: BTC All time high is {BTC_ATH}")
            await client.get_channel(channel.id).send(f"Test alert: ETH All time high is {ETH_ATH}")

client.run(TOKEN)