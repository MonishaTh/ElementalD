# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

class CustomClient(discord.Client):
    async def on_ready(self):
        print(f'{client.user} has connected to Discord!')
        guild = discord.utils.get(client.guilds, name=GUILD)
        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )
    async def on_member_join(self,member):
        pass#For later
    async def on_message(self,message):
        if "Hello" in message.content:
            await message.channel.send("I'm not ready yet.")



client = CustomClient()
client.run(TOKEN)