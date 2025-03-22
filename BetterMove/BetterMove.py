from discord.ext import commands
from core import checks
import discord

class BetterMove(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.category_ids = {
            "asda": "1299775139399078010",
            "mc": "1349813171459850293",
            "dmods": "1299798139473104988"
        }

    @checks.thread_only()
    @commands.command()
    async def mc(self, ctx):        
        category = ctx.guild.get_channel(self.category_ids["mc"])
        
        if category is None or not isinstance(category, discord.CategoryChannel):
            await ctx.send("Invalid category ID, Contact Dann.")
            return
        
        try:
            await ctx.channel.edit(category=category)
            await ctx.send(f"Moved to {category.name}")
        except Exception as e:
            await ctx.send(f"An error occurred: {str(e)}")
    
    @checks.thread_only()
    @commands.command()
    async def asda(self, ctx):        
        category = ctx.guild.get_channel(self.category_ids["asda"])
        
        if category is None or not isinstance(category, discord.CategoryChannel):
            await ctx.send("Invalid category ID, Contact Dann.")
            return
        
        try:
            await ctx.channel.edit(category=category)
            await ctx.send(f"Moved to {category.name}")
        except Exception as e:
            await ctx.send(f"An error occurred: {str(e)}")
        
    @checks.thread_only()    
    @commands.command()
    async def dmods(self, ctx):        
        category = ctx.guild.get_channel(self.category_ids["dmods"])
        
        if category is None or not isinstance(category, discord.CategoryChannel):
            await ctx.send("Invalid category ID, Contact Dann.")
            return
        
        try:
            await ctx.channel.edit(category=category)
            await ctx.send(f"Moved to {category.name}")
        except Exception as e:
            await ctx.send(f"An error occurred: {str(e)}")
            
async def setup(bot):
    await bot.add_cog(BetterMove(bot))
