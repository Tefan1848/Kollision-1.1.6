#Grygierek

import os
from random import randint

import pygame

class Settings():
    window_width = 700
    window_height = 200
    fps = 60
    title = "Grygierek 1.1.6"
    file_path = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(file_path, "images")

class Obst(pygame.sprite.Sprite):
    def __init__(self, banane) -> None:
        super().__init__()
        self.image = pygame.image.load(os.path.join(Settings.image_path, banane)).convert_alpha()
        self.rect = self.image.get_rect()
        self.radius = self.rect.width // 2
        self.circle = pygame.circle.from_surface(self.image)
        self.rect.left = 300
        self.rect.centery = Settings.window_height // 2

    def __init__(self, ananas) -> None:
        super().__init__()
        self.image = pygame.image.load(os.path.join(Settings.image_path, ananas)).convert_alpha()
        self.rect = self.image.get_rect()
        self.radius = self.rect.width // 2
        self.circle = pygame.circle.from_surface(self.image)
        self.rect.left = 300
        self.rect.centery = Settings.window_height // 2

    def __init__(self, apfel) -> None:
        super().__init__()
        self.image = pygame.image.load(os.path.join(Settings.image_path, apfel)).convert_alpha()
        self.rect = self.image.get_rect()
        self.radius = self.rect.width // 2
        self.circle = pygame.circle.from_surface(self.image)
        self.rect.left = 300
        self.rect.centery = Settings.window_height // 2

    def __init__(self, pflaume) -> None:
        super().__init__()
        self.image = pygame.image.load(os.path.join(Settings.image_path, pflaume)).convert_alpha()
        self.rect = self.image.get_rect()
        self.radius = self.rect.width // 2
        self.circle = pygame.circle.from_surface(self.image)
        self.rect.left = 300
        self.rect.centery = Settings.window_height // 2

    def __init__(self, oragne) -> None:
        super().__init__()
        self.image = pygame.image.load(os.path.join(Settings.image_path, oragne)).convert_alpha()
        self.rect = self.image.get_rect()
        self.radius = self.rect.width // 2
        self.circle = pygame.circle.from_surface(self.image)
        self.rect.left = 300
        self.rect.centery = Settings.window_height // 2


    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Bomb(pygame.sprite.Sprite):
    def __init__(self, bomben, colorkey=None) -> None:
        super().__init__()
        if colorkey is not None:
            self.image = pygame.image.load(Settings.get_image_path(bomben)).convert()
            self.image.set_colorkey(colorkey)
        else:
            self.image = pygame.image.load(Settings.get_image_path(bomben)).convert_alpha()
        self.rect = self.image.get_rect()
        self.vel = [0, 0]

    def update(self) -> None:
        self.rect.top += self.vel[1]
        self.rect.left += self.vel[0]

        if self.rect.right >= Settings.SCREENRECT.width:
            self.vel[0] *= -1
        if self.rect.left <= 0:
            self.vel[0] *= -1

        if self.rect.bottom >= Settings.SCREENRECT.height:
            self.vel[1] *= -1
        if self.rect.top <= 0:
            self.vel[1] *= -1

        return super().update()


class Bomb(pygame.sprite.Sprite):
    def __init__(self, filename, colorkey=None) -> None:
        super().__init__()
        if colorkey is not None:
            self.image = pygame.image.load(Settings.get_image_path(filename)).convert()
            self.image.set_colorkey(colorkey)
        else:
            self.image = pygame.image.load(Settings.get_image_path(filename)).convert_alpha()
        self.rect = self.image.get_rect()
        self.vel = [0, 0]

    def update(self) -> None:
        self.rect.top += self.vel[1]
        self.rect.left += self.vel[0]

        if self.rect.right >= Settings.SCREEMRECT.width:
            self.vel[0] *= -1
        if self.rect.left <= 0:
            self.vel[0] *= -1

        if self.rect.bottom >= Settings.SCREEMRECT.height:
            self.vel[1] *= -1
        if self.rect.top <= 0:
            self.vel[1] *= -1

        return super().update()



class Game():
    def __init__(self) -> None:
        super().__init__()
        os.environ['SDL_VIDEO_WINDOW_POS'] = "10, 50"
        pygame.init()
        pygame.display.set_caption(Settings.title)
        self.font = pygame.font.Font(pygame.font.get_default_font(), 24)

        self.screen = pygame.display.set_mode((Settings.window_width, Settings.window_height))
        self.clock = pygame.time.Clock()

        self.ananas = Obst("ananas.png")
        self.apfel = Obst("apfel.png")
        self.banane = Obst("alienbig2.png")
        self.oragne = Obst("oragne.png")
        self.pflaume = Obst("pflaume.png")
        self.bomb = Bomb("bomben.png")

        self.all_obstacles = pygame.sprite.Group()
        self.all_obstacles.add(self.ananas)
        self.all_obstacles.add(self.apfel)
        self.all_obstacles.add(self.banane)
        self.all_obstacles.add(self.oragne)
        self.all_obstacles.add(self.pflaume)
        self.all_bomb.add(self.bomb)

        self.running = False

    def run(self):
        self.resize()

        self.running = True
        while self.running:
            self.clock.tick(60)
            self.watch_for_events()
            self.update()
            self.draw()

        pygame.quit()

    def watch_for_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def update(self):
        self.counter += 1
        if self.counter >= 30:
            bomb = Bomb ("bomben.png")
            bomb.vel[0] = randint(1, 3)
            bomb.vel[1] = randint(1, 3)
            self.bombs.add(bomb)
            self.counter = 0
        for obst in self.obst.sprites():
            pygame.sprite.spritecollide(obst, self.bombs, True)

        self.bombs.update()

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.bombs.draw(self.screen)
        self.obsts.draw(self.screen)
        pygame.display.flip()

    def resize(self):
        total_width = self.ananas.rect.width
        total_width += self.apfel.rect.width
        total_width += self.banane.rect.width
        total_width += self.oragne.rect.width
        total_width += self.pflaume.rect.width

        padding = (Settings.window_width - total_width) // 4
        self.ananas.rect.left = padding
        self.apfel.rect.left = self.apfel.rect.right + padding
        self.banane.rect.left = self.banane.rect.right + padding
        self.oragne.rect.left = self.oragne.rect.right + padding
        self.pflaume.rect.left = self.pflaume.rect.right + padding

def main():
    game = Game()
    game.run()

if __name__ == "__maim__":
    main()


# Zunächst habe ich die Datei die im Unterricht vorgezeigt ist
# angeschaut und im Anschluss die Datei mit umbennanten Varibeln
# umgeändert, da die Hausaufgaben nicht funktiontstüchtig
# wahr

#Im Anschluss habe ich die Datei kollison.py mir als Beispiel benutzt
