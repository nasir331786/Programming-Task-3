# Problem 3: Number of Students Doing Homework at a Given Time
# LeetCode 1450

class Solution:
    def busyStudent(self, startTime, endTime, queryTime):
        """Count students doing homework at queryTime."""
        count = 0
        for start, end in zip(startTime, endTime):
            if start <= queryTime <= end:
                count += 1
        return count


if __name__ == "__main__":
    sol = Solution()
    print(sol.busyStudent([1, 2, 3], [3, 2, 7], 4))  # Expected: 1
    print(sol.busyStudent([4], [4], 4))              # Expected: 1
