import discord
from discord.ext import commands
import random
import asyncio

intents = discord.Intents.default()
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
bot = commands.Bot(command_prefix='$', intents=intents)

jokes=[
    "What's orange and sounds like a parrot? A carrot!",
    "How do you organize a space party? You planet!",
    "What did one math book say to the other math book? I've got too many problems!",
    "Why did the golfer bring two pairs of pants? In case he got a hole in one!",
    "What do you call a fish wearing a crown? King mackerel!",
    "What do you call a fish with no eyes? Fsh!"
]
jokechoice= random.choice(jokes)

coinn=random.choice(["Heads!","Tails!"])

choices=random.choice(["Yes","No"])

def generator_pass(pass_length = 10):
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    passwords = ""

    for i in range(pass_length):
        passwords += random.choice(elements)

    return passwords


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')
    
    
@bot.command()
async def bye(ctx):
    await ctx.send(f'пока')

@bot.command()
async def coin (ctx):
    await ctx.send(coinn)

@bot.command()
async def joke(ctx):
    await ctx.send(jokechoice)
@bot.command()
async def choice(ctx):
    await ctx.send(choices)
@bot.command()
async def helps(ctx):
    await ctx.send('here are some commands')
    await ctx.send('$hello')
    await ctx.send('$bye')
    await ctx.send('$coin')
    await ctx.send('$password')
    await ctx.send('$choice')
    await ctx.send('$heh and then lenght')

@bot.command()
async def password(ctx):
    await ctx.send(generator_pass())

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)    

bot.run("TOKEN")
