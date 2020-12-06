import json
import random

with open('stage_01.json') as f:
    dicts = json.load(f)

for i in range(100):
    d = dicts[0].copy()
    d["time"] = 1 + random.randrange(300) / 10
    d["start_x"] = random.randrange(1000)
    d["start_y"] = random.randrange(600, 1000)
    d["shooting_pattern"] = random.randint(1, 4)
    d["speed"] = random.randint(100, 200)
    d["bullet_speed"] = random.uniform(1, 3)
    dicts.append(d)

dicts.sort(key=lambda d: d["time"])

with open('stage_02.json', 'w') as f:
    json.dump(dicts, f, indent=2)
