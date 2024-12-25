def bubble(nums):
    n = len(nums)

    for i in range(0, n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    print(nums)

nums = input().split()
nums = [int(nums[k]) for k in range(len(nums))]
bubble(nums)