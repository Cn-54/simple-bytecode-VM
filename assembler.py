



def assemble(program):
    output = []
    for i, x in enumerate(program):
        if isinstance(x,str):
            match x:
                case "HALT": 
                    output.append(-1)
                    output.append(0)
                    output.append(0)
                    output.append(0)
                case "SET": 
                    output.append(1)
                    output.append(int(program[i+1]))
                    output.append(0)
                    output.append(int(program[i+2]))
                case "LOAD": 
                    output.append(2)
                    output.append(int(program[i+1]))
                    output.append(0)
                    output.append(int(program[i+2]))
                case "STORE": 
                    output.append(3)
                    output.append(int(program[i+1]))
                    output.append(0)
                    output.append(int(program[i+2]))
                case "ADD": 
                    output.append(4)
                    output.append(int(program[i+1]))
                    output.append(int(program[i+2]))
                    output.append(int(program[i+3]))
    
    return output