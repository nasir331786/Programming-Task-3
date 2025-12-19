# Problem 2: Count Number of Teams
# LeetCode 1395
# N soldiers standing in a line with unique ratings
# Form teams of 3 soldiers in ascending or descending order

class Solution:
    def numTeams(self, rating):
        """
        Count teams of 3 soldiers with ascending or descending ratings.
        
        For each middle element, count elements on left and right:
        - Smaller on left & larger on right = ascending
        - Larger on left & smaller on right = descending
        
        Time: O(n^2), Space: O(1)
        """
        count = 0
        n = len(rating)
        
        for j in range(1, n - 1):
            left_smaller = left_larger = 0
            right_smaller = right_larger = 0
            
            for i in range(j):
                if rating[i] < rating[j]:
                    left_smaller += 1
                elif rating[i] > rating[j]:
                    left_larger += 1
            
            for k in range(j + 1, n):
                if rating[k] > rating[j]:
                    right_larger += 1
                elif rating[k] < rating[j]:
                    right_smaller += 1
            
            count += left_smaller * right_larger + left_larger * right_smaller
        
        return count


if __name__ == "__main__":
    sol = Solution()
    print(sol.numTeams([2, 5, 3, 4, 1]))  # Expected: 3
    print(sol.numTeams([2, 1, 3]))        # Expected: 0
