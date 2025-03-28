

class And:
    def operate(self, condition1, condition2):
        if condition1 and condition2:
            return 1
        else:
            return 0


class Or:
    def operate(self, condition1, condition2):
        if condition1 or condition2:
            return 1
        else:
            return 0

class Xor:
    def operate(self, condition1, condition2):
        if condition1 ^ condition2:
            return 1
        else:
            return 0

class Nand:
    def operate(self, condition1, condition2):
        if not (condition1 and condition2):
            return 1
        else:
            return 0

class Nor:
    def operate(self, condition1, condition2):
        if not (condition1 or condition2):
            return 1
        else:
            return 0

class Nxor:
    def operate(self, condition1, condition2):
        if not (condition1 ^ condition2):
            return 1
        else:
            return 0
