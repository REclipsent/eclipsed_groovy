import discord
from discord import app_commands

MY_SERVER_ID = discord.Object(id=709287381668462652)

class EclipsedGroovy(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_SERVER_ID)
        await self.tree.sync(guild=MY_SERVER_ID)