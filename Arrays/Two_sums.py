def Two_sum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return (num_dict[complement], i)
        num_dict[num] = i
    return ()
def main():
    nums = [2, 7, 11, 15]   
    target = 9
    result = Two_sum(nums, target)
    print(result)  # Output: (0, 1) because nums[0] + nums[1] = 2 + 7 = 9
if __name__ == "__main__":    
     main()