class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> differences;
        vector<int> solution;
        for (int i = 0; i < nums.size(); i++){
            int difference = target - nums[i];
            //in the case that you found it
            if (differences.find(difference) != differences.end())
            {
                solution.push_back(differences[difference]);

                solution.push_back(i);
                
                return solution;
            }
            differences[nums[i]] = i;
        
        }
        
    }
};
