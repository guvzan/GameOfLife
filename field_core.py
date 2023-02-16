from copy import deepcopy
from settings import Settings

class FieldCore:
    """pass"""
    def __init__(self):
        self.settings = Settings()
        self.init_field()
        self.next_field = deepcopy(self.field)

    def show_field(self):
        """pass"""
        for row in self.field:
            for cell in row:
                if cell == True:
                    print('*', end=' ')
                else:
                    print('.', end=' ')
            print()
        print()

    def init_field(self):
        """pass"""
        self.width = self.settings.width // self.settings.cell_size
        self.height = self.settings.height // self.settings.cell_size
        self.field = [[False for i in range(self.width)] for j in range(self.height)]
