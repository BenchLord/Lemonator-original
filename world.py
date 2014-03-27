import sys

class World:
    def __init__(self, max_stands):
        self.max_stands = max_stands
        self.stands = set()
        self.world_x = 25
        self.world_y = 15

    def draw_map(self):
        for y in range(self.world_y):
            for x in range(self.world_x):
                for stand in self.stands:
                    if stand.stand_coords == (x,y):
                        sys.stdout.write('*')
                    else:
                        sys.stdout.write('.')
            print
        print