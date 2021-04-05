"""
python附带一个模块，它包含许多容器数据类型，名字叫做collections。
包括：defaultdict
    counter
    deque
    namedtuple
    enum.Enum
"""


from collections import defaultdict

colors = (
    ("yasoob", "yellow"),
    ("ali", "blue"),
    ("arham", "green"),
    ("ali", "black"),
    ("yasoob", "red"),
    ("ahmed", "silver")
)

favourite_colors = defaultdict(list)
for name, color in colors:
    favourite_colors[name].append(color)

print(favourite_colors)
import json
print(json.dumps(favourite_colors))

# some_dict = {}
# some_dict["colors"]["favourite"] = "yellow"
# print(some_dict)

import collections
tree = lambda : collections.defaultdict(tree)
some_dict = tree()
some_dict["colors"]["favourite"] = "yellow"
print(json.dumps(some_dict))

from collections import Counter

favx = Counter(name for name, color in colors)
print(json.dumps(favx))

from collections import deque

# deque提供一个双端队列，可以从头部和尾部两端添加或删除元素。
d = deque()

d.append("1")
d.append("2")
d.append("3")
print(len(d))
print(d)

d = deque(range(5))
print(d)
print(d.popleft())
print(d)
print(d.pop())
print(d)
d.appendleft(99)
print(d)
d.extendleft([100, 101, 102])
print(d)

man = ("Ali", 30)
print(man[0])

from collections import namedtuple
Animal = namedtuple("dog", "name age type")
pretty = Animal(name="pretty", age=31, type="cat")
print(pretty)
print(pretty.name)
print(pretty[0])

print("hello world")

array = list(range(10))
print(array)