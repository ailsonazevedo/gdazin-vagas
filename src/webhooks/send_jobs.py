import os
from discord_webhook import DiscordWebhook, DiscordEmbed
from dotenv import load_dotenv

load_dotenv()

url = os.getenv('DISCORD_WEBHOOK')

class SendJobs:
    def send(jobs):
        for job in jobs:
            webhook = DiscordWebhook(url=url)
            embed = DiscordEmbed(title=job["title"], description=job["url"], color="8D21ED")
            embed.set_author(name=job["author"], url=job["author_url"], icon_url=job["url_avatar"])
            embed.set_footer(text="Fonte: apibr.com")
            embed.set_thumbnail(url=job["org_avatar"])
            embed.set_timestamp()
            keywords_list = "\n".join(job["keywords"])
            embed.add_embed_field(name="Palavras-chaves", value=keywords_list, inline=False)
            embed.add_embed_field(name="Data de criação da vaga", value=job["created_at"])
            embed.add_embed_field(name="Repositório", value=job["repository"])

            webhook.add_embed(embed)
            response = webhook.execute()

