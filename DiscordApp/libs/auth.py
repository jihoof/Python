import discord, asyncio
from dotenv import load_dotenv
import os

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("봇이 실행되었습니다.")
    await client.change_presence(
        status=discord.Status.online,
        activity=None
    )

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content == "테스트":
        await message.channel.send(
            f"{message.author} | {message.author.mention}, Hello"
        )
        await message.author.send(
            f"{message.author} | {message.author.mention}, User, Hello"
        )

client.run(os.getenv("DISCORD_TOKEN"))