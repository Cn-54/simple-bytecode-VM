simple bytecode VM written in python that follows a harvard architecture and programs written with numeric mneumonics
instructions consist of 4 "bytes" : OPCODE,A,B,C

 ISA
 
 -1 / halt /
 
 0  / NO-OP / 
 
 1  / SET   / sets DATA[C] to A / immidiete
 
 2  / LOAD  / DATA[A] = DATA[DATA[C]] /
 
 3  / STORE / DATA[DATA[C]] = DATA[A] /
 
 4  / ADD   / Adds data[A] and data[B] into data[C]
 
 5  / SUB   / subtracts data[A] and data[B] into data[C]
 
 6  / MUL   / multiplies data[A] and data[B] into data[C]
 
 7  / DIV   / divides data[A] and data[B] into data[C] / always rounds
 
 8  / MOD   / modulos data[A] and data[B] into data[C]
 
 9  / POW   / does data[A] to the power of data[B] into data[C]
 
 10 / JMP   / always jumps to C
 
 11 / JGT   / jumps to C if DATA[A] > DATA[B]
 
 12 / JLT   / jumps to C if DATA[A] < DATA[B]
 
 13 / JEQ   / jumps to C if DATA[A] = DATA[B]
