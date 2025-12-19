# Problem 5: Counting Bits
# LeetCode 338

class Solution:
    def countBits(self, n):
        """Count 1's in binary for each number 0 to n."""
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.countBits(2))  # Expected: [0,1,1]
    print(sol.countBits(5))  # Expected: [0,1,1,2,1,2]
