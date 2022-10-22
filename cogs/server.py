import discord
from discord import Member
from discord.ext import commands


class Server(commands.Cog, name="server"):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def userinfo(self, ctx, member: discord.Member):
        user_info = discord.Embed(
            title=f":mag: User Info - {member.display_name}",
            color=discord.Color.blue()
        )

        user_info.add_field(name="User-ID:", value=f"```{member.id}```", inline=True)
        user_info.add_field(name="Nickname:", value=f"```{member.nick if member.nick else 'Not set'}```",
                            inline=True)
        user_info.add_field(name="Joined Discord:", value=f"```{member.created_at.strftime('%d.%m.%Y')}```",
                            inline=True)
        user_info.add_field(name="Joined the server:", value=f"```{member.joined_at.strftime('%d.%m.%Y')}```",
                            inline=True)
        user_info.add_field(name="Roles:", value=f"```{len(member.roles)}```", inline=True)
        user_info.add_field(name="Highest role:", value=f"```{member.top_role.name}```", inline=True)
        user_info.add_field(name="User or Bot:", value=f"```{'Bot' if member.bot else 'User'}```", inline=True)
        user_info.set_thumbnail(url=f"{member.avatar_url}")
        user_info.set_footer(text=f"Requested by {ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

        await ctx.send(embed=user_info)

    @commands.command()
    async def ping(self, ctx):
        ping = discord.Embed(
            title="Bot Ping :ping_pong:",
            description=f"Bot Latency: {round(self.client.latency * 1000)} ms!",
            color=discord.Color.blue()
        )

        ping.set_footer(text=f"Requested by {ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

        await ctx.channel.send(embed=ping)

    @commands.command()
    async def avatar(self, ctx, member: Member = None):

        if member is None:
            self_avatar = discord.Embed(
                title=f"Avatar from {ctx.author.name}",
                description=f"{ctx.author.mention} asked for his avatar!",
                color=discord.Color.green()
            )

            self_avatar.set_image(url=f"{ctx.author.avatar_url}")
            self_avatar.set_footer(text=f"Requested by {ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

            await ctx.send(embed=self_avatar)
        elif member == ctx.author:
            self_avatar = discord.Embed(
                title=f"Avatar from {ctx.author.name}",
                description=f"{ctx.author.mention} asked for his avatar!",
                color=discord.Color.green()
            )

            self_avatar.set_image(url=f"{ctx.author.avatar_url}")
            self_avatar.set_footer(text=f"Requested by {ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

            await ctx.send(embed=self_avatar)
        else:
            avatar = discord.Embed(
                title=f"Avatar from {member.display_name}",
                description=f"{ctx.author.mention} asked for {member.mention} avatar!",
                color=discord.Color.green()
            )

            avatar.set_image(url=f"{member.avatar_url}")
            avatar.set_footer(text=f"Requested by {ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

            await ctx.send(embed=avatar)

    @commands.command()
    async def serverinfo(self, ctx):
        name = str(ctx.guild.name)
        owner = str(ctx.guild.owner)
        id = str(ctx.guild.id)
        region = str(ctx.guild.region)
        memberCount = str(ctx.guild.member_count)
        icon = str(ctx.guild.icon_url)
        voice_channels = len(ctx.guild.voice_channels)
        text_channels = len(ctx.guild.text_channels)
        channels_total = voice_channels + text_channels
        verification = ctx.guild.verification_level
        embed = discord.Embed(
            title=f"Server Information of {name}",
            color=discord.Color.blue()
        )
        embed.add_field(name="Owner:", value=owner, inline=False)
        embed.add_field(name="Server-ID:", value=id, inline=False)
        embed.add_field(name="Region", value=region, inline=False)
        embed.add_field(name="Member Count:", value=memberCount, inline=False)
        embed.add_field(name="Text-Channels:", value=str(text_channels), inline=False)
        embed.add_field(name="Voice-Channels:", value=str(voice_channels), inline=False)
        embed.add_field(name="Total Channels:", value=str(channels_total), inline=False)
        embed.add_field(name="Verification Level:", value=verification, inline=False)
        embed.set_thumbnail(url=icon)
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
        await ctx.send(embed=embed)

    @commands.command()
    async def invite(self, ctx):
        invite = discord.Embed(
            title="Add to server here",
            url="https://discord.com/oauth2/authorize?client_id=852469183429345290&scope=bot+applications.commands",
            description="Press the button to invite the bot to your server",
            color=discord.Color.blue()
        )

        invite.set_footer(text=f"Requested by {ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

        await ctx.send(embed=invite)


def setup(client):
    client.add_cog(Server(client))
