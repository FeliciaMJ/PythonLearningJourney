is_fat = True

state = "fat" if is_fat else "not fat"
print(state)

fat = True
fitness = ("skinny", "fat")[fat]
print("ali is ", fitness)

condition = True
print(2 if condition else 1/0)
print((1 / 0, 2)[condition])
