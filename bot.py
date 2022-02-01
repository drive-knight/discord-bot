import discord
from discord.ext import commands
import os
import random

settings = {
    'bot': 'info',
    'id': 843794727824523265,
    'prefix': '!',
}

bot = commands.Bot(command_prefix=settings['prefix'])

gifs = ('https://i.imgur.com/8JGpqi8.gif', 'https://i.imgur.com/EZrsYyu.gif', 'https://i.imgur.com/7zEEI0C.gif',
        'https://i.imgur.com/0SpBiAn.gif', 'https://i.imgur.com/5mAm5yA.gif', 'https://i.imgur.com/xmdhGdV.gif',
        'https://i.imgur.com/RV5YOMy.gif', 'https://i.imgur.com/BGcWxa0.gif', 'https://i.imgur.com/I8iN2iv.gif',
        'https://i.imgur.com/40lsJPi.gif', 'https://i.imgur.com/FC73FLS.gif', 'https://i.imgur.com/RvdRd4O.gif'
        'https://i.imgur.com/wQVdG5P.gif', 'https://i.imgur.com/p2lnrna.gif', 'https://i.imgur.com/wQVdG5P.gif')


@bot.command(pass_context=True)
async def info(ctx, member: discord.Member = None):
    if not member:
        member = ctx.message.author
    roles = [role for role in member.roles]
    emb = discord.Embed(colour=discord.Colour.blue(), timestamp=ctx.message.created_at,
                        title=f"User Info - {member}")
    emb.set_thumbnail(url=member.avatar_url)
    emb.set_footer(text=f"Requested by {ctx.author}")

    emb.add_field(name="ID:", value=member.id)
    emb.add_field(name="Name:", value=member.display_name)
    emb.add_field(name="Nick:", value=member.nick)

    emb.add_field(name="Created Account On:", value=member.created_at.strftime("%d.%m.%Y, %I:%M %p UTC"))
    emb.add_field(name="Joined Server On:", value=member.joined_at.strftime("%d.%m.%Y, %I:%M %p UTC"))

    emb.add_field(name="Roles:", value="".join([role.mention for role in roles[1:]]))
    await ctx.send(embed=emb)


@bot.command()
async def ts(ctx):
    embed = discord.Embed()
    embed.set_image(url=random.choice(gifs))
    await ctx.send(embed=embed)

token = os.environ.get('BOT_TOKEN')

bot.run(str(token))
