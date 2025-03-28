import random


class EnergyCondition:
    def __init__(self):
        self.value = random.random() * 500000
        self.operator = random.choice(["<", "==", ">"])

    def condition(self, cell):
        if self.operator == "<":
            return cell.get_energy() < self.value
        if self.operator == "==":
            return cell.get_energy() == self.value
        if self.operator == ">":
            return cell.get_energy() > self.value
        raise ValueError("No operator was chose")

class XCondition:
    def __init__(self):
        self.value = random.random() * 1000
        self.operator = random.choice(["<", "==", ">"])

    def condition(self, cell):
        if self.operator == "<":
            return cell.get_relative_x() < self.value
        if self.operator == "==":
            return cell.get_relative_x() == self.value
        if self.operator == ">":
            return cell.get_relative_x() > self.value
        raise ValueError("No operator was chose")

class YCondition:
    def __init__(self):
        self.value = random.random() * 100
        self.operator = random.choice(["<", "==", ">"])

    def condition(self, cell):
        if self.operator == "<":
            return cell.get_relative_y() < self.value
        if self.operator == "==":
            return cell.get_relative_y() == self.value
        if self.operator == ">":
            return cell.get_relative_y() > self.value
        raise ValueError("No operator was chose")

class TickCondition:
    def __init__(self):
        self.value = -1 #random.random() * 1000 #Disabled because plants make harakiri at the same time
        self.operator = random.choice(["<", "==", ">"])

    def condition(self, cell):
        if self.operator == "<":
            return cell.get_tickTimer() < self.value
        if self.operator == "==":
            return cell.get_tickTimer() == self.value
        if self.operator == ">":
            return cell.get_tickTimer() > self.value
        raise ValueError("No operator was chose")

class PlantTickCondition:
    def __init__(self):
        self.value = random.random() * 1000
        self.operator = random.choice(["<", "==", ">"])

    def condition(self, cell):
        if self.operator == "<":
            return cell.get_PlantTickTimer() < self.value
        if self.operator == "==":
            return cell.get_PlantTickTimer() == self.value
        if self.operator == ">":
            return cell.get_PlantTickTimer() > self.value
        raise ValueError("No operator was chose")