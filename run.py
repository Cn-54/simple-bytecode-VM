from VM import CPU
from assembler import assemble
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <filename>")
        sys.exit(1)
    else:
        cpu = CPU()
        program = None
        filename = sys.argv[1]
        with open(filename, 'r') as file:
            if filename.endswith(".M"):
                program = [int(x) for x in file.read().replace("\n", "").split(",")] # formates the program from a machine code file
            elif filename.endswith(".A"):
                program = file.read().replace("\n", " ").split(" ") # formats the program to be passed to the assembler
                program = assemble(program)
        file.close()
        cpu.run(program)
        print(cpu.dumpDataMemory())