import discord
from discord.ext import commands
from Events.console_chatting import console_chatting
from utility import get_cogs, log


bot = commands.Bot(command_prefix='$', owner_id=540481950763319317, intents=discord.Intents.all(), help_command=None)


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("$도움말"))
    log("Logged in")


@bot.command(aliases=["r", "ㄱ"])
async def reload(ctx: commands.Context):
    for cog in get_cogs():
        bot.unload_extension(cog)
        bot.load_extension(cog)
    log("Reloaded")
    await ctx.message.add_reaction("✅")
    await ctx.message.delete(delay=3)


@bot.event
async def on_message(msg: discord.Message):
    if msg.author.bot: return
    await bot.process_commands(msg)
    
    await console_chatting(bot, msg)


if __name__ == "__main__":
    for cog in get_cogs():
        bot.load_extension(cog)
    with open("token.txt", "r") as f:
        token = f.read()

    bot.run(token)
