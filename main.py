import discord
from discord.ext import commands
import PyPDF2
from move import catchMove

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

discord_token = 'MTE5Mzk4MzQ1OTQ3MTkyOTQ0NA.G1gcpv.B0s26K06WKJRhxJ5Oc3j4dxfFjzaWbp_d83suQ'

@bot.command()
async def moves(ctx,*,texto):
    await ctx.send(catchMove(texto))


bot.run(discord_token)