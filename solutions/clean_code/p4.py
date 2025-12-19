# Problem 4: Number of Steps to Reduce a Number to Zero
# LeetCode 1342

class Solution:
    def numberOfSteps(self, num):
        """Count steps to reduce num to zero."""
        steps = 0
        while num > 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            steps += 1
        return steps


if __name__ == "__main__":
    sol = Solution()
    print(sol.numberOfSteps(14))  # Expected: 6
    print(sol.numberOfSteps(8))   # Expected: 4
