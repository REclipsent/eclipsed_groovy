from secrets import discord_key
from discord import app_commands
from discord.ext import commands
import random
import json
from my_client import EclipsedGroovy
from functions import roll_agent, roll_champion
from role_types import LeagueRole, ValorantAgentRole
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
        await message.channel.send('Download Genshin Impact on PC for free and reach the '
                                   'milestones to support the stream! Use code '
                                   'GENSHINGIFT to get in-game rewards! ***')


@client.tree.command()
async def hello(ctx: discord.Interaction):
    await ctx.response.send_message('Hello!')

@client.tree.command()
async def agent(ctx: discord.Interaction, agent_role: ValorantAgentRole = None):
    if agent_role is None:
        rolled_agent = roll_agent()
        print(f'{ctx.user} has rolled {rolled_agent} in the agent roll')
    else:
        rolled_agent = roll_agent(agent_role.name)
        print(f'{ctx.user} has rolled {rolled_agent} in the agent roll with {agent_role.name}')

    await ctx.response.send_message(f'You Rolled {rolled_agent}')


@client.tree.command()
async def champion(ctx: discord.Interaction, champion_role: LeagueRole = None):
    if champion_role is None:
        rolled_champion = roll_champion()
        print(f'{ctx.user} has rolled {rolled_champion} in the champion roll')
    else:
        rolled_champion = roll_champion(champion_role.name)
        print(f'{ctx.user} has rolled {rolled_champion} in the champion roll with {champion_role.name}')
    await ctx.response.send_message(f'You Rolled {rolled_champion}')


if __name__ == '__main__':
    client.run(discord_key)
