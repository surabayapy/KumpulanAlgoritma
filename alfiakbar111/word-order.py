from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass
d = OrderedCounter(input() for _ in range(int(input())))
print(len(d))
print(*d.values())

# ex-input:
### 4
### bcdef
### abcdefg
### bcde
### bcdef