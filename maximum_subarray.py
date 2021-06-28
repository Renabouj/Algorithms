from typing import List

def maxSubArr(nums: List[int]) -> int:
    sub_arr = [0] * len(nums)
    sub_arr[0] = nums[0]
    max_numb = sub_arr[0]

    for k in range(1, len(nums)):
        sub_arr[k] = max((sub_arr[k - 1] + nums[k]), nums[k])
        if sub_arr[k] > max_numb: max_numb = sub_arr[k]
    return max_numb

def main():
    """
    >>> maxSubArr([-4, 3, 2, -1, 10, -9, 2])
    14
    """

if __name__ == '__main__':
    import doctest
    doctest.testmod()
