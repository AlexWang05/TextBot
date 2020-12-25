import discord
from discord.ext import commands
import random
import time

client = commands.Bot(command_prefix="tb ")  # prefix = tb + space
client.remove_command("help")  # removes default help command


@client.event
async def on_ready():  # runs when bot is ready
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(
        type=discord.ActivityType.listening, name="tb help"
    ))  # sets status of "Listening to tb help"
    print("Bot is ready, logged in as TextBot")


@client.command()
async def help(ctx):  # help menu
    # embed message to send back
    my_embed = discord.Embed(title="TextBot Help Menu", description="Version 0.0.2", color=discord.Color.blue())
    my_embed.set_footer(text="Hope this helps!")

    # fields
    my_embed.add_field(name="tb ping @user", value="Spam pings specified user with ping speed 0.3-0.8s", inline=True)
    my_embed.add_field(name="tb cringe", value="Pings the cringiest person on the server!", inline=True)
    my_embed.add_field(name="tb say", value="Says random things", inline=True)
    my_embed.add_field(name="tb pog", value="Tells you if you are poggers", inline=False)

    await ctx.send(embed=my_embed)  # sends embedded message


@client.command()
async def say(ctx):  # says random things
    response_list = ["sup", "what's up", "what do you even want me to say", "bruh",
                     "okay...?", "yo wassup", "hey how's it going?", "hi"]
    random_option = random.randint(0, len(response_list) - 1)  # random index in list
    await ctx.send(response_list[random_option])  # sends message


@client.command()
async def cringe(ctx):  # pings person
    await ctx.send("<@598616534222503938> is cringe")  # @pings user, syntax = <@ID>


@client.command()
async def ping(ctx):  # spam pings someone
    spam_speed_low = 0.3  # lower spam speed limit
    spam_speed_high = 0.8  # upper spam speed limit

    msg = ctx.message.content  # gets user message
    name = msg.split()  # splits into list

    if len(name) == 3:
        ping_person = name[2]  # gets index 2 (who to ping)

        # generates random speed and spams
        for i in range(10):
            spam_speed = random.uniform(spam_speed_low, spam_speed_high)  # random spam speed
            await ctx.send(ping_person)  # pings person
            time.sleep(spam_speed)  # waits the spam speed
    else:
        await ctx.send("Incorrect format: tb ping @user")


@client.command()
async def pog(ctx):  # tells someone if they are poggers
    username = ctx.message.author.id  # gets author's name
    ping_str = "<@" + str(username) + ">"  # str that pings user

    pog_status = ["not at all", "not really", "kind of", "sort of",
                  "a little", "pretty", "very", "extremely"]
    pog_choice = random.randint(0, len(pog_status) - 1)  # random index
    return_str = ping_str + " is " + pog_status[pog_choice] + " poggers!"

    await ctx.send(return_str)


TOKEN = "ENTER_TOKEN_HERE"

# runs client with token
client.run(TOKEN)
