int findDelayedArrivalTime(int arrivalTime, int delayedTime) {
    int sum=arrivalTime+delayedTime;
    if(sum==24){
        return 0;
    }
    if(sum<24){
        return sum;
    }
    return sum-24;
}