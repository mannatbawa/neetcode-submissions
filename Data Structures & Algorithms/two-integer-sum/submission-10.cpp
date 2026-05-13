class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        //map [val][index]
        // i want to use find to get the value
        //at the end the goal is to get that index
        unordered_map<int,int> previous;
        //iterate through map and see if the complement exists
        for (int i = 0; i< nums.size(); i++){
            int difference = target-nums[i];
            // i = 0, difference = 7 - 3 = 4
            // 2nd iteration i = 1, difference 7 - 4 = 4
            if (previous.find(difference) != previous.end()){
                return {previous[difference], i};
            }
            //base case 
            //previous[3] = 0
            previous[nums[i]]=i;
            
        }
    }
};
