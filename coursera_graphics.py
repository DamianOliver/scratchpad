import pygame
import os

pygame.init()

screen_width = 1200
screen_height = 600

class Level(object):
    coordinates = [[["Tile1.png", screen_width - 1200, screen_height - 50], ["Tile2.png", screen_width - 1150, screen_height - 50], ["Tile2.png", screen_width - 1100, screen_height - 50], ["Tile2.png", screen_width - 1050, screen_height - 50], ["Tile3.png", screen_width - 1000, screen_height - 50], \
    ["Tile14.png", screen_width - 900, screen_height - 150], ["Tile15.png", screen_width - 850, screen_height - 150], ["Tile15.png", screen_width - 800, screen_height - 150], ["Tile15.png", screen_width - 750, screen_height - 150], ["Tile16.png", screen_width - 700, screen_height - 150], \
        ["Tile14.png", screen_width - 700, screen_height - 250], ["Tile15.png", screen_width - 650, screen_height - 250], ["Tile15.png", screen_width - 600, screen_height - 250], ["Tile15.png", screen_width - 550, screen_height - 250], ["Tile15.png", screen_width - 500, screen_height - 250], ["Tile16.png", screen_width - 450, screen_height - 250], \
            ["Tile14.png", screen_width - 350, screen_height - 300], ["Tile15.png", screen_width - 300, screen_height - 300], ["Tile15.png", screen_width - 250, screen_height - 300], ["Tile15.png", screen_width - 200, screen_height - 300], ["Tile15.png", screen_width - 150, screen_height - 300], ["Tile15.png", screen_width - 100, screen_height - 300], ["Tile16.png", screen_width - 50, screen_height - 300] \
        ]]

    def __init__(self, id):
        self.id = id
        path = "png/Tiles/"
        all_images = os.listdir(path)
        self.img = {image: pygame.transform.scale(pygame.image.load(path + image).convert_alpha(), (50,50)) for image in all_images}
    
    def build_level(self, surface):
        for tile in self.coordinates[self.id]:
            surface.blit(self.img[tile[0]], (tile[1], tile[2]))

def main():
    game_clock = pygame.time.Clock()
    screen_size = (screen_width, screen_height)
    screen = pygame.display.set_mode(screen_size, 0, 32)
    background = pygame.image.load('png/BG.png').convert()

    level = Level(0)

    while True:
        game_clock.tick(45)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.blit(pygame.transform.scale(background, screen_size), (0,0))
        level.build_level(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()