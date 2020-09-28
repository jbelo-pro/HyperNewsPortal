# create your dictionary here
from collections.abc import Hashable
objects_dict = dict()
for ob in objects:
    if isinstance(ob, Hashable):
        objects_dict[ob] = hash(ob)
