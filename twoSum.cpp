class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        map<int, int> mapper;
        vector<int> res;
        int check;

        for(int i=0; i < nums.size(); i++) {
            check = target - nums[i];
            
            if(mapper.find(check) != mapper.end()){
                res.push_back(mapper[check]);
                res.push_back(i);         
                break;
            }
            mapper[nums[i]] = i;
        }
        return res;
        
    }
};