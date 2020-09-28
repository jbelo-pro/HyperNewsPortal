import copy


def solve(obj):
    dc = copy.deepcopy(obj)
    if id(obj) != id(dc):
        return True
    else:
        return False