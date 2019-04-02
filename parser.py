from mechanize import syntax


def check(line):
    words = line.split(" ")

    expected = None
    for word in words:
        synt = syntax.get(word, None)
        if not synt:
            print("word \"{}\" not in library".format(word))
            return False
        if expected:
            type_ = synt.get("type", None)
            if type_ not in expected:
                print("Error: expected: {}, got: {}".format(expected, type_))
                return False
        if synt:
            expected = synt["expected"]

    return True


def lookup(word):
    return syntax[word]["type"]

def parse(filename):
    inst = open(filename)

    all_true = True

    instructions_decomposed = []

    for line in inst:
        line = line.replace("\n", "")
        valid = check(line)
        print(valid)
        if not valid:
            return not all_true
        inst = {}
        words = line.split(" ")
        for word in words:
            type_ = lookup(word)
            inst[word] = type_
        instructions_decomposed.append(inst)

    return  instructions_decomposed
