import discord
from discord.ext import commands


class Help(commands.Cog, name="help"):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):

        thumbnail = "https://cdn.pixabay.com/photo/2012/04/13/00/19/unknown-31209_1280.png"

        help = discord.Embed(title=f"{ctx.message.guild.name}", color=discord.Color.blue())

        help.add_field(name=f":man_construction_worker:**Moderation**", value="```$help moderation```", inline=True)
        help.add_field(name=f":desktop: **Server**", value="```$help server```", inline=True)
        help.add_field(name=f":stuck_out_tongue_winking_eye: **Fun**", value="```$help fun```", inline=True)
        help.set_thumbnail(url=f"{thumbnail}")
        help.set_footer(text=f"Requested by {ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

        moderation = discord.Embed(title=f":man_construction_worker: Moderation",
                                   color=discord.Color.blue())

        moderation.add_field(name="$kick @user", value="Kick a user", inline=False)
        moderation.add_field(name="$ban @user", value="Ban a user", inline=False)
        moderation.add_field(name="$unban @user", value="Unban a user", inline=False)
        moderation.add_field(name="$clear (amount)", value="Delete a amount of messages", inline=False)
        moderation.add_field(name="$poll (selection-1) (selection-2)", value="Create a poll and send it in the channel", inline=False)
        moderation.set_thumbnail(url=f"{thumbnail}")
        moderation.set_footer(text=f"Requested by {ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

        server = discord.Embed(title=f":desktop: Server", color=discord.Color.blue())
        server.add_field(name="$serverinfo", value="Sends infos about the server", inline=False)
        server.add_field(name="$userinfo @user", value="Sends infos about the user", inline=False)
        server.add_field(name="$avatar @user - optional", value="Sends the avatar of the user", inline=False)
        server.add_field(name="$ping", value="Sends the ping from the bot to the server", inline=False)
        server.add_field(name="$invite", value="Sends the invite link from the bot", inline=False)
        server.set_thumbnail(url=f"{thumbnail}")
        server.set_footer(text=f"Requested by {ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

        fun = discord.Embed(title=f":stuck_out_tongue_winking_eye: Fun",
                            color=discord.Color.blue())

        fun.add_field(name="$meme", value="Sends a random meme", inline=False)
        fun.add_field(name="$rps (choose)", value="Play a Rock, Paper, Scissors Match against the bot!", inline=False)
        fun.add_field(name="$hug @user", value="Embraces a user", inline=False)
        fun.add_field(name="$rickroll @user", value="Rickroll a user", inline=False)
        fun.add_field(name="$covid (country)", value="Sends covid stats from the country", inline=False)
        fun.set_thumbnail(url=f"{thumbnail}")
        fun.set_footer(text=f"Requested by {ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

        if ctx.message.content == "$help moderation":
            await ctx.channel.send(embed=moderation)
        elif ctx.message.content == "$help server":
            await ctx.channel.send(embed=server)
        elif ctx.message.content == "$help fun":
            await ctx.channel.send(embed=fun)
        else:
            await ctx.channel.send(embed=help)


def setup(client):
    client.add_cog(Help(client))
