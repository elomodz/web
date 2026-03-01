import discord
import os

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowano jako {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == "!ping":
        await message.channel.send("Pong!")

def run_bot():
    bot.run(TOKEN)
