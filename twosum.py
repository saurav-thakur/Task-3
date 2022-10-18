def two_sum(nums,target):
    d = {}

    for i in range(len(nums)):
        diff = target - nums[i]

        if diff in d:
            return [d[diff],i]

        d[nums[i]] = diff

    return "Not Found"

nums = [2,7,11,15]
target = 9
print(two_sum(nums,target))