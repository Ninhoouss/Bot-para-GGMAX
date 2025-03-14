import discord
from discord.ext import commands
import asyncio

TOKEN = 'TOKEN_DO_BOT_FRACO'  # Substitua pelo token do bot
PREFIX = '!fraco'

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f'Bot Fraco conectado como {bot.user}')

# Comando para enviar mensagens em massa (lento)
@bot.command()
async def raid(ctx, quantidade: int, *, mensagem: str):
    if ctx.author.guild_permissions.administrator:
        for i in range(quantidade):
            await ctx.send(f"{mensagem} - {i+1}")
            await asyncio.sleep(1)  # Intervalo de 1 segundos
    else:
        await ctx.send("Você não tem permissão para usar este comando.")

# Comando para criar alguns canais (lento)
@bot.command()
async def create_channels(ctx, quantidade: int, nome: str):
    if ctx.author.guild_permissions.administrator:
        for i in range(quantidade):
            await ctx.guild.create_text_channel(f"{nome}-{i+1}")
            await asyncio.sleep(1)  # Intervalo de 1 segundos
    else:
        await ctx.send("Você não tem permissão para usar este comando.")

bot.run(TOKEN)