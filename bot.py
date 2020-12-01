import os
from os.path import join, dirname

import discord
from discord.ext import tasks

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
            channel_spec = client.get_channel(channel.id)
            test.start(channel_spec)
            
@tasks.loop(minutes=1)
async def test(channel_spec):
    await channel_spec.send(f"Test alert every minute: BTC All time high is {BTC_ATH}")
    await channel_spec.send(f"Test alert every minute: ETH All time high is {ETH_ATH}")

client.run(TOKEN)