from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print("Logged in")


if __name__ == "__main__":
    with open("token.txt", "r") as f:
        token = f.read()
        bot.run(token)
