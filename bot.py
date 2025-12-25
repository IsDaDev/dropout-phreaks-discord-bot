import discord
import time
import embed
from discord.ext import commands

TOKEN = "[REDACTED]"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Simple cooldown storage for slash command
cooldowns = {}
COOLDOWN_SECONDS = 5

TESTSERVER = 1453396053939327148

async def sendEmbed(embedTemplate, interaction: discord.Interaction):
    user_id = interaction.user.id
    now = time.time()

    last_used = cooldowns.get(user_id, 0)
    remaining = COOLDOWN_SECONDS - (now - last_used)

    if remaining > 0:
        await interaction.response.send_message(
            f"⏳ Please wait {int(remaining)} seconds before using this again.",
            ephemeral=True
        )
        return

    cooldowns[user_id] = now
    await interaction.response.send_message(embed=embedTemplate)

@bot.event
async def on_ready():
    guild = discord.Object(id=TESTSERVER)
    await bot.tree.sync(guild=guild)  # sync only to your test server
    await bot.tree.sync()
    print(f"Logged in as {bot.user}")

@bot.tree.command(name="howtostart", description="Get information on how to get started")
async def howtostart_command(interaction: discord.Interaction):
    await sendEmbed(embed.hdigsembed(), interaction)

@bot.tree.command(name="igothacked", description="What to do when you get hacked")
async def igothacked_command(interaction: discord.Interaction):
    await sendEmbed(embed.igothackedembed(), interaction)

@bot.tree.command(name="certificates", description="Certificate list sorted by domain")
async def certificates_command(interaction: discord.Interaction):
    await sendEmbed(embed.certificatesembed(), interaction)

@bot.tree.command(name="resources", description="List of useful cybersecurity resources")
async def resources_command(interaction: discord.Interaction):
    await sendEmbed(embed.resourcesembed(), interaction)

@bot.tree.command(name="blog", description="Link for the acid.wiki blog")
async def blog_command(interaction: discord.Interaction):
    await sendEmbed(embed.blogembed(), interaction)

bot.run(TOKEN)
