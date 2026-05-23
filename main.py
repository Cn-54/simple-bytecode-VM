from VM import CPU
import sys


if __name__ == "__main__":
    numArgs = len(sys.argv)
    if len(sys.argv) < 2:
        print("Usage: python main.py <filename>")
        sys.exit(1)
    else:
        cpu = CPU()
        program = None
        filename = sys.argv[1]
        with open(filename, 'r') as file:
            program = [int(x) for x in file.read().replace("\n", "").split(",")]
        file.close()
        cpu.run(program)
        print(cpu.dumpDataMemory())