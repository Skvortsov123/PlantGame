import random

from PlantMng.Plant.Cell.Operators.Operators import *
from PlantMng.Plant.Cell.Operators.Conditions import *
import random

class DNA:
    def __init__(self, plant, amount_obj):
        #self.plant = plant
        if amount_obj % 2 == 0:
            amount_obj = amount_obj - 1
        self.amount_obj = amount_obj
        self.DNAList = self.create_random_DNA(amount_obj)

    def tick(self, cellList):
        copyCellList = list(cellList)       #tick from Cell tick(cell)
        for cell in copyCellList:
            self.DNA_grow_all(cell)

    def DNA_grow_all(self, cell):
        if cell.if_can_grow_left():
            if self.if_DNA_grow(self.get_DNAList()[0], cell):   #Left
                cell.growLeft()
        if cell.if_can_grow_up():
            if self.if_DNA_grow(self.get_DNAList()[1], cell):   # Up
                cell.growUp()
        if cell.if_can_grow_right():
            if self.if_DNA_grow(self.get_DNAList()[2], cell):  # Right
                cell.growRight()

    def if_DNA_grow(self, DNA, cell):
        result = DNA[0].condition(cell)
        for i in range(1, len(DNA)-1, 2):
            result = DNA[i].operate(result, DNA[i+1].condition(cell))
        return result

    def create_random_DNA(self, amount_obj):
        DNAList = []
        for _ in range(3):
            DNASubList = []
            DNASubList.append(self.get_random_Condition())
            for _ in range(int(amount_obj / 2)):
                DNASubList.append(self.get_random_Operators())
                DNASubList.append(self.get_random_Condition())
            DNAList.append(DNASubList)
        return DNAList

    def mutate_DNA(self, percentMutate):
        self.set_DNA(self.create_mutated_DNA(percentMutate))

    def create_mutated_DNA(self, percentMutate):  # min 0 -> 1 max
        randomDNAList = self.create_random_DNA(self.amount_obj)
        mutatedDNAList = []
        for side in range(len(randomDNAList)):
            mutatedDNAList.append([])
            for i in range(len(randomDNAList[side])):
                if random.random() < percentMutate:
                    mutatedDNAList[side].append(randomDNAList[side][i])
                else:
                    mutatedDNAList[side].append(self.get_DNAList()[side][i])
        return mutatedDNAList

    def set_DNA(self, DNAList):
        self.DNAList = DNAList
    def get_random_Condition(self):
        return random.choice(self.get_conditionList())()    #() call class contructor

    def get_random_Operators(self):
        return random.choice(self.get_operatorsList())()    #() call class contructor

    def get_conditionList(self):
        return [EnergyCondition, XCondition, YCondition, TickCondition, PlantTickCondition]

    def get_operatorsList(self):
        return [And, Or, Xor, Nand, Nor, Nxor]

    def get_DNAList(self):
        return self.DNAList

    def get_amount_obj(self):
        return self.amount_obj