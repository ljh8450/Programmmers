def solution(nums):
    n = len(nums)
    n = n//2

    snums = set(nums)
    nums = list(snums)

    if len(nums) < n:
        return len(nums)
    else:
        return n