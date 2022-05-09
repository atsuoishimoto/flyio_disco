import os
import pathlib
import shelve
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()

DATADIR = pathlib.Path(os.environ.get("DATADIR", ".")).resolve()
COUNTFILE = DATADIR / "count"
db = shelve.open(os.fspath(COUNTFILE))

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="?", intents=intents)


@bot.event
async def on_message(message):
    if message.author.bot:
        return
    channel = message.channel
    key = str(message.author.id)
    n = db.get(key, 0) + 1
    db[key] = n
    await channel.send(f"{n} 回目の発言")
    db.sync()


bot.run(os.environ["DISCORDBOT_TOKEN"])
