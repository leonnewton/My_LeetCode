int singleNumber(int* nums, int numsSize) {
     int i,m=0;
    for(i=0;i<numsSize;i++)
        m=m^nums[i];
    return m;
}