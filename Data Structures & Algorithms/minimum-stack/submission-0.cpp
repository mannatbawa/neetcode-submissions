class MinStack {
public:
    vector<int> stack;
    vector<int> minstack;     

    MinStack() {
        
    }
    
    void push(int val) {
        stack.push_back(val);
        if (!minstack.empty())
        {
            int minimum = min(minstack.back(), val);
            minstack.push_back(minimum);
        }
        else{
            minstack.push_back(val);
        }
        
    }
    
    void pop() {
        if (!stack.empty()){
            stack.pop_back();
            minstack.pop_back();
        }
    }
    
    int top() {
        if (!stack.empty()){
            return stack.back();
        }
        return -1;
    } 
    
    int getMin() {
        if (!minstack.empty()){
            return minstack.back();
        }
        return -1;
    }
};
