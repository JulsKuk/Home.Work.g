from collections import Counter
from functools import reduce

dict_1 = {'a': 1, 'b': 2, 'c': 3, 'z': 3}
dict_2 = {'z': 1, 'x': 9, 'c': 6, 'a': 5}


def max_dct(*dicts):
   return dict(reduce(lambda a, b: Counter(a) | Counter(b), dicts))
dict_3 =  (max_dct(dict_1, dict_2))
print(dict_3)
