def two_sum(nums, target):
    complements = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in complements:
            return [complements[complement], i]
        complements[num] = i


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    print(two_sum(nums, target))
