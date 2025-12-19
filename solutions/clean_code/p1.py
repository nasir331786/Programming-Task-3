# Problem 1: Maximum Product of Two Elements in an Array
# LeetCode 1464
# Given array of integers nums, choose two different indices i and j
# Return maximum value of (nums[i]-1)*(nums[j]-1)

class Solution:
    def maxProduct(self, nums):
        """
        Find the maximum product of (nums[i]-1)*(nums[j]-1) for i != j
        
        Approach: Find the two largest elements in the array
        Time Complexity: O(n) for single pass, or O(n log n) if sorting
        Space Complexity: O(1)
        """
        # Get two largest numbers
        max1 = max2 = float('-inf')
        
        for num in nums:
            if num > max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num
        
        return (max1 - 1) * (max2 - 1)


# Alternative approach: Sort and get the two largest
class SolutionAlt:
    def maxProduct(self, nums):
        nums.sort(reverse=True)
        return (nums[0] - 1) * (nums[1] - 1)


if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    print(sol.maxProduct([10, 2, 5, 2]))  # Expected: 36 (10-1) * (5-1) = 9 * 4 = 36
    print(sol.maxProduct([1, 5, 4, 5]))   # Expected: 16 (5-1) * (5-1) = 4 * 4 = 16
    print(sol.maxProduct([3, 7]))         # Expected: 12 (7-1) * (3-1) = 6 * 2 = 12
