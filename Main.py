import datetime
import discord
from discord.ext import commands

from ChatHandler import ChatHandler

PREFIX = "!"
INFO_EMBED_URL = "https://google.com"
DISCORD_TOKEN = "TODO"

client = commands.Bot(command_prefix=PREFIX, description="DESCRIPTION HERE")

chatHandler = ChatHandler()


@client.command()
async def ping(ctx):
    await ctx.send('pong')


@client.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Lorem Ipsum asdasd",
                          timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url=INFO_EMBED_URL)

    await ctx.send(embed=embed)


@client.command(aliases=['prefix'])
async def change_prefix(ctx, *, prefix):
    client.command_prefix = prefix

    global PREFIX
    PREFIX = prefix

    print("Changed Prefix to", prefix)

# Events

@client.event
async def on_message(message):

    channel = message.channel

    if message.content.startswith('{}reply'.format(PREFIX)):

        print("User asked for response to {}".format(message))
        await channel.send("User asked for response to {}".format(message))
        response = chatHandler.get_response(message)
        print("Responded with message {}".format(response))
        await channel.send*"Responded with message {}".format(response)

    elif message.content.startswith('{}train'.format(PREFIX)):

        print("Training Bot")
        await message.channel.send("Training Bot")
        chatHandler.train()
        print("Successfully Trained Bot")
        await message.channel.send("Successfully Trained Bot")
    else:
        print("Test Print")


@client.event
async def on_ready():
    await client.change_presence(
        activity=discord.Game(name="With Reemon", url="https:github.com/danielbatchford/DiscordChatBot"))
    print('Bot Online')


client.run(DISCORD_TOKEN)
