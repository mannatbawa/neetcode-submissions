class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        //brute force: order all the strings, group them together
        //vector of vectors
        //hash map for each string to determine their frequencey
        //if this frequency matches with something in the hash map, add it 
        map<vector<int>, vector<string>> groupings;
        vector<vector<string>> solution; 
        //key is the frequency
        
        for (string str : strs){
            vector<int> str_freq(26,0);
            for (char c : str){
                str_freq[c-'a']++;
            }
            groupings[str_freq].push_back(str);
        } 
        for (auto it = groupings.begin(); it != groupings.end(); it++){
            solution.push_back(it->second);
        }
        return solution;
    }
};
