import copy


def detect_copy():
    obj = [[1, 2], [3, 4]]
    co = copying_machine(obj)
    if id(obj[0]) != id(co[0]):
        return "deep copy"
    else:
        return "shallow copy"