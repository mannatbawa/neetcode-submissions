class Solution {
public:
    bool isValid(string s) {
        stack<char> myStack;
        for (int i = 0; i < s.length(); i++){
            if (!myStack.empty())
            {
                char topElement = myStack.top();
                //if top element == string [s]
                if (topElement == '(' && s[i] == ')'){
                    myStack.pop();
                }
                else if (topElement == '{' && s[i] == '}'){
                    myStack.pop();
                }
                else if (topElement == '[' && s[i] == ']'){
                    myStack.pop();
                }
                else {
                    myStack.push(s[i]);
                }
            }
            else{
                myStack.push(s[i]);
            }
        }
        return myStack.empty();
        
    }
};
