from functools import reduce

nums = [13, 22, 34, 42]

product = reduce(lambda x, y: x * y, nums)

print(product)
