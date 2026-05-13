class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> s_freq;
        unordered_map<char, int> t_freq;

        for (char c: s)
        {
            s_freq[c]++;
        }
        for (char y: t){
            t_freq[y]++;
        }

        return (s_freq == t_freq);
        
    }
};
