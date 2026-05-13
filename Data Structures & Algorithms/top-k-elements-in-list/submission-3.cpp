class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> frequencies;
    

        for (int i = 0; i < nums.size(); i++){
            frequencies[nums[i]]++;
        }

        vector<vector<int>> reversed_freq(nums.size()+1);

        for (auto it = frequencies.begin(); it != frequencies.end(); it++){
            reversed_freq[it->second].push_back(it->first);
        }

        vector<int> solution;
        for (int i = reversed_freq.size() - 1; i > 0; i--)
        {
            for (int j : reversed_freq[i]){
                solution.push_back(j);
                if (solution.size() >= k){
                    return solution;
                }
            }
        }
        return solution;

        
    }
};
