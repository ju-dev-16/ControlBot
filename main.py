import os
import discord
import json

from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix="$", help_command=None, intents=intents)

with open('config.json', 'r') as file:
    config = json.loads(file.read())

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run(config["token"])
