import discord
from discord.ext import commands
from discord.utils import get
import random
import time

client = commands.Bot(command_prefix="tb ")  # prefix = tb + space
client.remove_command("help")  # removes default help command


@client.event
async def on_ready():  # runs when bot is ready
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(
        type=discord.ActivityType.listening, name="tb help"
    ))  # sets status of "Listening to tb help"
    print("Bot is ready, logged in as TextBot")


@client.command()
async def help(ctx):  # help menu
    # embed message to send back
    my_embed = discord.Embed(title="TextBot Help Menu", description="Version 0.1.0", color=discord.Color.blue())
    my_embed.set_footer(text="Hope this helps!")

    # fields
    my_embed.add_field(name="tb ping", value="Spam pings someone", inline=True)
    my_embed.add_field(name="tb cringe", value="Pings the cringiest person on the server!", inline=True)
    my_embed.add_field(name="tb say", value="Says random things", inline=True)

    await ctx.send(embed=my_embed)  # sends embedded message


@client.command()
async def say(ctx):  # says random things
    random_option = random.randint(1, 5)  # random integer

    # random response
    if random_option == 1:
        await ctx.send("bruh fr")
    elif random_option == 2:
        await ctx.send("what's up")
    elif random_option == 3:
        await ctx.send("what do you even want to to say")
    elif random_option == 4:
        await ctx.send("uh, okay..?")
    else:
        await ctx.send("sup")


@client.command()
async def cringe(ctx):  # pings person
    await ctx.send("<@598616534222503938> is cringe")  # @pings user, syntax = <@ID>


@client.command()
async def ping(ctx):  # spam pings someone
    spam_speed_low = 0.3  # lower spam speed limit
    spam_speed_high = 0.8  # upper spam speed limit

    # generates random speed and
    for i in range(10):
        spam_speed = random.uniform(spam_speed_low, spam_speed_high)
        await ctx.send("<@406236936810921984>")  # pings person
        time.sleep(spam_speed)  # waits


TOKEN = "ENTER_TOKEN_HERE"

# runs client with token
client.run(TOKEN)
