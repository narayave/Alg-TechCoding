
# Leetcode mock interview - https://leetcode.com/problems/kth-largest-element-in-a-stream/
# Passes 9 of 10 tests, large testcase is large. Time takes close to n*nlogn, so fails by exceeding time limit

# Submitte solution
import heapq as hp


class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.nums = [-i for i in nums]
        hp.heapify(self.nums)

        self.k = k

    def add(self, val: int) -> int:
        hp.heappush(self.nums, -1*val)
        nsmallest = hp.nsmallest(self.k, self.nums)
        # for i in nsmallest:
        #     hp.heappush(self.nums, i)

        print(nsmallest[-1]*-1)
        return nsmallest[-1]*-1


# Working solutions

class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.nums = nums
        hp.heapify(self.nums)

        self.k = k

    def add(self, val: int) -> int:
        hp.heappush(self.nums, val)

        # Only keep k tyhings in heap at all times
        while len(self.nums) > self.k:
            hp.heappop(self.nums)

        return self.nums[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
