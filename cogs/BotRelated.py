import discord
import config
import user
from discord.ext import commands

class BotRelatedCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@commands.command(name="ping", aliases=["pong", "latency"], brief="shows the bot's latency.")
async def latency(ctx):
    embed = discord.Embed(title="ProtoPaw latency", color=config.color)
    embed.add_field(name="ping", value=f'**{bot.latency:.2f}**s')
    await ctx.send(embed=embed)

@commands.command()
async def help(ctx):
    embed = discord.Embed(title='commands | `?`, `p!`', color=config.color)
    embed.add_field(name="**🔨 moderation**", value="`ban` `unban` `kick` `softban`", inline=True)
    embed.add_field(name="**🤖 bot related**", value="`help` `ping` `invite` `stats` `links` `info`", inline=True)
    embed.add_field(name="**🏗️ Utils**", value="`get_id` `avatar` `serverinfo` `random` `poll` `decide`", inline=True)
    embed.set_thumbnail(url="https://www.dropbox.com/s/yx7z6iefnx0q576/Icon.jpg?dl=1")
    embed.set_footer(text="Thank you, " + ctx.message.author.name + ", for using ProtoPaw!")
    await ctx.send(embed=embed)

@commands.command(name='invite')
async def invite(self, ctx):
    embed = discord.Embed(title='invite', color=config.colour)
    embed.add_field(name="oauth link", value="[Add ProtoPaw to your server](https://discord.com/api/oauth2/authorize?client_id=620990340630970425&permissions=806218999&scope=bot)")
    embed.set_footer(text="Thank you, " + ctx.message.author.name + ", for using ProtoPaw!")
    await ctx.send(embed=embed)

@commands.command(name="stats")
async def stats(self, ctx):
    embed = discord.Embed(title="ProtoPaw statistics", color=config.colour)
    embed.add_field(name="guilds", value=len(self.bot.guilds), inline=True)
    embed.add_field(name="users", value=len(self.bot.users), inline=True)
    await ctx.send(embed=embed)

@commands.command(name='links', brief='Discord related links')
async def links(ctx):
    embed = discord.Embed(title='Protopaw Links', color=config.color)
    embed.add_field(name='Support/community discord Server:', value="https://discord.gg/k64tAer\nhttps://discord.gg/bcjdqyn\nhttps://discord.me/thepawkingdom\nhttps://discord.st/thepawkingdom", inline=True)
    embed.add_field(name="Contact", value="ChosenFate#5108\nBluewytheRenegade#2923")
    embed.add_field(name="Social media:", value="Twitter | https://twitter.com/furrycontentuvs", inline=False)
    embed.set_thumbnail(url="https://www.dropbox.com/s/yx7z6iefnx0q576/Icon.jpg?dl=1")
    embed.set_footer(text="Thank you, " + ctx.message.author.name + ", for using ProtoPaw!")
    await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(BotRelatedCog(bot))
