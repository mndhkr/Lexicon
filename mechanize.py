from typing import Dict

library = open("library", "r")

lines = library.readlines()

syntax: Dict[str, Dict[str, str]] = {}

for line in lines:
    line = line.replace("\n", "")
    split = line.split(":")
    syntax[split[1]] = {"type": split[0], "expected": split[2].split("|")}

print(syntax)




instructions = open("instructions")

semantics = {}

while(True):
    line = instructions.readline().replace("\n", "")
    if not line:
        break
    if line.startswith("verbo"):
        verbo = line.split(":")[1]
        semantics[verbo] = []
        counter = 0
        while(True):
            line = instructions.readline().replace("\n", "")
            if len(line) <3:
                break
            semantics[verbo].append({})
            if line.startswith("target"):
                target = line.split(":")[1]
                semantics[verbo][counter]["target"] = target
            line = instructions.readline().replace("\n", "")
            if line.startswith("command"):
                split = line.split(":")
                command = {"type":split[1], "instruction":split[2]}
                semantics[verbo][counter]["command"] = command
            counter += 1


print(semantics)

