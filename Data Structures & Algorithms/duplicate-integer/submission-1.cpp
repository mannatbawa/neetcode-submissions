class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        // int size = nums.size();
        unordered_set<int> singles;
        for (int i = 0; i < nums.size(); i++)
        {
            int templength = singles.size();
            singles.insert(nums[i]);
            int newlength = singles.size(); 
            if (templength == newlength){
                return true;
            }
        }
        return false;
    }
};