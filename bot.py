import discord
from discord.ext import commands
import os

settings = {
    'bot': 'info',
    'id': 843794727824523265,
    'prefix': '!'
}


bot = commands.Bot(command_prefix = settings['prefix'])

@bot.command(pass_context=True)
async def info(ctx, member: discord.Member = None):
    if not member:  # if member is no mentioned
        member = ctx.message.author  # set member as the author
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=discord.Colour.purple(), timestamp=ctx.message.created_at,
                          title=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}")

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Name:", value=member.display_name)

    embed.add_field(name="Created Account On:", value=member.created_at.strftime("%d.%m.%Y, %I:%M %p UTC"))
    embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%d.%m.%Y, %I:%M %p UTC"))

    embed.add_field(name="Roles:", value="".join([role.mention for role in roles[1:]]))
    await ctx.send(embed=embed)
    
token = os.environ.get('BOT_TOKEN')

bot.run(str(token))
