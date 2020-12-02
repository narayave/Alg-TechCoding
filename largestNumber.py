class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        
        result = ""
        count = len(nums)
        
        if count == 1:
            return nums
        
        part_1 = self.largestNumber(nums[:count/2])
        part_2 = self.largestNumber(nums[count/2:])
        
        psize_1 = len(part_1)
        psize_2 = len(part_2)
        print 'Part 1 size - ', psize_1
        print 'Part 2 size - ', psize_2
        
        # Combining
        p1 = p2 = 0
        tmp_order = []
        while p1 != psize_1 and p2 != psize_1:
            
            print tmp_order
            print p1, part_1[p1]
            print p2, part_2[p2]

            tmp_p1 = tmp_p2 = 0
            tmp1 = map(int, str(part_1[p1]))
            tmp2 = map(int, str(part_2[p2]))
            print tmp1, tmp2
            while tmp_p1 < len(tmp1) and tmp_p2 < len(tmp2):
                print 'Temps - ', tmp1[tmp_p1], tmp2[tmp_p2]
                if tmp1[tmp_p1] > tmp2[tmp_p2]:
                    tmp_order.append(tmp1[0:])
                    p1 += 1
                    break
                elif tmp2[tmp_p2] > tmp1[tmp_p1]:
                    tmp_order.append(tmp2[0:])
                    p2 += 1
                    break                    
                else:
                    # Both equal
                    # Update pointers
                    if tmp_p1 + 1 < len(tmp1):
                        tmp_p1 += 1
                    if tmp_p1 + 1 < len(tmp2):
                        tmp_p2 += 1
                    
            print 'Parts - ', part_1, part_2
            print 'tmp_order - ', tmp_order
            if p1 != psize_1:
                tmp_order = tmp_order[0][0:] + part_1[p1:]
            if p2 != psize_2:
                tmp_order = tmp_order[0][0:] + part_2[p2:]
        print tmp_order
        
        # List should hold 
        result = ''.join(str(x) for x in tmp_order)
        print result
        return result
