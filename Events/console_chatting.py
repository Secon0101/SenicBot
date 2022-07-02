import discord
from discord.ext import commands

channel_id: int = None

async def console_chatting(bot: commands.Bot, msg: discord.Message):
    if msg.channel.id == 796719890434097192:
        global channel_id
        
        # 채널 ID 설정 (ex: id 1234)
        if msg.content.startswith("id") and ' ' in msg.content:
            try:
                channel_id = int(msg.content.split()[1])
            except ValueError:
                await msg.channel.send("채널 ID가 올바르지 않습니다.")
            else:
                if bot.get_channel(channel_id) is not None:
                    await msg.channel.send(f"채널을 <#{channel_id}>(으)로 설정했습니다.")
                else:
                    await msg.channel.send(f"ID가 `{channel_id}`인 채널을 찾을 수 없습니다.")
        
        # 메세지 전송
        else:
            if channel_id is None:
                await msg.channel.send("`id <channel_id>`로 채널 ID를 설정해주세요.")
                await msg.add_reaction("❌")
            else:
                channel = bot.get_channel(channel_id)
                if channel is None:
                    await msg.channel.send(f"ID가 {channel_id}인 채널을 찾을 수 없습니다.")
                    await msg.add_reaction("❌")
                else:
                    await channel.send(msg.content)
                    await msg.add_reaction("🚀")
