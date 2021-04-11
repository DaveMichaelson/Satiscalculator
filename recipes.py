from enum import Enum, auto

class Recipe:

    def __init__(self, input, output, time, machine):
        self.input = input
        self.output = output
        self.time = time
        self.machine = machine

    def __str__(self):
        return f"{self.input} - {self.machine} in {self.time}s > {self.output}"

class RecipeParseError(Exception):
    pass

def parse_recipe(line):
    line = line.strip('\n')

    class ParseState(Enum):
        NUMBER = 1
        NAME = 2
        TIME = 3
        MACHINE = 4

    number = None
    name = ""
    input = {}
    output = {}
    current_dir = input
    time = 0
    machine = ""
    pos = 0

    state = ParseState.NUMBER

    for token in line.split(" "):
        if token == "":
            pos += 1
            continue
        elif token in [",", "-"]:
            pos += len(token) + 1
            current_dir[name[1:]] = number
            name = ""
            number = None

            if token == ",":
                state = ParseState.NUMBER
            else:
                state = ParseState.TIME

            continue
        elif token == ">":
            pos += len(token) + 1
            machine = machine[1:]
            state = ParseState.NUMBER
            current_dir = output
            continue

        if state is ParseState.NUMBER:
            number = int(token)
            state = ParseState.NAME
        elif state is ParseState.NAME:
            name += " " + token
        elif state is ParseState.TIME:
            time = int(token)
            state = ParseState.MACHINE
        elif state is ParseState.MACHINE:
            machine += " " + token
        else:
            raise RecipeParseError()

        pos += len(token) + 1

    output[name[1:]] = number

    if not(input and output and time and machine):
        raise RecipeParseError()
    
    return Recipe(input, output, time, machine)
    

