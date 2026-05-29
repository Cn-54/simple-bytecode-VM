import sys

def disassemble(program):
    output = []
    i = 0
    while i < len(program):
        x = program[i]
        match x:
            case -1:
                output.append("HALT")
                i += 4
            case 0:
                output.append("NOP")
                i += 4
            case 1:
                output.append(f"SET {program[i+1]} {program[i+3]}")
                i += 4
            case 2:
                output.append(f"LOAD {program[i+1]} {program[i+3]}")
                i += 4
            case 3:
                output.append(f"STORE {program[i+1]} {program[i+3]}")
                i += 4
            case 4:
                output.append(f"ADD {program[i+1]} {program[i+2]} {program[i+3]}")
                i += 4
            case 5:
                output.append(f"SUB {program[i+1]} {program[i+2]} {program[i+3]}")
                i += 4
            case 6:
                output.append(f"MUL {program[i+1]} {program[i+2]} {program[i+3]}")
                i += 4
            case 7:
                output.append(f"DIV {program[i+1]} {program[i+2]} {program[i+3]}")
                i += 4
            case 8:
                output.append(f"MOD {program[i+1]} {program[i+2]} {program[i+3]}")
                i += 4
            case 9:
                output.append(f"POW {program[i+1]} {program[i+2]} {program[i+3]}")
                i += 4
            case 10:
                output.append(f"JUMP {program[i+3]}")
                i += 4
            case 11:
                output.append(f"JGT {program[i+1]} {program[i+2]} {program[i+3]}")
                i += 4
            case 12:
                output.append(f"JLT {program[i+1]} {program[i+2]} {program[i+3]}")
                i += 4
            case 13:
                output.append(f"JEQ {program[i+1]} {program[i+2]} {program[i+3]}")
                i += 4
            case 14:
                output.append(f"OUT {program[i+1]}")
                i += 4
            case 15:
                output.append(f"PUT {program[i+1]}")
                i += 4
            case 16:
                output.append(f"INP {program[i+1]}")
                i += 4
            case 17:
                output.append("ONL")
                i += 4
            case 18:
                output.append(f"PUTI {program[i+1]}")
                i += 4
            case 19:
                output.append(f"OUTI {program[i+1]}")
                i += 4
            case 20:
                output.append(f"INPI {program[i+1]}")
                i += 4
            case _:
                output.append(f"UNKNOWN {x}")
                i += 4
    return output


if __name__ == "__main__":
    filename = sys.argv[1]
    program = []
    with open(filename, 'r') as file:
        if filename.endswith(".M"):
            program = [int(x) for x in file.read().replace("\n", "").split(",")] # formates the program from a machine code file
            program = disassemble(program)
        else:
            print("wrong file type passed")
    print(program)