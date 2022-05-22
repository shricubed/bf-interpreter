import sys

def readfile(fname):
    p = ""
    with open(fname, 'r') as f:
        p = f.read()
        interpret(p)


def interpret(parsed):
    memory = [0]
    pointer, bpoint = 0, 0
    parsed = ''.join(filter(lambda x: x in ['.', ',', '[', ']', '<', '>', '+', '-'], parsed))
    n = len(parsed)
    loops = handleloop(parsed)

    while bpoint < n:
        match parsed[bpoint]:
            case '>':
                if (pointer == len(memory) - 1):
                    memory.append(0)
                pointer += 1
            case '<':
                pointer = max(0, pointer - 1)
            case '+':
                memory[pointer] = min(memory[pointer] + 1, 255)
            case '-':
                memory[pointer] = memory[pointer] - 1 if memory[pointer] > 0 else 255
            case '[':
                if memory[pointer] == 0:
                    bpoint = loops[bpoint]
            case ']':
                if memory[pointer] != 0:
                    bpoint = loops[bpoint]
            case ',':
                memory[pointer] = int(input("input:"))
            case '.':
                print(chr(memory[pointer]), end='')
        bpoint += 1
            
def handleloop(code):
    temp_bracestack, bracemap = [], {}

    for position, command in enumerate(code):
        if command == "[": temp_bracestack.append(position)
        if command == "]":
            start = temp_bracestack.pop()
            bracemap[start] = position
            bracemap[position] = start
    return bracemap

readfile(sys.argv[1])



