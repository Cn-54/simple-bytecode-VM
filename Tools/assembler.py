import sys


def formatProgram(program):
    output = []
    for line in program.splitlines():
        line = line.split(";")[0]
        line = line.strip()
        if not line:
            continue
        output.extend(line.split())
    return output

def assemble(program):
    program = formatProgram(program)
    output = []
    error = False
    i = 0
    instruction_num = 0

    while i < len(program):
        x = program[i]

        if not isinstance(x, str) or x.strip() == "":
            i += 1
            continue

        match x.upper():
            case "HALT":
                output.extend([-1, 0, 0, 0])
                i += 1
            case "NOP":
                output.extend([0, 0, 0, 0])
                i += 1
            case "SET":
                output.extend([1, int(program[i+2]), 0, int(program[i+1])])
                i += 3
            case "LOAD":
                output.extend([2, int(program[i+1]), 0, int(program[i+2])])
                i += 3
            case "STORE":
                output.extend([3, int(program[i+1]), 0, int(program[i+2])])
                i += 3
            case "ADD":
                output.extend([4, int(program[i+1]), int(program[i+2]), int(program[i+3])])
                i += 4
            case "SUB":
                output.extend([5, int(program[i+1]), int(program[i+2]), int(program[i+3])])
                i += 4
            case "MUL":
                output.extend([6, int(program[i+1]), int(program[i+2]), int(program[i+3])])
                i += 4
            case "DIV":
                output.extend([7, int(program[i+1]), int(program[i+2]), int(program[i+3])])
                i += 4
            case "MOD":
                output.extend([8, int(program[i+1]), int(program[i+2]), int(program[i+3])])
                i += 4
            case "POW":
                output.extend([9, int(program[i+1]), int(program[i+2]), int(program[i+3])])
                i += 4
            case "JUMP":
                output.extend([10, 0, 0, int(program[i+1])])
                i += 2
            case "JGT":
                output.extend([11, int(program[i+1]), int(program[i+2]), int(program[i+3])])
                i += 4
            case "JLT":
                output.extend([12, int(program[i+1]), int(program[i+2]), int(program[i+3])])
                i += 4
            case "JEQ":
                output.extend([13, int(program[i+1]), int(program[i+2]), int(program[i+3])])
                i += 4
            case "OUT":
                output.extend([14, int(program[i+1]),0,0])
                i += 2
            case "PUT":
                output.extend([15, int(program[i+1]),0,0])
                i += 2
            case "INP":
                output.extend([16, int(program[i+1]),0,0])
                i += 2
            case "ONL":
                output.extend([17,0,0,0])
                i += 1
            case "PUTI":
                output.extend([18, int(program[i+1]),0,0])
                i += 2
            case "OUTI":
                output.extend([19, int(program[i+1]),0,0])
                i += 2
            case "INPI":
                output.extend([20, int(program[i+1]),0,0])
                i += 2
            case _:
                print(f"[Assembler]: instruction {instruction_num} : Unknown opcode: {x}")
                error = True
                i += 1
                

        instruction_num += 1

    if error:
        sys.exit(1)

    return output


if __name__ == "__main__":
    filename = sys.argv[1]
    program = []
    with open(filename, 'r') as file:
        if filename.endswith(".A"):
            program = file.read()
            program = assemble(program)
        else:
            print("wrong file type passed")
    print(program)