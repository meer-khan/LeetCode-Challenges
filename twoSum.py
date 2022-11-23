def twoSum( nums , target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target: 
                return[i,j]
            else:
                continue



print(twoSum(nums = [3,3], target = 6))