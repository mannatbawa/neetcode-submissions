class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> differences;
        vector<int> solution;
        for (int i = 0; i < nums.size(); i++){
            cout <<" this is i " << i << endl;
            int difference = target - nums[i];
            //in the case that you found it
            if (differences.find(difference) != differences.end())
            {
                cout <<" this is j being added" << differences[difference] << endl;
                solution.push_back(differences[difference]);

                cout <<" this is i being added" << i << endl;
                solution.push_back(i);
                
                return solution;
            }
            differences[nums[i]] = i;
        
        }
        
    }
};
