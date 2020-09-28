class NegativeSumError(Exception):
    pass

def sum_with_exceptions(a, b):
    if a + b < 0:
        raise NegativeSumError()
    else:
        return a + b