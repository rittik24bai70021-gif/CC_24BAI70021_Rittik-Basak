class Solution:

    def containsNearbyDuplicate(self, nums, k):

        window = set()

        left = 0

        for right in range(len(nums)):

            if nums[right] in window:
                return True

            window.add(nums[right])

            if len(window) > k:
                window.remove(nums[left])
                left += 1

        return False

nums = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter k: "))

sol = Solution()
print(sol.containsNearbyDuplicate(nums, k))