import discord
from discord.ext import commands
from utility import get_cogs, log


bot = commands.Bot(command_prefix='$', owner_id=540481950763319317, intents=discord.Intents.all())


@bot.event
async def on_ready():
    log("Logged in")


@bot.command(aliases=["r", "ㄱ"])
async def reload(ctx: commands.Context):
    for cog in get_cogs():
        bot.unload_extension(cog)
        bot.load_extension(cog)
    log("Reloaded")
    await ctx.message.add_reaction("✅")
    await ctx.message.delete(delay=3)


if __name__ == "__main__":
    for cog in get_cogs():
        bot.load_extension(cog)
    with open("token.txt", "r") as f:
        token = f.read()

    bot.run(token)
