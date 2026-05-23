# ISA
# -1 / halt /
# 0  / NO-OP / 
# 1  / LOAD / loads A into DATA[C] / immidiete
# 2  / ADD / Adds data[A] and data[B] into data[C]
# 3  / SUB / subtracts data[A] and data[B] into data[C]
# 4  / MUL / multiplies data[A] and data[B] into data[C]
# 5  / DIV / divides data[A] and data[B] into data[C] / always rounds
# 6  / MOD / modulos data[A] and data[B] into data[C]
# 7  / POW / does data[A] to the power of data[B] into data[C]


class memory:
    def __init__(self):
        self.CODE = [0]*255
        self.DATA = [0]*255
    
    def loadProgram(self,program):
        for i,byte in enumerate(program):
            self.CODE[i] = byte

class instruction:
    def __init__(self,opcode,a,b,C):
        self.OPCODE = opcode
        self.A = a
        self.B = b
        self.C = C

class CPU:
    def __init__(self):
        self.MEM = memory()
        self.PC = 0
        self.HALTED = False

    def fetch(self):
        ins = instruction(
            self.MEM.CODE[self.PC],
            self.MEM.CODE[self.PC+1],
            self.MEM.CODE[self.PC+2],
            self.MEM.CODE[self.PC+3],
        )
        self.PC += 4
        return ins

    def decodeExecute(self,INS):
        match INS.OPCODE:
            case -1: self.HALTED = True
            case 0: pass                                                            # NO-OP
            case 1: self.MEM.DATA[INS.C] = INS.A                                      # load
            case 2: self.MEM.DATA[INS.C] = self.MEM.DATA[INS.A]+self.MEM.DATA[INS.B]  # ADD
            case 3: self.MEM.DATA[INS.C] = self.MEM.DATA[INS.A]-self.MEM.DATA[INS.B]  # SUB
            case 4: self.MEM.DATA[INS.C] = self.MEM.DATA[INS.A]*self.MEM.DATA[INS.B]  # MUL
            case 5: self.MEM.DATA[INS.C] = self.MEM.DATA[INS.A]/self.MEM.DATA[INS.B]  # DIV
            case 6: self.MEM.DATA[INS.C] = self.MEM.DATA[INS.A]%self.MEM.DATA[INS.B]  # MOD
            case 6: self.MEM.DATA[INS.C] = self.MEM.DATA[INS.A]**self.MEM.DATA[INS.B] # POW
    
    def run(self,program):
        self.MEM.loadProgram(program)
        while not self.HALTED:
            ins = self.fetch()
            self.decodeExecute(ins)
    
    def dumpCodeMemory(self):
        return self.MEM.CODE
    def dumpDataMemory(self):
        return self.MEM.DATA

        