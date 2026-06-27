nums = [1, 3, 0]
def missingNumber(nums):
    result= len(nums)
    for i in range(len(nums)):
        result = result ^ i ^ nums[i]
    return result
print(missingNumber(nums))
