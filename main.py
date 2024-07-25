from secrets import discord_key
from discord import app_commands
from discord.ext import commands
import random
import json
from my_client import EclipsedGroovy
from functions import roll_agent, roll_champion
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

    if message.content.startswith('!genshin'):
        await message.channel.send('Genshin Sucks Balls Guppy')


@client.tree.command()
async def hello(ctx: discord.Interaction):
    await ctx.response.send_message('Hello!')

@client.tree.command()
async def agent(ctx: discord.Interaction, agent_role: str = None):
    rolled_agent = roll_agent(agent_role)
    if agent_role is None:
        print(f'{ctx.user} has rolled {rolled_agent} in the agent roll')
    else:
        print(f'{ctx.user} has rolled {rolled_agent} in the agent roll with {agent_role}')
    await ctx.response.send_message(f'You Rolled {rolled_agent}')


@client.tree.command()
async def champion(ctx: discord.Interaction, champion_role: str = None):
    rolled_champion = roll_champion(champion_role)
    if champion_role is None:
        print(f'{ctx.user} has rolled {rolled_champion} in the champion roll')
    else:
        print(f'{ctx.user} has rolled {rolled_champion} in the champion roll with {champion_role}')
    await ctx.response.send_message(f'You Rolled {rolled_champion}')


if __name__ == '__main__':
    client.run(discord_key)
