from discord.ext import commands
from discord.utils import get
from core import checks
import discord

class BetterMove(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.category_ids = {
            "asda": 1299775139399078010,
            "mc": 1349813171459850293,
            "dmods": 1299798139473104988
        }
        self.staff_role_ids = {
            "admins": "1299296154885951549",
            "mcstaff": "1214942778002505749",
            "dmods": "1214942755923427378"
        }
        
    @checks.thread_only()
    @commands.command()
    async def mc(self, ctx):        
        category = discord.utils.get(ctx.guild.categories, id=self.category_ids["mc"])
        roleId = self.staff_role_ids["mcstaff"]
        
        try:
            await ctx.channel.edit(category=category, sync_permissions=True)
            await ctx.send(f"<@&{roleId}>")
        except Exception as e:
            await ctx.send(f"An error occurred: {str(e)}")
    
    @checks.thread_only()
    @commands.command()
    async def asda(self, ctx):        
        category = get(ctx.guild.categories, id=self.category_ids["asda"])
        roleId = self.staff_role_ids["admins"]
        
        try:
            await ctx.channel.edit(category=category, sync_permissions=True)
            await ctx.send(f"<@&{roleId}>")
        except Exception as e:
            await ctx.send(f"An error occurred: {str(e)}")
        
    @checks.thread_only()    
    @commands.command()
    async def dmods(self, ctx):        
        category = get(ctx.guild.categories, id=self.category_ids["dmods"])
        roleId = self.staff_role_ids["dmods"]
        
        try:
            await ctx.channel.edit(category=category, sync_permissions=True)
            await ctx.send(f"<@&{roleId}>")
        except Exception as e:
            await ctx.send(f"An error occurred: {str(e)}")
            
async def setup(bot):
    await bot.add_cog(BetterMove(bot))
