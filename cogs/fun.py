import json
import random

import discord
import requests
from discord import Member
from discord.ext import commands

with open('config.json', 'r') as file:
    config = json.loads(file.read())


class Fun(commands.Cog, name="fun"):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def hug(self, ctx, member: Member):
        url = "https://random-gifs-api.herokuapp.com/gifs/virtual-hugs"
        response = requests.get(url=url)
        gifs = response.text

        if member.mention == ctx.author.mention:
            self_hug = discord.Embed(
                title=":hugging: Hug",
                description="Does anyone need a hug?",
                color=discord.Color.blue()
            )

            self_hug.set_image(url=f"{gifs}")
            self_hug.set_footer(text=f"Requested by {ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

            await ctx.send(embed=self_hug)
        else:
            hug = discord.Embed(
                title=f":people_hugging: Hug",
                description=f"{member.mention}, {ctx.author.mention} hugged you.",
                color=discord.Color.green()
            )

            hug.set_image(url=f"{gifs}")
            hug.set_footer(text=f"Requested by {ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

            await ctx.send(embed=hug)

    @commands.command()
    async def rickroll(self, ctx, member: Member):
        rick_roll_gif = config["rick_roll"]

        if member.mention == ctx.author.mention:
            self_rick_roll = discord.Embed(
                title="Never gonna give you up",
                description=f"{ctx.author.mention} rickrolled himself",
                color=discord.Color.green()
            )

            self_rick_roll.set_image(url=f"{rick_roll_gif}")
            self_rick_roll.set_footer(text=f"Requested by {ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

            await ctx.channel.send(embed=self_rick_roll)
        else:
            rick_roll = discord.Embed(
                title="Never gonna give you up",
                description=f"{ctx.author.mention} rickrolled {member.mention}",
                color=discord.Color.green()
            )

            rick_roll.set_image(url=f"{rick_roll_gif}")
            rick_roll.set_footer(text=f"Requested by {ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

            await ctx.channel.send(embed=rick_roll)

    @commands.command()
    async def covid(self, ctx, countryName=None):
        url = f"https://coronavirus-19-api.herokuapp.com/countries/{countryName}"
        image = "https://dgpi.de/wp-content/uploads/2020/03/covid19.jpg"

        data = requests.get(url=url)
        json_data = data.json()

        country = json_data["country"]
        cases = json_data["cases"]
        todayCases = json_data["todayCases"]
        deaths = json_data["deaths"]
        todayDeaths = json_data["todayDeaths"]
        active = json_data["active"]
        recovered = json_data["recovered"]

        if countryName is not None:
            covid = discord.Embed(
                title=f":microbe: Covid-19 Stats from {country}",
                description="All informations arent live! It may differ from the real data.",
                color=discord.Color.blue()
            )

            covid.add_field(name="Country", value=f"{country}", inline=True)
            covid.add_field(name="Cases", value=f"{cases}", inline=True)
            covid.add_field(name="Cases today", value=f"{todayCases}", inline=True)
            covid.add_field(name="Deaths", value=f"{deaths}", inline=True)
            covid.add_field(name="Deaths today", value=f"{todayDeaths}", inline=True)
            covid.add_field(name="Active cases", value=f"{active}", inline=True)
            covid.add_field(name="Recovered", value=f"{recovered}", inline=True)
            covid.set_image(url=f"{image}")
            covid.set_footer(text=f"Requested by {ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

            await ctx.send(embed=covid)
        elif countryName is None:
            embed = discord.Embed(
                title="No country specified. Please use the comand like this: ``$covid (country)``",
                color=discord.Color.red()
            )

            await ctx.send(embed=embed)
        else:
            error = discord.Embed(
                title="Error while searching for country",
                color=discord.Color.red(),
                description="Please enter a real country or pronounce it right"
            )

            await ctx.send(embed=error)

    @commands.command()
    async def meme(self, ctx):
        url = "https://meme-api.herokuapp.com/gimme"

        data = requests.get(url=url)
        json_data = data.json()

        title = json_data["title"]
        link_url = json_data["url"]
        author = json_data["author"]
        post_link = json_data["postLink"]

        meme = discord.Embed(
            title=f"{title}",
            color=discord.Color.green()
        )

        meme.set_author(name=f"{author}", url=f"{post_link}")
        meme.set_image(url=f"{link_url}")
        meme.set_footer(text=f"Requested by {ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

        await ctx.send(embed=meme)

    @commands.command()
    async def rps(self, ctx, choice=None):
        moves = ["rock", "scissors", "paper"]
        if choice not in moves:
            await ctx.send("You need to use **rock, paper or scissors** as a move!")

        if choice in moves:
            bots_choice = random.choice(moves)
            embed = discord.Embed(title="Rock, Paper, Scissors", description=f"**Bots choice: {bots_choice}**")
            await ctx.send(embed=embed)

            if choice == "rock" and bots_choice == "paper":
                await ctx.send(f"**You lost! {ctx.author.mention}**")

            if choice == "paper" and bots_choice == "rock":
                await ctx.send(f"**You won! {ctx.author.mention}**")

            if choice == "paper" and bots_choice == "scissors":
                await ctx.send(f"**You lost! {ctx.author.mention}**")

            if choice == "scissors" and bots_choice == "paper":
                await ctx.send(f"**You won! {ctx.author.mention}**")

            if choice == "rock" and bots_choice == "scissors":
                await ctx.send(f"**You won! {ctx.author.mention}**")

            if choice == "scissors" and bots_choice == "rock":
                await ctx.send(f"**You lost! {ctx.author.mention}**")

            if choice == bots_choice:
                await ctx.send(f"**Its a Tie!**")

    """
    # TicTacToe
    @commands.command()
    async def play(self, ctx, member: Member):
        class Player:
            class Player1:
                def __init__(self, turn=False):
                    self.symbol = "❌"
                    self.turn = turn
                    self.name = ctx.author.name
                    self.url = ctx.author.avatar_url

                def getSymbol(self):
                    return self.symbol

                def getTurn(self, new_turn=False):
                    self.turn = new_turn
                    return self.turn

                def getName(self):
                    return self.name

                def getUrl(self):
                    return self.url

            class Player2:
                def __init__(self, turn=True):
                    self.symbol = "⭕"
                    self.turn = turn
                    self.name = member.display_name
                    self.url = member.avatar_url

                def getSymbol(self):
                    return self.symbol

                def getTurn(self, new_turn=True):
                    self.turn = new_turn
                    return self.turn

                def getName(self):
                    return self.name

                def getUrl(self):
                    return self.url

        player_1 = Player.Player1()
        player_2 = Player.Player2()

        board = {
            1: None,
            2: None,
            3: None,
            4: None,
            5: None,
            6: None,
            7: None,
            8: None,
            9: None

        }

        begin = await ctx.channel.send(f"{member.mention}, press ✅ to play with {ctx.author.mention}")
        await begin.add_reaction("✅")
        await begin.add_reaction("❎")

        async def choose_number():
            round_x = await ctx.channel.send("Choose a number from 1-9 to place your mark")
            await round_x.add_reaction("1️⃣")
            await round_x.add_reaction("2️⃣")
            await round_x.add_reaction("3️⃣")
            await round_x.add_reaction("4️⃣")
            await round_x.add_reaction("5️⃣")
            await round_x.add_reaction("6️⃣")
            await round_x.add_reaction("7️⃣")
            await round_x.add_reaction("8️⃣")
            await round_x.add_reaction("9️⃣")

            return round_x

        async def draw_board(emoji=None, emoji_1='1️⃣', emoji_2='2️⃣', emoji_3='3️⃣', emoji_4='4️⃣', emoji_5='5️⃣',
                             emoji_6='6️⃣', emoji_7='7️⃣', emoji_8='8️⃣', emoji_9='9️⃣'):

            def check_turn():
                while True:
                    if player_1.getTurn() is False:
                        turn = '❌'

                        player_1.getTurn(True)
                        player_2.getTurn(False)
                        return turn
                    elif player_2.getTurn() is False:
                        turn = '⭕'

                        player_2.getTurn(True)
                        player_1.getTurn(False)
                        return turn

            def getName():  # Muss korrigiert werden. Allgemein alles... ka
                if player_1.getTurn() is False:
                    return player_1.getName()
                elif player_2.getTurn() is True:
                    return player_2.getName()

            def getUrl():
                if player_1.getTurn() is False:
                    return player_1.getUrl()
                elif player_2.getTurn() is True:
                    return player_2.getUrl()

            if emoji == '1️⃣':
                emoji_1 = check_turn()
            elif emoji == '2️⃣':
                emoji_2 = check_turn()
            elif emoji == '3️⃣':
                emoji_3 = check_turn()
            elif emoji == '4️⃣':
                emoji_4 = check_turn()
            elif emoji == '5️⃣':
                emoji_5 = check_turn()
            elif emoji == '6️⃣':
                emoji_6 = check_turn()
            elif emoji == '7️⃣':
                emoji_7 = check_turn()
            elif emoji == '8️⃣':
                emoji_8 = check_turn()
            elif emoji == '9️⃣':
                emoji_9 = check_turn()

            embed_board = discord.Embed(title="Tic Tac Toe",
                                        description=
                                        f'''{emoji_1} {emoji_2} {emoji_3}                          
{emoji_4} {emoji_5} {emoji_6}
{emoji_7} {emoji_8} {emoji_9}
                                        ''',
                                        color=discord.Color.blue())

            embed_board.set_footer(text=f"It`s {getName()}`s turn", icon_url=f"{getUrl()}")

                return await ctx.channel.send(embed=embed_board)

        # Alles ab hier checkt den Start des Spieles:
        
        # Akzeptiert der Gegner die Anfrage? 
        # 1. Wenn ja, dann wird die Beginn Nachricht gelöscht und eine
        # Bestätigungsnachricht gesendet. Diese Nachricht wird dann nach 1,5 Sekunden gelöscht und die draw_board()
        # Funktion wird aufgerufen, die ein Spielfeld mit dem aktuellen Spieler, der am Zug ist, anzeigt. 
        # Nach 0,5 Sekunden wird die choose_number() Funktion aufgerufen, die eine Auswahl von Nummern anzeigt, wo der
        # Spieler seine Markierung setzen möchte. 
        
        # 2. Wenn nein, dann wird eine Nachricht gesendet: ,,{ctx.author.mention},
        # your opponent {member.mention} didn't dare!".
        

        def check_emoji(reaction, user):
            return user == member and str(reaction.emoji) == '✅' or user == member and str(reaction.emoji) == '❎'

        try:
            reaction, user = await self.client.wait_for('reaction_add', timeout=15, check=check_emoji)

            if reaction.emoji == '✅':
                await begin.delete()
                match_msg = await ctx.channel.send(f"Match with {ctx.author.mention} and {member.mention}")
                await asyncio.sleep(1.5)
                await match_msg.delete()
                await draw_board()
                await asyncio.sleep(0.5)
                await choose_number()

            elif reaction.emoji == '❎':
                await ctx.channel.send(f"{ctx.author.mention}, your opponent {member.mention} didn't dare!")
                pass

            else:
                await ctx.channel.send("Invalid emoji!")

        except asyncio.TimeoutError:
            await ctx.channel.send(f"Timed out! Be faster next time...")


        # Ab hier wird gecheckt, wie der Spieler vorgeht:
        
        # Es wird gecheckt, welche Nummer ausgewählt wurde. Danach ob das Feld schon besetzt ist.
        # Wenn nicht, dann kann eine Markierung gesetzt werden ( Wird an die draw_board() Funktion übergeben ) .
        

        def check_number(choose, player):
            return player == member and str(choose.emoji) == '1️⃣' or player == member and str(choose.emoji) == '2️⃣' \
                   or player == member and str(choose.emoji) == '3️⃣' or player == member and str(choose.emoji) == '4️⃣' \
                   or player == member and str(choose.emoji) == '5️⃣' or player == member and str(choose.emoji) == '6️⃣' \
                   or player == member and str(choose.emoji) == '7️⃣' or player == member and str(choose.emoji) == '8️⃣' \
                   or player == member and str(choose.emoji) == '9️⃣'

        try:
            while True:
                choose, player = await self.client.wait_for('reaction_add', timeout=20, check=check_number)
                await ctx.send(f"You choosed {choose.emoji}")

                if choose.emoji == '1️⃣':
                    if board[1] == 1:
                        await ctx.send("Here is a symbol already")
                    else:
                        board[1] = 1
                        choose = '1️⃣'
                        await draw_board(emoji=choose)
                elif choose.emoji == '2️⃣':
                    if board[2] == 1:
                        await ctx.send("Here is a symbol already")
                    else:
                        board[2] = 1
                        choose = '2️⃣'
                        await draw_board(emoji=choose)
                elif choose.emoji == '3️⃣':
                    if board[3] == 1:
                        await ctx.send("Here is a symbol already")
                    else:
                        board[3] = 1
                        choose = '3️⃣'
                        await draw_board(emoji=choose)
                elif choose.emoji == '4️⃣':
                    if board[4] == 1:
                        await ctx.send("Here is a symbol already")
                    else:
                        board[4] = 1
                        choose = '4️⃣'
                        await draw_board(emoji=choose)
                elif choose.emoji == '5️⃣':
                    if board[5] == 1:
                        await ctx.send("Here is a symbol already")
                    else:
                        board[5] = 1
                        choose = '5️⃣'
                        await draw_board(emoji=choose)
                elif choose.emoji == '6️⃣':
                    if board[6] == 1:
                        await ctx.send("Here is a symbol already")
                    else:
                        board[6] = 1
                        choose = '6️⃣'
                        await draw_board(emoji=choose)
                elif choose.emoji == '7️⃣':
                    if board[7] == 1:
                        await ctx.send("Here is a symbol already")
                    else:
                        board[7] = 1
                        choose = '7️⃣'
                        await draw_board(emoji=choose)
                elif choose.emoji == '8️⃣':
                    if board[8] == 1:
                        await ctx.send("Here is a symbol already")
                    else:
                        board[8] = 1
                        choose = '8️⃣'
                        await draw_board(emoji=choose)
                elif choose.emoji == '9️⃣':
                    if board[9] == 1:
                        await ctx.send("Here is a symbol already")
                    else:
                        board[9] = 1
                        choose = '9️⃣'
                        await draw_board(emoji=choose)

        except asyncio.TimeoutError:
            await ctx.channel.send("Timed out! Be faster next time...")
        """


def setup(client):
    client.add_cog(Fun(client))
