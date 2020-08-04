import datetime
import discord
from discord.ext import commands

import DiscordChatBot

PREFIX = "!"
INFO_EMBED_URL = "https://google.com"

bot = commands.Bot(command_prefix=PREFIX, description="This is a Helper Bot")

chatBot = DiscordChatBot()


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
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


@bot.command(pass_context=True, aliases=['prefix'])
async def change_prefix(ctx, *, prefix):
    bot.command_prefix = prefix
    async print("Changed Prefix to", prefix)


# Events
@bot.command
async def train(ctx):
    print("Training Bot")
    await message.channel.send("Training Bot")
    chatBot.train(ctx)
    print("Successfully Trained Bot")
    await message.channel.send("Successfully Trained Bot")


@bot.event
async def on_ready():
    await bot.change_presence(
        activity=discord.Game(name="With Reemon", url="https:github.com/danielbatchford/DiscordChatBot"))
    print('Bot Online')

bot.run('token')
