class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        //basically go through the words
        //make a frequency code through the alphabet
        //if that frequency code doesnt exists in the map add it as the key 

        //key -- int: frequency code of the alphabet
        //value -- strings  
        map<vector<int>, vector<string>> frequency;
        //end goal
        vector<vector<string>> solution;

        for (int i = 0; i < strs.size(); i++){
            //searched up
            vector<int> alphabetArray(26,0);
            for (char c: strs[i]){
                alphabetArray[c-'a']++;
            }
            frequency[alphabetArray].push_back(strs[i]); 
        }
        for (auto it: frequency){
            solution.push_back(it.second);
        }
        return solution;
    }
};
