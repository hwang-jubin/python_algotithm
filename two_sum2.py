def twoSum(nums, target):
    # O(nlogn)
    nums.sort()
    l = 0
    r = len(nums)-1
    # O(n)
    while l<r:
        if nums[l]+nums[r] > target:
            r = r-1
        elif nums[l]+nums[r] < target:
            l = l+1
        elif nums[l]+nums[r] == target:
            return True
    return False

print(twoSum(nums=[1,2,4,5], target = 9))