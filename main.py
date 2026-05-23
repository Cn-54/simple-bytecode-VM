from VM import CPU

cpu = CPU()
cpu.run([
    1,10,0,0,
    1,5,0,1,
    2,0,1,2,
    -1,0,0,0
])

print(cpu.dumpDataMemory())