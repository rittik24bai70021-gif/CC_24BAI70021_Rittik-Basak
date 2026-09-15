def search_insert(nums, target):

    for i in range(len(nums)):

    
        if nums[i] == target:
            return i
        if nums[i] > target:
            return i
        
    return len(nums)


nums = [1, 3, 5, 6]
target = 7

result = search_insert(nums, target)
print("Insert Position:", result)