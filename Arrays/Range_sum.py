# Prefix Sum for Range Sum Query
# Problem
# Given an array, answer multiple sum queries quickly.
# nums = [2, 4, 1, 3, 6]
# Find sum from index 1 to 3.
# 4 + 1 + 3 = 8

def Range_Sum(nums, left, right):
    pre_sum = prefix_sum(nums)
    return pre_sum[right+1] - pre_sum[left]

def prefix_sum(nums):
    sums=[0]
    for num in nums:
        sums.append(sums[-1] + num)
    return sums

def main():
    nums = [2, 4, 1, 3, 6]  
    result = Range_Sum(nums, 1,3)
    print(result)  

if __name__ == "__main__":    
     main()