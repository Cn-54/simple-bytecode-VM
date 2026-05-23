# ISA
# -1 / halt /
# 0  / NO-OP / 
# 1  / SET   / sets DATA[C] to A / immidiete
# 2  / LOAD  / DATA[A] = DATA[DATA[C]] /
# 3  / STORE / DATA[DATA[C]] = DATA[A] /
# 4  / ADD   / Adds data[A] and data[B] into data[C]
# 5  / SUB   / subtracts data[A] and data[B] into data[C]
# 6  / MUL   / multiplies data[A] and data[B] into data[C]
# 7  / DIV   / divides data[A] and data[B] into data[C] / always rounds
# 8  / MOD   / modulos data[A] and data[B] into data[C]
# 9  / POW   / does data[A] to the power of data[B] into data[C]
# 10 / JMP   / always jumps to C
# 11 / JGT   / jumps to C if DATA[A] > DATA[B]
# 12 / JLT   / jumps to C if DATA[A] < DATA[B]
# 13 / JEQ   / jumps to C if DATA[A] = DATA[B]




class Memory:
    # initialise the Memory of the Cpu with 2 arrays of size 255
    def __init__(self):
        self.CODE = [0]*255
        self.DATA = [0]*255
    
    # loads a given program into the cpu memory
    def loadProgram(self,program):
        for i,byte in enumerate(program):
            self.CODE[i] = byte


class Instruction:
    # initailises each operand of the instruction
    def __init__(self,opcode,a,b,C):
        self.OPCODE = opcode
        self.A = a
        self.B = b
        self.C = C

class CPU:
    # initialises the cpu memory, the program counter and its halted flag
    def __init__(self):
        self.MEM = Memory()
        self.PC = 0
        self.HALTED = False

    # fetched 4 bytes from memory and increments the program counter
    def fetch(self):
        ins = Instruction(
            self.MEM.CODE[self.PC],
            self.MEM.CODE[self.PC+1],
            self.MEM.CODE[self.PC+2],
            self.MEM.CODE[self.PC+3],
        )
        self.PC += 4
        return ins

    # takes the current instruction and decodes it before executing it
    def decodeExecute(self,INS):
        match INS.OPCODE:
            case -1: self.HALTED = True                                               # Halt
            case 0: pass                                                              # NO-OP
            case 1: self.MEM.DATA[INS.C] = INS.A                                      # SET
            case 2: self.MEM.DATA[INS.A] = self.MEM.DATA[self.MEM.DATA[INS.C]]        # LOAD
            case 3: self.MEM.DATA[self.MEM.DATA[INS.C]] = self.MEM.DATA[INS.A]        # STORE
            case 4: self.MEM.DATA[INS.C] = self.MEM.DATA[INS.A]+self.MEM.DATA[INS.B]  # ADD
            case 5: self.MEM.DATA[INS.C] = self.MEM.DATA[INS.A]-self.MEM.DATA[INS.B]  # SUB
            case 6: self.MEM.DATA[INS.C] = self.MEM.DATA[INS.A]*self.MEM.DATA[INS.B]  # MUL
            case 7: self.MEM.DATA[INS.C] = self.MEM.DATA[INS.A]//self.MEM.DATA[INS.B] # DIV
            case 8: self.MEM.DATA[INS.C] = self.MEM.DATA[INS.A]%self.MEM.DATA[INS.B]  # MOD
            case 9: self.MEM.DATA[INS.C] = self.MEM.DATA[INS.A]**self.MEM.DATA[INS.B] # POW
            case 10: self.PC = INS.C * 4                                              # JMP
            case 11:                                                                  # JGT
                if self.MEM.DATA[INS.A] > self.MEM.DATA[INS.B]:                       #
                    self.PC = INS.C * 4                                               #
            case 12:                                                                  # JLT
                if self.MEM.DATA[INS.A] < self.MEM.DATA[INS.B]:                       #
                    self.PC = INS.C * 4                                               #
            case 13:                                                                  # JEQ
                if self.MEM.DATA[INS.A] == self.MEM.DATA[INS.B]:                      #
                    self.PC = INS.C * 4                                               #


    # loads the memory of the cpu then runs the program until it halts
    def run(self,program):
        self.MEM.loadProgram(program)
        while not self.HALTED:
            ins = self.fetch()
            self.decodeExecute(ins)
    
    # returns th full code memory
    def dumpCodeMemory(self):
        return self.MEM.CODE
    #returns the full data memory
    def dumpDataMemory(self):
        return self.MEM.DATA

        