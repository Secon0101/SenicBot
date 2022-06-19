import discord
from discord.ext import commands


class Bot(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command(name="세닉봇")
    async def info(self, ctx: commands.Context):
        embed = discord.Embed(title="🔧 세닉봇", description="Since 2020. 9. 21.\nhttps://github.com/Secon0101/SenicBot", color=0x747f8d)
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.set_footer(text=f"Made by {self.bot.get_user(self.bot.owner_id)}", icon_url=self.bot.get_user(self.bot.owner_id).avatar_url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Bot(bot))
