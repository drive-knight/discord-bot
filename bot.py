import discord
from discord.ext import commands
import os

settings = {
    'bot': 'info',
    'id': 843794727824523265,
    'prefix': '!',
}

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=settings['prefix'], intents=intents)

gifs = {'sbor': 'https://i.imgur.com/8JGpqi8.gif', 'legenda': 'https://i.imgur.com/EZrsYyu.gif',
        'ladno': 'https://i.imgur.com/5mAm5yA.gif', 'josko': 'https://i.imgur.com/RV5YOMy.gif',
        'zavtra': 'https://i.imgur.com/I8iN2iv.gif', 'chel': 'https://i.imgur.com/40lsJPi.gif',
        'idem': 'https://i.imgur.com/FC73FLS.gif', 'che': 'https://i.imgur.com/RvdRd4O.gif',
        'krinj': 'https://i.imgur.com/wQVdG5P.gif'}


@bot.command(pass_context=True)
async def info(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=discord.Colour.blue(), timestamp=ctx.message.created_at,
                          title="User Info")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Запросил {ctx.author}")

    embed.add_field(name="ID:", value=member.id, inline=True)
    embed.add_field(name="Ник:", value=f'{member}', inline=True)
    embed.add_field(name="Ник на сервере:", value=member.nick, inline=True)
    embed.add_field(name="Аккаунт создан:", value=member.created_at.strftime("%d.%m.%Y, %H:%M "), inline=True)
    embed.add_field(name="Присоединился к серверу:", value=member.joined_at.strftime("%d.%m.%Y, %H:%M "), inline=True)
    embed.add_field(name='Статус:', value=str(member.status).title(), inline=True)
    embed.add_field(name="Роли:", value="".join([role.mention for role in roles[1:]]), inline=True)

    await ctx.send(embed=embed)


@bot.command(pass_context=True)
async def serverinfo(ctx, guild: discord.Guild = None):
    if not guild:
        guild = ctx.guild
    embed = discord.Embed(title="Server Info")
    embed.set_thumbnail(url=guild.icon_url)
    embed.add_field(name="ID:", value=guild.id, inline=True)
    embed.add_field(name="Владелец:", value=guild.owner, inline=True)
    embed.add_field(name="Регион:", value=guild.region, inline=True)
    embed.add_field(name="Сервер создан:", value=guild.created_at.strftime("%d.%m.%Y, %H:%M "), inline=True)
    embed.add_field(name="Пользователи:", value=str(len(guild.members)), inline=True)
    embed.add_field(name='Люди:', value=str(len(list(filter(lambda m: not m.bot, guild.members)))), inline=True)
    embed.add_field(name="Боты:", value=str(len(list(filter(lambda m: m.bot, guild.members)))), inline=True)
    #embed.add_field(name="Забаненные пользователи:", value=str(len(await guild.bans())), inline=True)
    #embed.add_field(name='Приглашения', value=str(len(await guild.invites())), inline=True)
    embed.add_field(name="Роли:", value=str(len(guild.roles)), inline=True)
    embed.add_field(name="Эмодзи:", value=str(len(guild.emojis)))

    await ctx.send(embed=embed)


@bot.command()
async def sbor(ctx):
    embed = discord.Embed()
    embed.set_image(url=gifs['sbor'])
    await ctx.send(embed=embed)


@bot.command()
async def legenda(ctx):
    embed = discord.Embed()
    embed.set_image(url=gifs['legenda'])
    await ctx.send(embed=embed)


@bot.command()
async def ladno(ctx):
    embed = discord.Embed()
    embed.set_image(url=gifs['ladno'])
    await ctx.send(embed=embed)


@bot.command()
async def josko(ctx):
    embed = discord.Embed()
    embed.set_image(url=gifs['josko'])
    await ctx.send(embed=embed)


@bot.command()
async def zavtra(ctx):
    embed = discord.Embed()
    embed.set_image(url=gifs['zavtra'])
    await ctx.send(embed=embed)


@bot.command()
async def chel(ctx):
    embed = discord.Embed()
    embed.set_image(url=gifs['chel'])
    await ctx.send(embed=embed)


@bot.command()
async def idem(ctx):
    embed = discord.Embed()
    embed.set_image(url=gifs['idem'])
    await ctx.send(embed=embed)


@bot.command()
async def che(ctx):
    embed = discord.Embed()
    embed.set_image(url=gifs['che'])
    await ctx.send(embed=embed)


@bot.command()
async def krinj(ctx):
    embed = discord.Embed()
    embed.set_image(url=gifs['krinj'])
    await ctx.send(embed=embed)


token = os.environ.get('BOT_TOKEN')

bot.run(str(token))
