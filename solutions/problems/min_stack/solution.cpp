class MinStack {
public:
    stack<long> stack;
    long min;

    MinStack() {}
    
    void push(int val) {
        if (stack.empty()) {
            stack.push(0);
            min = val;
        } else {
            stack.push(val - min);
            if (val < min) {
                min = val;
            }
        }
    }
    
    void pop() {
        if (stack.top() < 0) {
            min = min - stack.top();
        }
        stack.pop();
    }
    
    int top() {
        if (stack.top() < 0) {
            return min;
        } else {
            return stack.top() + min;
        }
    }
    
    int getMin() {
        return min;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */