import random

# nums = [random.randint(1, 45) for _ in range(6)]
nums = set()

while len(nums) < 6:
    num = random.randint(1, 45)
    nums.add(num)

nums = list(nums)
nums.sort()
print(nums)