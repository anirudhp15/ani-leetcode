def contains_duplicate(nums):
    duplicates = {}
    for num in nums:
        if num in duplicates:
            return True
        duplicates[num] = True
    return False


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print(contains_duplicate(nums))
    nums2 = [1, 2, 3, 4, 5, 5]
    print(contains_duplicate(nums2))
