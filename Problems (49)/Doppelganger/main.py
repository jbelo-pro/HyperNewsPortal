# the object_list has already been defined
from collections.abc import Hashable
# object_list = [1, 397, 27468, -95, 1309, 397, -539874, -240767, -95, 397]
object_list = [x for x in object_list if isinstance(x, Hashable)]
d = dict()
for h in object_list:
    d[h] = d.get(h, 0) + 1
s = 0
for v in d.values():
    if v > 1:
        s += v
print(s)
