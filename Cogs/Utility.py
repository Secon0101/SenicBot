import discord
from discord.ext import commands
from pytz import timezone
from datetime import datetime


class Utility(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    
    @commands.command(name="시각", aliases=["시간"], help="전세계의 현재 시각을 알려드립니다.", usage="$시각 <지역 이름>")
    async def cmd_time(self, ctx: commands.Context, location: str = None):
        TIMEZONE_LIST = (
            (("대한민국", "한국", "서울"),
            "Asia/Seoul"),
            (("캘리포니아", "로스앤젤리스", "로스앤젤레스"),
            "America/Los_Angeles")
        )
        
        zone: str = None
        for z in TIMEZONE_LIST:
            if location in z:
                zone = z[1]
                break
        
        if zone is not None:
            time = datetime.now(timezone(zone))
            await ctx.send(f"{location}의 현재 시각은 **{time.strftime('%Y년 %m월 %d일 %H시 %M분 %S초')}**입니다. `({time.tzinfo})`")
            
        else:
            embed = discord.Embed(title="시간대 목록", description="ex) `$시각 캘리포니아`")
            for z in TIMEZONE_LIST:
                embed.add_field(name=z[1], value=' '.join(z[0]))
            await ctx.send(f"리스트에 없는 시각입니다.", embed=embed)


def setup(bot):
    bot.add_cog(Utility(bot))
