import pygame

from copy import deepcopy

from settings import Settings
from field_core import FieldCore

class GameLife:
    """pass"""
    def __init__(self):
        #Власні змінні
        self.keep_drawing = False
        self.keep_erasing = False
        self.keep_live = False
        self.clock = pygame.time.Clock()
        self.fps = 5

        #Підключені класи
        self.settings = Settings()
        self.field_core = FieldCore()

        pygame.init()
        self.surface = pygame.display.set_mode(self.settings.resolution)

    def run_game(self):
        """pass"""
        while True:
            self.draw_screen()
            self.check_events()
            if self.keep_drawing or self.keep_erasing:
                self.invert_cell(pygame.mouse.get_pos())
            if self.keep_live:
                self.update_life()
            pygame.display.flip()




    def draw_screen(self):
        """pass"""
        #Фон
        self.surface.fill(pygame.Color('black'))

        # Замалювати клітинки
        for x in range(self.field_core.height):
            for y in range(self.field_core.width):
                if self.field_core.field[x][y] == True:
                    pygame.draw.rect(self.surface, pygame.Color('forestgreen'),
                                     (y * self.settings.cell_size, x * self.settings.cell_size,
                                      self.settings.cell_size, self.settings.cell_size))

        #Вертикальні прямі
        [pygame.draw.line(self.surface, pygame.Color('darkslategray'), (x, 0), (x, self.settings.height))
         for x in range(0, self.settings.width, self.settings.cell_size)]

        #Горизонтальні прямі
        [pygame.draw.line(self.surface, pygame.Color('darkslategray'), (0, y), (self.settings.width, y))
         for y in range(0, self.settings.height, self.settings.cell_size)]



    def invert_cell(self, mouse_pos):
        """pass"""
        x = mouse_pos[0] // self.settings.cell_size
        y = mouse_pos[1] // self.settings.cell_size

        if x < self.field_core.width and y < self.field_core.height:
            if self.keep_drawing:
                self.field_core.field[y][x] = True
            elif self.keep_erasing:
                self.field_core.field[y][x] = False
            else:
                self.field_core.field[y][x] = not self.field_core.field[y][x]





    def check_events(self):
        """pass"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    exit()
                elif event.key == pygame.K_p:
                    self.field_core.show_field()
                elif event.key == pygame.K_z:
                    self.keep_drawing = True
                elif event.key == pygame.K_x:
                    self.keep_erasing = True
                elif event.key == pygame.K_g:
                    self.keep_live = not self.keep_live
                elif event.key == pygame.K_c:
                    self.field_core.init_field()


            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_z:
                    self.keep_drawing = False
                elif event.key == pygame.K_x:
                    self.keep_erasing = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.invert_cell(mouse_pos)

    def check_cell(self, x, y):
        """pass"""
        count = 0
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if self.field_core.field[i][j]:
                    count += 1

        if self.field_core.field[x][y]:
            count -= 1
            if count == 2 or count == 3:
                return True
            else:
                return False
        else:
            if count == 3:
                return True
            else:
                return False


    def update_life(self):
        """pass"""
        for i in range(1, self.field_core.height-1):
            for j in range(1, self.field_core.width-1):
                self.field_core.next_field[i][j] = self.check_cell(i, j)
        self.field_core.field = deepcopy(self.field_core.next_field)
        self.clock.tick(self.fps)





if __name__ == "__main__":
    game = GameLife()
    game.run_game()






