import os
from time import strftime


def get_cogs() -> list[str]:
    cogs = []
    for filename in os.listdir("Cogs"):
        if filename.endswith('.py'):
            cogs.append(f"Cogs.{filename[:-3]}")
    return cogs

def log(ctx: str):
    time = strftime("%H:%M:%S")
    print(f"[{time}] {ctx}")
