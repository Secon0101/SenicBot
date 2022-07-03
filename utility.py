import os
from datetime import datetime
from pytz import timezone


def get_cogs() -> list[str]:
    cogs = []
    for filename in os.listdir("Cogs"):
        if filename.endswith('.py'):
            cogs.append(f"Cogs.{filename[:-3]}")
    return cogs


def log(ctx: str):
    time = datetime.now(timezone('Asia/Seoul')).strftime("%y/%m/%d %H:%M:%S")
    print(f"[{time}] {ctx}")
