int* sortArrayByParity(int* nums, int numsSize, int* returnSize) {

    for(int i = 0; i < numsSize - 1; i++) {
        for(int j = 0; j < numsSize - i - 1; j++) {

            if(nums[j] % 2 != 0 && nums[j+1] % 2 == 0) {
                int temp = nums[j];
                nums[j] = nums[j+1];
                nums[j+1] = temp;
            }

        }
    }

    *returnSize = numsSize;
    return nums;
}
