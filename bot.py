import os
import pandas as pd
from dotenv import load_dotenv
import requests

import discord
from discord.ext import tasks

#from ath import *

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

ENDPOINT = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids='

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
            price_check.start(channel_spec)
            
@tasks.loop(minutes=5)
async def price_check(channel_spec):
    df = pd.read_csv('coins_endpoints.csv').drop(['Unnamed: 0'],axis=1)
    for coin in df['Name']:
        ath_change_percentage = requests.get(ENDPOINT+coin).json()[0]['ath_change_percentage']
        if abs(ath_change_percentage) <= 2:
            await channel_spec.send(f"{coin} is within 2% of its all time high")
    #await channel_spec.send(f"Test alert every minute: ETH All time high is {ETH_ATH}")

client.run(TOKEN)