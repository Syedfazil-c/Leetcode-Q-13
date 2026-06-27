Missing Number

Problem

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Approach

Use the XOR (^) operator.

- Initialize result with the length of the array.
- Traverse the array using its index.
- XOR the current result with both the index and the element at that index.
- Since identical numbers cancel each other out using XOR, only the missing number remains.

Complexity

Time Complexity: O(n)

Space Complexity: O(1)

Key Insight

XOR has two important properties:

a ^ a = 0

a ^ 0 = a

By XORing all indices and all array elements together, every matching number cancels out. The only value left is the missing number.

Example

Input:

nums = [3,0,1]

Output:

2

Explanation:

Expected numbers: 0, 1, 2, 3

Array contains: 3, 0, 1

Missing number: 2

Input:

nums = [1,3,2,0]

Output:

4

Explanation:

Expected numbers: 0, 1, 2, 3, 4

Array contains: 0, 1, 2, 3

Missing number: 4

Code

def missingNumber(nums):

    result = len(nums)

    for i in range(len(nums)):
    
        result ^= i ^ nums[i]

    return result

