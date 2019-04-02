from parser import  parse
from mechanize import  semantics
from os import system

instructions = parse("script")

verbo = target = cmd = None

if instructions:
    for instruction in instructions:
        print(instruction)
        for word, type_ in instruction.items():
            if type_ == "verbo":
                verbo = word
                break
        for word, type_ in instruction.items():
            if type_ == "sostantivo":
                target = word
                break

        print(verbo, target)

        commands = semantics[verbo]
        for command in commands:
            print(command, target)
            if command["target"] == target:
                cmd = command["command"]
            break

        command_type = cmd["type"]
        command_inst = cmd["instruction"]

        if command_type == "system":
            system(command_inst)
        if command_type == "code":
            eval(command_inst)