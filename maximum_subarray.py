from typing import List

def maxSubArr(nums: List[int]) -> int:
    sub_arr = [0] * len(nums)
    sub_arr[0] = nums[0]
    max_numb = sub_arr[0]

    for k in range(1, len(nums)):
        sub_arr[k] = max((sub_arr[k - 1] + nums[k]), nums[k])
        if sub_arr[k] > max_numb: max_numb = sub_arr[k]
        print(sub_arr)
        print(max_numb)
    return max_numb

print(maxSubArr([-4, 3, 2, -1, 10, -9, 2]))
#result should be: 14 
