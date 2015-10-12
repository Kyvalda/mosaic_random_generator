from PIL import Image
from random import randrange

class PileMosaic:
    def __init__(self):
        self.width, self.height = 2380, 2800
        self.filename = "pile_mosaic.png"
        self.crema = (240, 233, 227)
        self.choco = (89, 62, 53)
        self.luna = (43, 97, 123)
        self.latte = (195, 175, 148)
        self.piscina = (170, 200, 211)
        self.lavanda = (189, 192, 209)
        self.viola = (133, 108, 140)
        self.morado = (121, 69, 92)
        self.rosa = (222, 179, 172)
        self.flamingo = (238, 157, 140)
        self.color_tuple = (self.crema, self.choco, self.luna, self.latte, self.piscina)
        # self.color_tuple = (self.lavanda, self.viola, self.rosa, self.morado, self.flamingo)
        self.tile_width = 300
        self.tile_height = 100

    def create_new_image(self):
        self.image = Image.new("RGB", (self.width, self.height), "white")
        self.data = [(255, 255, 255)]*(self.width*self.height)

    def write_image(self):
        self.image.save(self.filename, "PNG")

    def hex_to_rgb(value):
        value = value.lstrip('#')
        lv = len(value)
        return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

    def rgb_to_hex(rgb):
        return '#%02x%02x%02x' % rgb

    def place_pile(self, color, x=0, y=0):
        for i in range(self.tile_width):
            for j in range(self.tile_height):
                self.image.im.putpixel((x + i, y + j), color)

    def fill_random(self):
        for x in range(self.width / self.tile_width):
            for y in range(self.height / self.tile_height):
                current_color = randrange(5)
                self.place_pile(self.color_tuple[current_color], x=x*self.tile_width, y=y*self.tile_height)

    def create_random_pattern(self):
        initial_pattern = []
        for x in range(self.width / self.tile_width):
            initial_pattern.append([])
            for y in range(self.height / self.tile_height):
                temp_list = list(self.color_tuple)
                if x - 1 >= 0:
                    try:
                        temp_list.remove(initial_pattern[x - 1][y])
                    except ValueError:
                        pass
                if y - 1 >= 0:
                    try:
                        temp_list.remove(initial_pattern[x][y - 1])
                    except ValueError:
                        pass
                initial_pattern[x].append(temp_list[randrange(len(temp_list))])
        return initial_pattern
 
    def fill(self, pattern):
        for x in range(self.width / (self.tile_width + 4)):
            for y in range(self.height / (self.tile_height + 4)):
                self.place_pile(pattern[x][y], x=x*(self.tile_width+4), y=y*(self.tile_height+4))
        

pile = PileMosaic()
pile.create_new_image()
pile.fill(pile.create_random_pattern())
pile.write_image()
