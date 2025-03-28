

class Cell:
    def __init__(self, x, y, relative_x, relative_y, plant):
        self.x = x
        self.y = y
        self.plant = plant
        self.tickTimer = 0
        self.relative_x = relative_x
        self.relative_y = relative_y
        self.sunCoefficient = 1
        self.hungerCoefficient = 1
        self.growCoefficient = 1
        self.printName = "n"

    def tick(self):
        self.tick_tickTimer()

    def createCell(self, x, y, relative_x, relative_y, cellType):
        self.plant.createCell(x, y, relative_x, relative_y, cellType)

    def growLeft(self, cellType):
        self.createCell(self.x-1, self.y, self.relative_x-1, self.relative_y, cellType)

    def growUp(self, cellType):
        self.createCell(self.x, self.y+1, self.relative_x, self.relative_y+1, cellType)

    def growRight(self, cellType):
        self.createCell(self.x+1, self.y, self.relative_x+1, self.relative_y, cellType)

    def if_can_grow_left(self):
        return not self.plant.plantMng.if_cell_exists(self.get_x()-1, self.get_y())

    def if_can_grow_up(self):
        return not self.plant.plantMng.if_cell_exists(self.get_x(), self.get_y()+1)

    def if_can_grow_right(self):
        return not self.plant.plantMng.if_cell_exists(self.get_x()+1, self.get_y())

    def if_can_grow(self):
        return self.if_can_grow_left() or self.if_can_grow_up() or self.if_can_grow_right()

    def tick_tickTimer(self):
        self.tickTimer += 1

    def get_x(self):    #Absolute
        return self.x

    def get_y(self):    #Absolute
        return self.y

    def get_relative_x(self):
        return self.relative_x

    def get_relative_y(self):
        return self.relative_y

    def get_group(self):
        return self.plant.get_group()

    def get_energy(self):
        return self.plant.energy.get_energy()

    def get_tickTimer(self):
        return self.tickTimer

    def get_PlantTickTimer(self):
        return self.plant.get_tickTimer()

    def get_sunCoefficient(self):
        return self.sunCoefficient

    def get_hungerCoefficient(self):
        return self.hungerCoefficient

    def get_growCoefficient(self):
        return self.growCoefficient

    def get_printName(self):
        return self.printName

    def __str__(self):
        return f"Cell x{self.x} y{self.y} g{self.get_group()}"

class CellSun(Cell):
    def __init__(self, x, y, relative_x, relative_y, plant):
        super().__init__(x, y, relative_x, relative_y, plant)
        self.sunCoefficient = 2
        self.hungerCoefficient = 3
        self.growCoefficient = 4
        self.printName = "e"

    def __str__(self):
        return f"CellSun x{self.x} y{self.y} g{self.get_group()}"

class CellSeed(Cell):
    def __init__(self, x, y, relative_x, relative_y, plant):
        super().__init__(x, y, relative_x, relative_y, plant)
        self.sunCoefficient = 0
        self.hungerCoefficient = 5
        self.growCoefficient = 10
        self.printName = "s"    #Seed is active from start, make other ideas later (need to grow 50 rounds)


    def __str__(self):
        return f"CellSeed x{self.x} y{self.y} g{self.get_group()}"