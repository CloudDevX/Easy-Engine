from opensimplex import OpenSimplex
import random

SEED = random.randint(-999999,999999)
noise = OpenSimplex(SEED)
random.seed(SEED)

def generate_chunk(CHUNK_SIZE,x,y,tile_blockstates):
    To_do = []
    scale = 15

    chunk_data = {}
    for y_pos in range(CHUNK_SIZE):
        for x_pos in range(CHUNK_SIZE):
            target_x = x * CHUNK_SIZE + x_pos #The generation start at "-2" and not "0" for screen problem
            target_y = y * CHUNK_SIZE + y_pos
            value = int(noise.noise2d(target_x*0.05,0)*scale)

            tile_type = "air"
            attribute = {}
            if target_y > 12 - value: tile_type = "stone"

            elif target_y > 8 - value: tile_type="dirt"

            elif target_y == 8 - value:
                if random.randint(1,5) > 2:
                    tile_type="plant"
                    attribute["pos"] = []
                    attribute["type"] = []
                    size = random.randint(4,7)
                    for plant in range(size):
                        attribute["pos"].append(plant*15//size)
                        attribute["type"].append(random.choice(["plant_0","plant_1","plant_2","plant_3"]))
                elif random.randint(0,8) == 0:
                    tile_type="log"
                    for size in range(random.randint(7,13)):
                        To_do.append({"type":"log","x":target_x,"y":target_y-size})

                elif random.randint(1,3) == 1: 
                    tile_type="torch"
            
            chunk_data[target_x,target_y] = {"type":tile_type,"attribute":attribute,"break":tile_blockstates[tile_type]["hardness"]}
    return chunk_data,To_do

def get_seed():
    return SEED

def create_block(tile_type,tile_blockstates):
    attribute = {}
    if tile_type =="plant":
        attribute["pos"] = []
        attribute["type"] = []
        size = random.randint(4,7)
        for plant in range(size):
            attribute["pos"].append(plant*15//size)
            attribute["type"].append(random.choice(["plant_0","plant_1","plant_2","plant_3"]))

    return {"type":tile_type,"attribute":attribute,"break":tile_blockstates[tile_type]["hardness"]}