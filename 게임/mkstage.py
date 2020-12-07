import json
import random
import gfw
import pattern
from pico2d import *

resource = 'res/'

def enter():
    pattern.init()

    global Tile, hz, vt
    Tile = pattern.getTile()
    hz, vt = pattern.getTileCount()
    for i in range(vt):
        for j in range(hz):
            print(Tile[i][j])

    with open(resource + 'stage_01.json') as f:
        dicts = json.load(f)

    for i in range(100):
        d = dicts[0].copy()

        n = random.randrange(1, 5)

        d["time"] = 1 + random.randrange(60)
        d["start_x"] = Tile[vt - 1][round((hz - 1) / 5 * n)][0]
        d["start_y"] = Tile[vt - 1][hz - 1][1]
        d["shooting_pattern"] = random.randrange(1, 4)
        d["speed"] = random.randrange(100, 200)
        d["bullet_speed"] = random.randrange(1, 4)
        d["dst_x"] = Tile[vt - 1][round((hz - 1) / 5 * n)][0]
        d["dst_y"] = Tile[0][0][1]
        d["hp"] = 2
        d["MOVE_PPS"] = 2
        d["move_pattern"] = random.randrange(1, 4)
        dicts.append(d)

    dicts.sort(key=lambda d: d["time"])

    with open('stage_02.json', 'w') as f:
        json.dump(dicts, f, indent=2)

def update():
    pass

def draw():
    pass

def exit():
    pass

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()

if __name__ == '__main__':
    gfw.run_main()
