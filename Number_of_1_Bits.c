int hammingWeight(uint32_t n) {
   int i,num=0;
    for(i=1;i<=32;i++)
     {

       if((n&0x1)==1)
          num++;
       n=n>>1;
     }

    return num;
    
}