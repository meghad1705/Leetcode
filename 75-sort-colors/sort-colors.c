void sortColors(int* nums, int numsSize) {
    for(int j=0;j<numsSize-1;j++){
        for(int i=0;i<numsSize-1;i++){
            if(nums[i]>nums[i+1]){
                int temp=nums[i];
                nums[i]=nums[i+1];
                nums[i+1]=temp;
            }
        }
    }

    return;
}