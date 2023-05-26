import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author ==  bot.user:
        return
    
    if message.content.startswith("hello"):
        await message.channel.send("Hey~~")
    
    if message.content.startswith("oo"):
        await message.channel.send("O.O")




@bot.command
async def info(ctx):
    await ctx.send(ctx.guild)
    await ctx.send(ctx.author)
    await ctx.send(ctx.message.id)
    


bot.run('MTAzMzMyMTMwMjY3ODgzNTI1MQ.GIiUsq.-n77ei3mFta6qIUc_EecanqnrRtjzleowswDvQ')