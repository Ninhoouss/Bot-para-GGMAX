import discord
from discord.ext import commands
import asyncio

TOKEN = 'TOKEN_DO_BOT_FORTE'  # Substitua pelo token do bot
PREFIX = '!forte'

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f'Bot Forte conectado como {bot.user}')

# Comando para enviar mensagens em massa (muito rápido)
@bot.command()
async def raid(ctx, quantidade: int, *, mensagem: str):
    if ctx.author.guild_permissions.administrator:
        for i in range(quantidade):
            await ctx.send(f"{mensagem} - {i+1}")
            await asyncio.sleep(0.1)  # Intervalo de 0.1 segundos
    else:
        await ctx.send("Você não tem permissão para usar este comando.")

# Comando para criar canais em massa (muito rápido)
@bot.command()
async def create_channels(ctx, quantidade: int, nome: str):
    if ctx.author.guild_permissions.administrator:
        for i in range(quantidade):
            await ctx.guild.create_text_channel(f"{nome}-{i+1}")
            await asyncio.sleep(0.1)  # Intervalo de 0.1 segundos
    else:
        await ctx.send("Você não tem permissão para usar este comando.")

# Comando para expulsar membros em massa
@bot.command()
async def kick_members(ctx, quantidade: int):
    if ctx.author.guild_permissions.administrator:
        members = list(ctx.guild.members)
        for i in range(min(quantidade, len(members))):
            try:
                await members[i].kick(reason="Teste de raid Forte")
                print(f"Membro {members[i]} expulso.")
                await asyncio.sleep(0.1)  # Intervalo de 0.1 segundos
            except discord.Forbidden:
                print(f"Não foi possível expulsar {members[i]}.")
    else:
        await ctx.send("Você não tem permissão para usar este comando.")

# Comando para banir membros em massa
@bot.command()
async def ban_members(ctx, quantidade: int):
    if ctx.author.guild_permissions.administrator:
        members = list(ctx.guild.members)
        for i in range(min(quantidade, len(members))):
            try:
                await members[i].ban(reason="Teste de raid Forte")
                print(f"Membro {members[i]} banido.")
                await asyncio.sleep(0.1)  # Intervalo de 0.1 segundos
            except discord.Forbidden:
                print(f"Não foi possível banir {members[i]}.")
    else:
        await ctx.send("Você não tem permissão para usar este comando.")

bot.run(TOKEN)