import discord
from discord import Member
from discord.ext import commands


class Moderation(commands.Cog, name="moderation"):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def kick(self, ctx, member: Member, reason=None):
        if member.mention == ctx.author.mention:
            self_kick = discord.Embed(
                title="Failed kick ✅",
                description=f"You cannot kick yourself!",
                color=discord.Color.red()
            )

            await ctx.channel.send(embed=self_kick)
        elif member.guild_permissions.manage_messages or member.guild_permissions.administrator:
            high_permissions_kick = discord.Embed(
                title="Failed kick ❎",
                description=f"The person has high permissions!",
                color=discord.Color.red()
            )

            await ctx.channel.send(embed=high_permissions_kick)
        else:
            kick = discord.Embed(
                title="Successful kick ✅",
                description=f"{member.mention} has been kicked. Reason: {'Unknown' if reason is None else str(reason)}",
                color=discord.Color.green()
            )

            await member.kick(reason=reason)
            await ctx.channel.send(embed=kick)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: Member, reason=None):
        if member.mention == ctx.author.mention:
            self_ban = discord.Embed(
                title="Failed ban ❎",
                description=f"You cannot ban yourself!",
                color=discord.Color.red()
            )

            await ctx.channel.send(embed=self_ban)
        elif member.guild_permissions.manage_messages or member.guild_permissions.administrator:
            high_permissions_ban = discord.Embed(
                title="Failed ban ❎",
                description=f"The person has high permissions!",
                color=discord.Color.red()
            )

            await ctx.channel.send(embed=high_permissions_ban)
        else:
            ban = discord.Embed(
                title="User banned successfully ✅",
                description=f"{member.mention} was banned for: {' not known' if reason is None else str(reason)}",
                color=discord.Color.green()
            )

            await member.ban(reason=reason)
            await ctx.channel.send(embed=ban)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        unban = discord.Embed(
            title="User unbanned successfully ✅",
            description=f"{member} was successfully unbanned",
            color=discord.Color.green()
        )

        failed_unban = discord.Embed(
            title="Failed unban ❎",
            description=f"{member} was not found",
            color=discord.Color.red()
        )

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.channel.send(embed=unban)
                return
            else:
                await ctx.channel.send(embed=failed_unban)
                return

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=0):
        if amount > 100:
            await ctx.channel.send(f"I cannot delete more than 100 messages!")
        elif amount <= 100:
            await ctx.channel.purge(limit=amount + 1)

            clear = discord.Embed(
                title=f"Deleted messages :incoming_envelope:",
                description=f"I could delete {amount} messages!",
                color=discord.Color.green()
            )

            await ctx.channel.send(embed=clear, delete_after=3.5)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def poll(self, ctx, answer1, answer2):
        poll = discord.Embed(
            title=f"{answer1} or {answer2}",
            color=discord.Color.blue()
        )
        poll.add_field(name=f":regional_indicator_a: {answer1}", value=" ‎", inline=False)
        poll.add_field(name=f":regional_indicator_b: {answer2}", value=" ‎", inline=False)
        poll.set_footer(text=f"Poll created by {ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
        msg = await ctx.send(embed=poll)
        await msg.add_reaction('🅰')
        await msg.add_reaction('🅱')


def setup(client):
    client.add_cog(Moderation(client))
