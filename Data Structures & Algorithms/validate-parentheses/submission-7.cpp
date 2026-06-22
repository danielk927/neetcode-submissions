class Solution {
public:
    bool isValid(string s) {
        stack<char> bracket;

        for (int i = 0; i < s.size(); i++){
        char c = s[i];

        if (c == ']'){
            if (bracket.empty()) return false;
            if (bracket.top() == '['){
                bracket.pop();
            }
            else{
                return false;
            }
        }

        else if (c == ')'){
            if (bracket.empty()) return false;
            if (bracket.top() == '('){
                bracket.pop();
            }
            else{
                return false;
            }
        }

        else if (c == '}'){
            if (bracket.empty()) return false;
            if (bracket.top() == '{'){
                bracket.pop();
            }
            else{
                return false;
            }
        }
        else{
            bracket.push(c);
        }
        }
        if (bracket.empty()){
            return true;
        }
        else{
            return false;
        }
    }
};
