public class Array3{
  public int[] seriesUp(int n) {
    int[] array = new int[n*(n + 1)/2]; //T(n)=c1
    int count = 0; //T(n)=c2
    for(int i=1; i<=n; i++){ //T(n)=n*c3
      for(int j =1; j<=i;j++){ //T(n)=n*c4*n
        array[count]=j; //T(n)=n*n*n*c5  -T(n)=n*n*c5
        count++; //T(n)=c6*n*n
      }
    }
    return array; //T(n)=c7
  }
  //T(n)=c*nˆ2
  //O(nˆ2)

  public boolean linearIn(int[] outer, int[] inner) {
    int in = 0; //T(n)=c1
    int out=0; //T(n)=c2
    for (out=0; out<outer.length && in<inner.length; out++){ //T(n)=c3*n
      if (outer[out]==inner[in]){ //T(n)=c4*n
        in++; //T(n)=c5*n
      }
    }
    return in==inner.length; //T(n)=c6
  }
  //T(n)=c*n
  //O(n)

  public boolean canBalance(int[] nums) {
    for(int i=0; i<nums.length; i++){ //T(n)=c1*n
      int sum1 = 0; //T(n)=c2*n
      int sum2 = 0; //T(n)=c3*n
      for(int j=0; j<i; j++){ //T(n)=c4*n*n
        sum1= sum1+nums[j]; //T(n)=c5*n*n
      }
      for(int k=i; k<nums.length; k++){ //T(n)=c6*n*n
        sum2= sum2+nums[k]; //T(n)=c7*n*n
      }
      if(sum1==sum2){ //T(n)=c8*n
        return true; //T(n)=c9*n
      }
    }
    return false; //T(n)=c10
  }
  //T(n)=c*n*n
  //T(n)=c1001*nˆ2
  //O(nˆ2)

  public int[] fix34(int[] nums) {
    for(int i=0; i<nums.length; i++){ //T(n)=c1*n
      if(nums[i]==3){ //T(n)=c2*n
        int temp = nums[i+1]; //T(n)=c3*n
        for(int j=i+1;j<nums.length;j++){ //T(n)=c4*n*n
          if(nums[j]==4){ //T(n)=c5*n*n
            nums[j]=temp; //T(n)=c6*n*n
          }
        }
        nums[i+1]=4; //T(n)=c7*n
      }
    }
    return nums; //T(n)=c8
  }
  //T(n)=c*n*n
  //T(n)=c5*nˆ2
  //O(nˆ2)

  public int[] fix45(int[] nums) {
    for(int i=0; i<nums.length; i++){ //T(n)=c1*n
      for(int j=0; j<nums.length; j++){ //T(n)=c2*n*n
        if(nums[j]==4 && nums[i] == 5){ //T(n)=c3*n*n
          int temp = nums[j+1]; //T(n)=c4*n*n
          nums[j+1]=5; //T(n)=c5*n*n
          nums[i]= temp; //T(n)=c6*n*n
        }
      }
    }
    return nums; //T(n)=c7
  }
  //T(n)=c*n*n
  //T(n)=c*nˆ2
  //O(nˆ2)
}