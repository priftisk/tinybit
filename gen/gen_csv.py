from pathlib import Path
from datetime import datetime, timedelta
import random

out = Path("fake_logs.csv")

levels = ["INFO", "WARN", "ERROR", "DEBUG"]
events = [
    "UserLogin succeeded",
    "UserLogin failed",
    "Database connection established",
    "Database connection timeout",
    "Cache miss",
    "Cache hit",
    "File uploaded",
    "File deleted",
    "Payment processed",
    "Payment declined",
    "API request completed",
    "API request failed",
]

start = datetime(2026, 1, 1, 8, 0, 0)

lines = []
for i in range(1000):
    ts = start + timedelta(seconds=i * random.randint(5, 60))
    level = random.choices(levels, weights=[50, 15, 20, 15])[0]
    event = random.choice(events)
    lines.append(f"{ts:%Y-%m-%d %H:%M:%S},{level},{event}")

out.write_text("\n".join(lines), encoding="utf-8")

print(str(out))
