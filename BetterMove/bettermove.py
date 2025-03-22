from discord.ext import commands
import discord

class BetterMove(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.category_ids = {
            "asda": "1299775139399078010",
            "mc": "1349813171459850293",
            "dmods": "1299798139473104988"
        }

    @commands.command()
    async def move(self, ctx, category:str):
        if category not in self.category_ids:
            await ctx.send(f"Invalid category. Valid categories are: {', '.join(self.category_ids.keys())}")
            return
        
        category_id = self.category_ids[category]
        category = ctx.guild.get_channel(category_id)
        
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