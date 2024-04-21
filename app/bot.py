import discord
from dotenv import load_dotenv
import os


load_dotenv()
DISCORD_BOT_TOKEN = os.getenv("DC_BOT_TOKEN")

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'我們已在線啦 {client.user}')

@client.event
async def on_message(message):
    print(message)
    if message.author == client.user:
        return

    print(message.content)
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(DISCORD_BOT_TOKEN)