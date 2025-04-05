import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"Přihlášen jako {bot.user}")

@bot.command()
async def test(ctx):
    await ctx.send("Testující message! :D ** A** *B*")

# Spuštění bota
bot.run(os.getenv("TOKEN"))
