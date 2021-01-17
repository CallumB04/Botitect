import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix="$")
TOKEN = "ODAwMTk5OTQ3MDEzOTgwMjIw.YAOqRg._Oo93HO3mso7DDwR8SDUSqq_uOk"

@bot.event
async def on_ready():
    print("Bot is online!")

@bot.event
async def on_message(message):
    if not message.author.bot:
        print(f"{message.guild} ; {message.author.name} : {message.content}")


bot.run(TOKEN)