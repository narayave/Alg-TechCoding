class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        
        int i = 0;  // Back pointer
        int j = 0;  // Front pointer
        int count = 1;
        
        if(nums.size() == 0) {
            return 0;
        }
        
        while (j != nums.size()) {
            
            if(nums[i]==nums[j]) {
                j += 1;
            } else {
                i += 1;
                nums[i] = nums[j];
                count += 1;
            }
        }
    
        return count;
    }
};