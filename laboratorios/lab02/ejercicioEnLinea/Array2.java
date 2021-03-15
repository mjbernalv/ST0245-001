public class Array2{
  public int countEvens(int[] nums) {
    int counter = 0; //T(n)=c1=1
    for(int i=0; i<nums.length;i++){ //T(n)=c2*n (c2=5)
      if(nums[i]%2==0){ //T(n)=n*c3 (c3=4)
        counter++; //T(n)=n*c4 (c4=2)
      }
    }
    return counter; //T(n)=c5=1
  }
  //T(n)=n*c
  //O(n)

  public int bigDiff(int[] nums) {
    int min = nums[0]; //T(n)=c1=2
    int max = nums[0]; //T(n)=c2=2
    for(int i=0; i<nums.length;i++){ //T(n)=c3*n (c3=5)
      for(int j=i+1; j<nums.length;j++){ //T(n)=c4*(n-1)*n (c4=6)
        if (Math.min(nums[i], nums[j])<min){ //T(n)=c5*(n-1)*n (c5=5)
          min = Math.min(nums[i], nums[j]); //T(n)=c6*(n-1)*n (c6=4)
        }
        if (Math.max(nums[i], nums[j])>max){ //T(n)=c7*(n-1)*n (c7=5)
          max = Math.max(nums[i], nums[j]); //T(n)=c8*(n-1)*n (c8=4)
        }
      }
    }
    return max-min; //T(n)=c9=2
  }
  //T(n)=c*(n-1)*n
  //T(n)=cnˆ2-cn
  //O(nˆ2)

  public int centeredAverage(int[] nums) {
    int min = nums[0]; //T(n)=c1=2
    int max = nums[0]; //T(n)=c2=2
    int sum = 0;  //T(n)=c3=1
    for(int i=0; i<nums.length;i++){ //T(n)=c4*n (c4=5)
      for(int j=i+1; j<nums.length;j++){ //T(n)=c5*(n-1)*n (c5=6)
        if (Math.min(nums[i], nums[j])<min){ //T(n)=c6*(n-1)*n (c6=5)
          min = Math.min(nums[i], nums[j]); //T(n)=c7*(n-1)*n (c7=4)
        }
        if (Math.max(nums[i], nums[j])>max){ //T(n)=c8*(n-1)*n (c8=5)
          max = Math.max(nums[i], nums[j]); //T(n)=c9*(n-1)*n (c9=4)
        }
      }
    }
    for(int k=0; k<nums.length;k++){ //T(n)=c10*n (c10=5)
      sum = sum + nums[k]; //T(n)=c11*n (c1=3)
    }
    return (sum-min-max)/(nums.length-2); //T(n)=c12=6
  }
  //T(n)=c*(n-1)*n
  //T(n)=cnˆ2-cn
  //O(nˆ2)

  public int sum13(int[] nums) {
    int sum = 0; //T(n)=c1=1
    if(nums.length==0){ //T(n)=c2=3
      return sum; //T(n)=c3=1
    }
    else{
      for(int i=0; i<nums.length; i++){ //T(n)=c4*n (c4=5)
        if(nums[i]==13){ //T(n)=c5*n (c5=3)
          i++; //T(n)=c6*n (c6=2)
        }
        else{
          sum=sum+nums[i]; //T(n)=c7*n (c7=3)
        }
      }
    } //T(n)=c4*n+c5*n+c6*n+c7*n
    return sum; //T(n)=c8=1
  }
  //T(n)=c*n
  //O(n)

  public boolean has22(int[] nums) {
    for(int i=0; i<nums.length;i++){ //T(n)=c1*n (c1=5)
      if(i!=nums.length-1 && nums[i]==2 && nums[i+1]==2){ //T(n)=c2*n (c2=11)
        return true; //T(n)=c3*n (c3=1)
      }
    }
    return false; //T(n)=c4=1
  }
  //T(n)=c*n
  //O(n)
}