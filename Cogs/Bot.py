from pydoc import describe
import discord
from discord.ext import commands


class Bot(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command(name="세닉봇", help="봇 정보를 보여줍니다.", usage="`$세닉봇`")
    async def info(self, ctx: commands.Context):
        embed = discord.Embed(title="🔧 세닉봇", description="Since 2020. 9. 21.\nhttps://github.com/Secon0101/SenicBot \n기능은 `$도움말`을 참고하세요!", color=0x747f8d)
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.set_footer(text=f"Made by {self.bot.get_user(self.bot.owner_id)}", icon_url=self.bot.get_user(self.bot.owner_id).avatar_url)
        await ctx.send(embed=embed)
    
    @commands.command(name="도움말", help="봇에서 사용할 수 있는 명령어들을 보여줍니다.", usage="`$도움말 <카테고리>` 또는 `$도움말 <명령어>`", aliases=["명령어", "help"])
    async def help(self, ctx: commands.Context, search: str = None):
        embed = discord.Embed(title="🔧 세닉봇 도움말", description="접두사는 **`$`**입니다.", color=0x747f8d)
        embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        
        # 전체 도움말 출력
        if search is None:
            for cog in self.bot.cogs:
                commands = [cmd.name for cmd in self.bot.get_cog(cog).get_commands()]
                if len(commands) > 0:
                    embed.add_field(name=f"- {cog} 카테고리", value=' '.join(commands))
            embed.description += f"\n`${ctx.command.name} <카테고리>`라고 입력하면 그 카테고리의 명령어들을 볼 수 있습니다."
        
        else:
            # 카테고리 명령어 출력
            if search in self.bot.cogs:
                embed.title = f"🔧 {search} 카테고리의 명령어"
                commands = self.bot.get_cog(search).get_commands()
                if len(commands) > 0:
                    for cmd in commands:
                        embed.add_field(name=f"- {cmd.name}", value=f"{cmd.help}\n사용법: {cmd.usage}", inline=False)
                else:
                    await ctx.send("카테고리에 명령어가 없습니다.")
                    return
            
            else:
                # 특정 명령어 출력
                cmd = self.bot.get_command(search)
                if cmd is not None:
                    embed.title = f"🔧 명령어: {cmd.name}"
                    embed.description = f"{cmd.help}\n사용법: {cmd.usage}"
                
                # 검색 실패
                else:
                    await ctx.send(f"명령어 또는 카테고리가 존재하지 않습니다.")
                    return
        
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Bot(bot))
