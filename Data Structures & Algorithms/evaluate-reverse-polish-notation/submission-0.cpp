class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> myStack;
        // you have a stack
        // 1 is already there
        // add 2 to the stack
        // if its a string, like + - / 
        // maybe once you hit the thing, till the queue is empty, you perform that operation

        for (string token : tokens){
            if (token == "+" || token == "-" || token == "/" || token == "*"){
                int top = myStack.top();
                myStack.pop();
                int result = 0;
                    if (token == "+") {
                        result = myStack.top() + top;
                        myStack.pop();
                    }
                    else if (token == "-") {
                        result = myStack.top() - top;
                        myStack.pop();
                    }
                    else if (token == "/") {
                        result = myStack.top()/ top;
                        myStack.pop();
                    }
                    else if (token == "*") {
                        result = myStack.top()* top;
                        myStack.pop();
                    }
                myStack.push(result);
            }
            else{
                myStack.push(stoi(token));
            }
        }
        return myStack.top();
    }
};
