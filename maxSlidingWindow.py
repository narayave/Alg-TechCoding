
# Leeetcode - https://leetcode.com/problems/sliding-window-maximum/

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # O(n) solution, as it's one pass

        if k == 0:
            return []

        if k == 1:
            return nums

        if k > len(nums):
            return max(nums)

        res = []
        n = len(nums)
        q = deque()     # We need this to be able to pop things off left and right

        # Basically find the maxs within k first
        for i in range(0,k):
            while len(q) != 0:
                if nums[i] > nums[q[-1]]:
                    q.pop()
                else:
                    break
            q.append(i)

        # Continue what we were doing before, but we need to start generating the final result
        for i in range(k, n):
            res.append(nums[q[0]])

            # When we are moving out of the window, pop the first item out
            if q[0] < i - k+1:
                q.popleft()

            while len(q) != 0:
                if nums[i] > nums[q[-1]]:
                    q.pop()
                else:
                    break
            q.append(i)

        res.append(nums[q[0]])

        return res