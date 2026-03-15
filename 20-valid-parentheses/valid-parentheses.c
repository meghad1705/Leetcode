#include <string.h>

bool isValid(char* s) {
    char stack[10000];
    int top = -1;

    for(int i = 0; i < strlen(s); i++) {

        if(s[i] == '(' || s[i] == '{' || s[i] == '[') {
            stack[++top] = s[i];
        }
        else {
            if(top == -1)
                return false;

            char popped = stack[top--];

            if((s[i] == ')' && popped != '(') ||
               (s[i] == '}' && popped != '{') ||
               (s[i] == ']' && popped != '[')) {
                return false;
            }
        }
    }

    return top == -1;
}
