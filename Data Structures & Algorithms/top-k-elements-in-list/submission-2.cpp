class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> frequencies;
    
        vector<int> solution;

        for (int i = 0; i < nums.size(); i++){
            frequencies[nums[i]]++;
        }

        map<int, vector<int>> reversed_freq;

        for (auto it = frequencies.begin(); it != frequencies.end(); it++){
            reversed_freq[it->second].push_back(it->first);
        }

        for (auto it = reversed_freq.rbegin(); it != reversed_freq.rend(); it++)
        {
            for (int i = 0; i < it->second.size(); i++){
                solution.push_back(it->second[i]);
                if (solution.size() >= k){
                    return solution;
                }
            }
        }
        return solution;

        
    }
};
