import random
import uuid

from PlantMng.Plant.Cell.Operators.Operators import *
from PlantMng.Plant.Cell.Operators.Conditions import *
import random

class DNA:
    def __init__(self, plant):
        #self.plant = plant #When saves it makes Ram eater
        self.lifeTime = None
        self.generate_random_lifeTime()     #Do random lifeTime changes plants variations? Does it exists most optimal lifeTime which we can just be set by default?
        self.dnaLength = None
        self.generate_random_dnaLength()    #Do random DNA length changes plants variations? Does it exists most optimal length which we can set by default?
        self.uuid = None
        self.generate_new_uuid()
        self.DNAList = self.create_random_DNA(self.get_dnaLength())

    def tick(self, cellList):
        copyCellList = list(cellList)       #tick from Cell tick(cell)
        for cell in copyCellList:
            self.DNA_grow_all(cell)

    def DNA_grow_all(self, cell):
        cellType = "Normal" #Normal Sun Seed
        if self.if_DNA(self.get_DNAList()[3], cell):    #If Normal
            cellType = "Normal"
        elif self.if_DNA(self.get_DNAList()[4], cell):  #If Sun
            cellType = "Sun"
        else:   #If Seed
            cellType = "Seed"
        if cell.if_can_grow_left():
            if self.if_DNA(self.get_DNAList()[0], cell):   #Left
                cell.growLeft(cellType)
        if cell.if_can_grow_up():
            if self.if_DNA(self.get_DNAList()[1], cell):   # Up
                cell.growUp(cellType)
        if cell.if_can_grow_right():
            if self.if_DNA(self.get_DNAList()[2], cell):  # Right
                cell.growRight(cellType)

    def if_DNA(self, DNA, cell):
        result = DNA[0].condition(cell)
        for i in range(1, len(DNA)-1, 2):
            result = DNA[i].operate(result, DNA[i+1].condition(cell))
        return result

    def create_random_DNA(self, dnaLength):
        DNAList = []
        for _ in range(5):  #left, up, right, normal, sun
            DNASubList = []
            DNASubList.append(self.get_random_Condition())
            for _ in range(int(dnaLength / 2)):
                DNASubList.append(self.get_random_Operators())
                DNASubList.append(self.get_random_Condition())
            DNAList.append(DNASubList)
        return DNAList

    def mutate_DNA(self, percentMutate):
        self.set_DNAList(self.create_mutated_DNA(percentMutate))
        self.mutate_lifeTime(0.01)
        self.generate_new_uuid()

    def create_mutated_DNA(self, percentMutate):  # min 0 -> 1 max  #maybe rename the arg to "mutatorIndex"
        randomDNAList = self.create_random_DNA(self.get_dnaLength())
        mutatedDNAList = []
        for side in range(len(randomDNAList)):
            mutatedDNAList.append([])
            for i in range(len(randomDNAList[side])):
                if random.random() < percentMutate:
                    mutatedDNAList[side].append(randomDNAList[side][i])
                else:
                    mutatedDNAList[side].append(self.get_DNAList()[side][i])
        return mutatedDNAList

    def generate_new_uuid(self):
        self.uuid = uuid.uuid1()

    def generate_random_dnaLength(self):    #Hard to handle, may cause crashes
        self.dnaLength = int(random.random() * 100)

    def generate_random_lifeTime(self):
        self.lifeTime = int(random.random() * 240)

    def mutate_lifeTime(self, mutatorIndex):    #0-1
        if random.random() > mutatorIndex:
            self.generate_random_lifeTime()

    def set_DNAList(self, DNAList):
        self.DNAList = DNAList

    def set_dnaLength(self, length):
        self.dnaLength = length

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

    def get_uuid(self):
        return self.uuid

    def get_dnaLength(self):
        return self.dnaLength

    def get_lifeTime(self):
        return self.lifeTime