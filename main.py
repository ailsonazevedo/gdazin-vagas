import discord
import os
import requests

from src.webhooks.send_jobs import SendJobs
from services.apibr import JobService

from dotenv import load_dotenv

from discord_webhook import DiscordWebhook, DiscordEmbed

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
load_dotenv()


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Olá {member.name}, Bem vindo ao servidor Timon City!'
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")

    elif message.content.startswith("$vagas"):
        command, technology = message.content.split(" ", 1)
        job_service = JobService()
        jobs = job_service.get_jobs(technology)
        
        if jobs is None:
            await message.channel.send("Nenhuma vaga encontrada")
        else:
            await message.channel.send(f"Vagas de {technology} saindo do forno:")
            SendJobs.send(jobs)


client.run(os.getenv('DISCORD_TOKEN'))
