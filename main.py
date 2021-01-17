import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import json

bot = commands.Bot(command_prefix="$")

with open("C:\\Users\\toure\\Coding\\Python\\Botitect\\botinfo.json", "r") as f:
    info = json.load(f)

    TOKEN = info["bot_token"]

@bot.event
async def on_ready():
    print("Bot is online!")

@bot.event
async def on_message(message):
    if not message.author.bot:
        print(f"{message.guild} ; {message.author.name} : {message.content}")


bot.run(TOKEN)