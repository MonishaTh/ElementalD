# bot.py
import os, csv

import shutil
from tempfile import NamedTemporaryFile

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
PREFIX = "!" #TODO: Make this not hard-coded.

  

client = CustomClient()
client.run(TOKEN)
