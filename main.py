from secrets import discord_key
from discord import app_commands
from my_client import EclipsedGroovy
import discord

intents = discord.Intents.default()
intents.message_content = True

client = EclipsedGroovy(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


@client.tree.command()
async def hello(ctx):
    await ctx.send('Hello!')

client.run(discord_key)
