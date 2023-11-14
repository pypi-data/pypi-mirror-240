from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.health_bar import HealthBar
from perlin_noise import PerlinNoise
from threading import Thread
from numba import jit
from ursina import *
import pickle
import random
import sys
import os

current_directory = os.getcwd()

app = Ursina(title="Block_Game", fullscreen=True)
CS = 1
RADIUS = 8
Y_1 = 0
Y_2 = 10

player = FirstPersonController()
player.speed = 7
player.mouse_sensitivity = [70, 70]
player.jump_height = 2
player.height = 30

window.cog_button.visible = False
window.exit_button.visible = False
Sky()
menu_open = False
seed1 = os.path.join(current_directory, "data", "seed.txt")

cobblestone = "assets/Cobblestone.jpeg"
stone = "assets/Stone.jpeg"
grass = "assets/Grass.jpeg"
brick = "assets/Brick.jpeg"
dirt = "assets/Dirt.jpeg"
wood = "assets/Wood.jpeg"
wool = "assets/Wool.jpeg"
log = "assets/Log.jpeg"

with open(seed1, "a") as rf:
    file_content = rf.read().strip()
    try:
        seed = int(file_content)
        print("\033[32mSEED LOADED.\033[0m")
    except ValueError:
        seed = random.randint(1, 100000)
        print("\033[32mSEED GENERATED.\033[0m")

noise = PerlinNoise(octaves=4, seed=seed)
generation_textures = [stone, grass, dirt, cobblestone]
block_textures = [grass, dirt, wood, log, cobblestone, stone, wool, brick]
selected_block_index = 0


def seed_decision(key, key_input, info, printed_text):
    if key == key_input:
        with open(seed1, "w") as f:
            f.write(info)
            print(f"\033[32mSEED {printed_text}.\033[0m")


class Voxel(Button):
    def __init__(self, position=(0, 0, 0), is_generated=True):
        voxel_y = position[1]

        if is_generated:
            if voxel_y >= 1:
                textures = [grass, dirt]
                block_texture = random.choice(textures)
            elif voxel_y >= 0:
                textures = [cobblestone, dirt]
                block_texture = random.choice(textures)
            elif voxel_y >= -2:
                textures = [cobblestone, stone]
                block_texture = random.choice(textures)
            else:
                block_texture = stone
        else:
            block_texture = block_textures[selected_block_index]

        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=.5,
            texture=block_texture,
            color=color.color(0, 0, random.uniform(0.7, 1.0)),
            highlight_color=color.gray,
            collider='mesh'
        )

        self.scale = (1, 1, 1)

    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                if not menu_open:
                    destroy(self)
            elif key == "right mouse down":
                if not menu_open:
                    hit_info = raycast(camera.world_position,
                                       camera.forward, distance=20)
                    if hit_info.hit:
                        Voxel(position=hit_info.entity.position + hit_info.normal, is_generated=False)


@jit
def destroy_chunk(x, z):
    for ent in scene.entities:
        if isinstance(ent, Voxel) and ent.position[0] // CS == x and ent.position[2] // CS == z:
            destroy(ent)


@jit
def generate_chunk(chunk_x, chunk_z):
    chunk_entities = []
    for z in range(chunk_z * CS, (chunk_z + 1) * CS):
        for x in range(chunk_x * CS, (chunk_x + 1) * CS):
            y = noise([x * .02, z * .02])
            y = floor(y * 8.5)
            chunk_entities.append(Voxel(position=(x, y, z)))

    return chunk_entities


loaded_chunks = {}


@jit
def manage_chunks_around_player(player_position):
    player_chunk_x = int(player_position.x) // CS
    player_chunk_z = int(player_position.z) // CS

    chunks_to_remove = []
    for chunk_cords, chunk_entities in loaded_chunks.items():
        x, z = chunk_cords
        if (
                x < player_chunk_x - RADIUS or
                x > player_chunk_x + RADIUS or
                z < player_chunk_z - RADIUS or
                z > player_chunk_z + RADIUS
        ):
            chunks_to_remove.append(chunk_cords)
            for chunk_ent in chunk_entities:
                chunk_ent.enabled = False

    for chunk_cords in chunks_to_remove:
        del loaded_chunks[chunk_cords]

    for x in range(player_chunk_x - RADIUS, player_chunk_x + RADIUS + 1):
        for z in range(player_chunk_z - RADIUS, player_chunk_z + RADIUS + 1):
            chunk_cords = (x, z)
            if chunk_cords not in loaded_chunks:
                chunk_entities = generate_chunk(x, z)
                loaded_chunks[chunk_cords] = chunk_entities


class Hotbar(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='quad',
            scale=(0.1, 0.1),
            position=(-0.45, -0.45),  # Adjust the position as needed
            texture=block_textures[selected_block_index]
        )
        self.texture = None

    def update_texture(self):
        self.texture = block_textures[selected_block_index]

    def input(self, key):
        if key.isdigit():
            index = int(key) - 1
            if 0 <= index < len(block_textures) and index != 8:
                global selected_block_index
                selected_block_index = index
                self.update_texture()

    def scroll_up(self):
        global selected_block_index
        selected_block_index = (
                                       selected_block_index - 1) % len(block_textures)
        if selected_block_index == 8:
            selected_block_index = 0
        self.update_texture()

    def scroll_down(self):
        global selected_block_index
        selected_block_index = (
                                       selected_block_index + 1) % len(block_textures)
        if selected_block_index == 8:
            selected_block_index = 0
        self.update_texture()


hotbar = Hotbar()


@jit
def input(key):
    if key == "escape":
        app.destroy()
        sys.exit()

    seed_decision(key, "enter", str(seed), "SAVED")
    seed_decision(key, "backspace", "", "DELETED")

    if held_keys["space"]:
        player.jump()

    if key == "f":
        player.y += 35

    if key.isdigit():
        hotbar.input(key)
    elif key == "scroll up":
        hotbar.scroll_up()
    elif key == "scroll down":
        hotbar.scroll_down()


@jit
def update():
    if player.y < -10:
        player.x += 1
        player.y = 20
        player.z += 1

    if held_keys["control"]:
        player.speed = 15
    elif held_keys["shift"]:
        player.speed = 5

    manage_chunks_around_player(player.position)


def save_app():
    app_state = {
        'seed': seed,
        'loaded_chunks': loaded_chunks,
    }
    with open("/data/save_app.pkl", "wb") as f:
        pickle.dump(app_state, f)
    print("app saved.")


def load_app():
    try:
        with open("data/save_app.pkl", "rb") as f:
            app_state = pickle.load(f)
        global seed, loaded_chunks
        seed = app_state['seed']
        loaded_chunks = app_state['loaded_chunks']
        print("app loaded.")
    except FileNotFoundError:
        print("No saved app found.")


Thread(target=generate_chunk(0, 0)).start()


class LoadingWheel(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.parent = camera.ui
        self.point = Entity(parent=self, model=Circle(
            24, mode='point', thickness=.03), color=color.light_gray, y=.75, scale=2, texture='circle')
        self.point2 = Entity(parent=self, model=Circle(
            12, mode='point', thickness=.03), color=color.light_gray, y=.75, scale=1, texture='circle')

        self.scale = .025
        self.text_entity = Text(world_parent=self, text='loading...', origin=(
            0, 1.5), color=color.light_gray)
        self.y = -.25

        self.bg = Entity(parent=self, model='quad',
                         scale_x=camera.aspect_ratio, color=color.black, z=1)
        self.bg.scale *= 400

        for key, value in kwargs.items():
            setattr(self, key, value)

    def update(self):
        self.point.rotation_y += 5
        self.point2.rotation_y += 3


if __name__ == '__main__':
    window.color = color.white
    loading_screen = LoadingWheel(enabled=False)


    def load_textures():
        textures_to_load = ["Grass.jpeg", "Dirt.jpeg",
                            "Wood.jpeg", "Log.jpeg",
                            "Cobblestone.jpeg", "Stone.jpeg",
                            "Wool.jpeg", "Brick.jpeg"] * 50
        bar = HealthBar(max_value=len(textures_to_load), value=0, position=(-.5, -.35, -2),
                        scale_x=1, animation_duration=0, world_parent=loading_screen, bar_color=color.gray)
        for i, tex in enumerate(textures_to_load):
            load_texture(tex)
            bar.value = i + 1
        print('loaded textures')
        loading_screen.enabled = False


    loading_screen.enabled = True
    t = time.time()

    try:
        Thread(target=load_textures, args='').run()
    except Exception as e:
        print('error starting thread', e)

    invoke(load_textures, delay=100)

    app.run()