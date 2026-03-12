bool isPalindrome(int x) {
    double rev=0;
    int rem;
    int original=x;
    while(x>0){
        rem =x % 10;
        rev = rev * 10 + rem;
        x /=10;
        
    }
    if(original==rev){
        return true;

    }
    return false;
}