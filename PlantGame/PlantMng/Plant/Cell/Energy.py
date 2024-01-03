

class Energy:
    def __init__(self, startEnergy=30, maxEnergy=100, sunCost=20, hungerCost=-1, growCost=-1):
        self.maxEnergy = maxEnergy
        self.energy = startEnergy
        self.sunCost = sunCost
        self.hungerCost = hungerCost
        self.growCost = growCost

    def plus_energy(self, num):
        self.energy += num
        if self.energy > self.maxEnergy:
            self.energy = self.maxEnergy

    def get_energy(self):
        return self.energy

    def give_sunCost(self, coefficient=1):
        self.plus_energy(self.sunCost * coefficient)

    def give_hungerCost(self, coefficient=1):
        self.plus_energy(self.hungerCost * coefficient)

    def give_growCost(self, coefficient=1):
        self.plus_energy(self.growCost * coefficient)