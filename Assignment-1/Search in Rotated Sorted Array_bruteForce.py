class Solution:
    def search(self, nums, target):
        for num in nums:
            if num == target:
                return True
        return False

nums = list(map(int, input("Enter the array elements: ").split()))
target = int(input("Enter the target: "))

obj = Solution()
result = obj.search(nums, target)

if result:
    print("Target found")
else:
    print("Target not found")