def assemble(program):
    output = []
    for i, x in enumerate(program):
        if isinstance(x,str):
            match x.upper():
                case "HALT": 
                    output.extend([-1,0,0,0])
                case "SET": 
                    output.extend([1, int(program[i+1]), 0, int(program[i+2])])
                case "LOAD": 
                    output.extend([2, int(program[i+1]), 0, int(program[i+2])])
                case "STORE": 
                    output.extend([3, int(program[i+1]), 0, int(program[i+2])])
                case "ADD": 
                    output.extend([4, int(program[i+1]), int(program[i+2]), int(program[i+3])])
                case "SUB": 
                    output.extend([5, int(program[i+1]), int(program[i+2]), int(program[i+3])])
                case "MUL": 
                    output.extend([6, int(program[i+1]), int(program[i+2]), int(program[i+3])])
                case "DIV": 
                    output.extend([7, int(program[i+1]), int(program[i+2]), int(program[i+3])])
                case "MOD": 
                    output.extend([8, int(program[i+1]), int(program[i+2]), int(program[i+3])])
                case "POW": 
                    output.extend([9, int(program[i+1]), int(program[i+2]), int(program[i+3])])
                case "JUMP": 
                    output.extend([10, 0, 0, int(program[i+1])])
                case "JGT": 
                    output.extend([11, int(program[i+1]), int(program[i+2]), int(program[i+3])])
                case "JLT": 
                    output.extend([12, int(program[i+1]), int(program[i+2]), int(program[i+3])])
                case "JEQ": 
                    output.extend([13, int(program[i+1]), int(program[i+2]), int(program[i+3])])
    return output