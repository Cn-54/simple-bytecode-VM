# Simple Bytecode VM

a simple byte code VM implementation in python.
has a custom isa with numeric instructions and a Harvard architecture.
programs can be written in bytecode or assembly.

## Architecture
 - consists of separated memory for code and data each 255 in size
 - fixed width instructions | 4 values per instruction | [OPCODE,A,B,C]
 - Harvard architecture preventing programming from modifying their own code

## ISA

| Opcode | Mnemonic | Operation |
|--------|----------|-----------|
| -1 | HALT | Stop execution |
| 0 | NOP | No operation |
| 1 | SET | DATA[C] = A (immediate) |
| 2 | LOAD | DATA[A] = DATA[DATA[C]] |
| 3 | STORE | DATA[DATA[C]] = DATA[A] |
| 4 | ADD | DATA[C] = DATA[A] + DATA[B] |
| 5 | SUB | DATA[C] = DATA[A] - DATA[B] |
| 6 | MUL | DATA[C] = DATA[A] * DATA[B] |
| 7 | DIV | DATA[C] = DATA[A] // DATA[B] (always rounds down) |
| 8 | MOD | DATA[C] = DATA[A] % DATA[B] |
| 9 | POW | DATA[C] = DATA[A] ** DATA[B] |
| 10 | JMP | PC = C |
| 11 | JGT | if DATA[A] > DATA[B]: PC = C |
| 12 | JLT | if DATA[A] < DATA[B]: PC = C |
| 13 | JEQ | if DATA[A] == DATA[B]: PC = C |
| 14 | OUT | print DATA[A] as a number |
| 15 | PUT | print DATA[A] as ASCII character (no newline) |
| 16 | INP | prompt user for input, store in DATA[A] |
| 17 | ONL | print a newline |
| 18 | PUTI | print DATA[DATA[A]] as ASCII character (no newline) |
| 19 | OUTI | print DATA[DATA[A]] as a number |
| 20 | INPI | prompt user for input, store in DATA[DATA[A]] |


## Usage
 
```bash
python main.py <file>
```
 
Two file formats are supported:
 
| Extension | Format |

| `.M` | Raw bytecode - comma separated integers |

| `.A` | Assembly - one instruction per line |

## Examples
 
### Bytecode (.M)
```
1,10,0,0,
1,5,0,1,
4,0,1,2,
-1,0,0,0
```
 
### Assembly (.A)
```
SET 10 0
SET 5 1
ADD 0 1 2
HALT
```
Both programs load 10 into DATA[0], 5 into DATA[1], add them and store the result in DATA[2].

## Project Structure
 
```
├── VM.py          # Memory, Instruction and CPU classes
├── assembler.py   # Assembles .A files into bytecode
└── main.py        # CLI entry point
```
