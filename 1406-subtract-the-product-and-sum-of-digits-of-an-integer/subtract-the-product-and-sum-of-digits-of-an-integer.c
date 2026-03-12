int subtractProductAndSum(int n) {
    int rem;
    int sum=0;
    double mul=1;
    while(n>0){
        rem=n%10;
        sum=sum+rem;
        mul=mul*rem;
        n/=10;
    }
    return mul-sum;
}