import os

import discord
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix="$", help_command=None, intents=intents)

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run(os.getenv("TOKEN"))
