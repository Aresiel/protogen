import discord
import config
from discord.ext import commands
import gifs
import random

class GifCommandsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="snuggle")
    async def snuggle(self, ctx, *args):
    	if (len(args) == 0):
        	return
    	embed = discord.Embed(title="", colour=config.colour, description=(ctx.message.author.mention + " " + "**snuggled**" + " " + '**,** '.join(args) + "**, how cute!**"))
    	GIFlist = gifs.SnuggleList
    	GIF = random.choice(GIFlist)
    	embed.set_image(url=GIF)
    	await ctx.send(embed=embed)


    @commands.command(name="hug")
    async def hug(self, ctx, *args):
    	if (len(args) == 0):
        	return
    	embed = discord.Embed(title="", colour=config.colour, description=(ctx.message.author.mention + " " + "**hugged**" + " " + '**,** '.join(args) + "**, how lovely!**"))
    	GIFlist = gifs.HugList
    	GIF = random.choice(GIFlist)
    	embed.set_image(url=GIF)
    	await ctx.send(embed=embed)


    @commands.command(name='pat')
    async def pat(self, ctx, *args):
        if (len(args) == 0):
            return
        embed = discord.Embed(title="", colour=config.colour, description=(ctx.message.author.mention + " " + "**pat**" + " " + '**,** '.join(args) + "**, how beautiful!**"))
        GIFlist = gifs.PatList
        GIF = random.choice(GIFlist)
        embed.set_image(url=GIF)
        await ctx.send(embed=embed)


    @commands.command(name='boop', aliases=['bp'])
    async def boop(self, ctx, *args):
    	if (len(args) == 0):
        	return
    	embed = discord.Embed(title="", colour=config.colour, description=(ctx.message.author.mention + " " + "**booped**" + " " + '**,** '.join(args) + "**, so soft!**"))
    	GIFlist = gifs.BoopList
    	GIF = random.choice(GIFlist)
    	embed.set_image(url=GIF)
    	await ctx.send(embed=embed)


    @commands.command(name='kiss', aliases=['smooch'])
    async def kiss(self, ctx, *args):
    	if (len(args) == 0):
       	 return
    	embed = discord.Embed(title="", colour=config.colour, description=(ctx.message.author.mention + " " + "**smooched**" + " " + '**,** '.join(args) + "**, lovely!**"))
    	GIFlist = gifs.KissList
    	GIF = random.choice(GIFlist)
    	embed.set_image(url=GIF)
    	await ctx.send(embed=embed)


    @commands.command(name="lick")
    async def lick(self, ctx, *args):
    	if (len(args) == 0):
        	return
    	embed = discord.Embed(title="", colour=config.colour, description=(ctx.message.author.mention + " " + "**licked**" + " " + '**,** '.join(args) + "**, tasty!**"))
    	GIFlist = gifs.LickList
    	GIF = random.choice(GIFlist)
    	embed.set_image(url=GIF)
    	await ctx.send(embed=embed)


    @commands.command(name="cuddle")
    async def cuddle(self, ctx, *args):
    	if (len(args) == 0):
        	return
    	embed = discord.Embed(title="", colour=config.colour, description=(ctx.message.author.mention + " " + "**cuddled**" + " " + '**,** '.join(args) + "**, heartwarming!**"))
    	GIFlist = gifs.CuddleList
    	GIF = random.choice(GIFlist)
    	embed.set_image(url=GIF)
    	await ctx.send(embed=embed)


def setup(bot):
	bot.add_cog(GifCommandsCog(bot))
