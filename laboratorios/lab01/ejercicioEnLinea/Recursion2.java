public boolean groupSum6(int start, int[] nums, int target) {
  boolean use = false; //T(n)=C1=1
  boolean dontUse = false; //T(n)=C2=1
  if (start>= nums.length){ //T(n)=C3=3
    return target == 0; //T(n)=C4=2
  }
  else{ //T(n)=C5=1
    if (nums[start]==6){ //T(n)=C6=3
      use = groupSum6(start+1, nums, target-nums[start]); //T(n)=T(n-1)+C6 (C6=4)
    }else{ //T(n)=C7 (C7=1)
      use = groupSum6(start+1, nums, target-nums[start]); //T(n)=T(n-1)+C8 (C9=4)
      dontUse = groupSum6(start+1, nums, target); //T(n)=T(n-1)+C9 (C9=2)
    } // T(n)=C7+T(n-1)+C8+T(n-1)+C9
    return use || dontUse; //T(n)=C10 (C10=2)
  }
}
//T(n)=C7+T(n-1)+C8+T(n-1)+C9 = 2T(n-1)+C (donde n es la posición del arreglo que se está sumando)
//T(n)=C(2^n-1)+C1*2^(n-1)
//O(2^n)

public boolean groupSum5(int start, int[] nums, int target) {
  boolean use = false; //T(n)=C1=1
  boolean dontUse = false; //T(n)=C2=1
  if (start>= nums.length){ //T(n)=C3=3
    return target ==0; //T(n)=C4=2
  }
  else{ //T(n)=C5=1
    if(nums[start]==1 && start>0 && nums[start-1]%5==0){ //T(n)=C6=10
      dontUse = groupSum5(start+1, nums, target); //T(n)=T(n-1)+C7 (C7=2)
      }
    else if (nums[start]%5==0){ //T(n)=C8=4
      use = groupSum5(start+1, nums, target-nums[start]); //T(n)=T(n-1)+C9 (C9=4)
    }
    else{ //T(n)=C10=1
      use = groupSum5(start+1, nums, target-nums[start]); //T(n)=T(n-1)+C11 (C11=4)
      dontUse = groupSum5(start+1, nums, target); //T(n)=T(n-1)+C12 (C12=2)
    } // T(n)=C10+T(n-1)+C11+T(n-1)+C12
    return use || dontUse; //T(n)=C13=2
  }
}
//T(n)=C10+T(n-1)+C11+T(n-1)+C12 = 2T(n-1)+C (donde n es la posición del arreglo que se está sumando)
//T(n)=C(2^n-1)+C1*2^(n-1)
//O(2^n)

public boolean groupNoAdj(int start, int[] nums, int target) {
  boolean use = false; //T(n)=C1=1
  boolean dontUse = false; //T(n)=C2=1
  if (start>= nums.length){ //T(n)=C3=3
    return target ==0; //T(n)=C4=2
  }
  else{ //T(n)=C5=1
    use = groupNoAdj(start+2, nums, target-nums[start]); //T(n)=T(n-2)+C6 (C6=4)
    dontUse = groupNoAdj(start+1, nums, target); //T(n)=T(n-1)+C7 (C7=2)
    return use || dontUse; //T(n)=C8=2
  } //T(n)=C5+T(n-2)+C6+T(n-1)+C7+C8
}
//T(n)=C5+T(n-2)+C6+T(n-1)+C7+C8=T(n-2)+T(n-1)+C (donde n es la posición del arreglo que se está sumando)
//O(2^n)

public boolean groupSumClump(int start, int[] nums, int target) {
  boolean use = false; //T(n)=C1=1
  boolean dontUse = false; //T(n)=C2=1
  if (start>= nums.length){ //T(n)=C3=3
    return target == 0; //T(n)=C4=2
  }
  else{ //T(n)=C5=1
    int count = 1; //T(n)=C6=1
    for(int i=start; i<nums.length-1; i++){ //T(n)=C7+n*C8 (C7=1, C8=4)
      if(nums[start]==nums[i+1]){ //T(n)=C9*n (C9=5)
          count++; //T(n)=C10*n (C10=2)
        }
    }
    use = groupSumClump(start+count, nums, target-(count*nums[start])); //T(n)=T(n-count)+C11 (C11=5)
    dontUse = groupSumClump(start+count, nums, target); //T(n)=T(n-count)+C12 (C12=2)
    } //T(n)=C5+C6+C7+n*C8+C9*n+T(n-count)+C11+T(n-count)+C12

    return use || dontUse; //T(n)=C13=2
  }
//T(n)=C5+C6+C7+n*C8+C9*n+T(n-count)+C11+T(n-count)+C12
//T(n)=2*n*C14+2T(n-count)+C15

public boolean splitArray(int[] nums) {
  return auxSplitArray(nums, 0, 0, 0); //T(n)=C1=?
}
public boolean auxSplitArray(int[]nums, int start, int group1, int group2){
  if(start>=nums.length){ //T(n)=C2=3
    return group1==group2; //T(n)=C3=2
  }
  else{ //T(n)=C4=1
    boolean add1 = auxSplitArray(nums, start+1, group1+nums[start], group2); //T(n)=T(n-1)+C5 (C5=4)
    boolean add2 = auxSplitArray(nums, start+1, group1, group2+nums[start]); //T(n)=T(n-1)+C6 (C6=4)
    return add1 || add2; //T(n)=C7=2
  }
}
//T(n)=T(n-1)+C5+T(n-1)+C6=2T(n-1)+C (donde n es la posición del arreglo que se está sumando a un grupo o al otro)
//T(n)=C(2^n-1)+C1*2^(n-1)
//O(2^n)