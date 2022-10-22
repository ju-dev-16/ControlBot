import asyncio

import discord
from discord.ext import commands


class Events(commands.Cog, name="events"):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Bot is logging in as {self.client.user}... and is on {len(self.client.guilds)} Servers!")
        await self.client.loop.create_task(self.status_task())

    @commands.Cog.listener()
    async def status_task(self):
        while True:
            await self.client.change_presence(
                activity=discord.Streaming(name=f"with $help", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
                status=discord.Status.online)
            await asyncio.sleep(45)
            await self.client.change_presence(
                activity=discord.Streaming(name=f"on {len(self.client.guilds)} Servers",
                                           url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
                status=discord.Status.online)
            await asyncio.sleep(45)
            await self.client.change_presence(activity=discord.Streaming(name="on v1.10",
                                                                         url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
                                              status=discord.Status.online)
            await asyncio.sleep(45)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        welcome = discord.Embed(
            title=member.name,
            color=discord.Color.green(),
            description=f"Welcome on {member.guild.name}!"
        )

        if channel is not None:
            await channel.send(embed=welcome)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.channel.send("Command not found. Use ```$help``` for help")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.channel.send("I got no permission to run this command.")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.channel.send('You got no permission to run this command.')


def setup(client):
    client.add_cog(Events(client))
