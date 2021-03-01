public int fibonacci(int n) {
  if (n==0){ // T(n)=C1=2
    return 0; //T(n)=C2=1
  }
  if (n==1){ //T(n)=C3=2
    return 1; //T(n)=C4=1
  }
  return fibonacci(n-1)+fibonacci(n-2); //T(n)=T(n-1)+T(n-2)+C5
}
//T(n)=T(n-1)+T(n-2)+C (donde n es la posición del número de Fibonnaci que estamos buscando)
//T(n)=-C+C1Fn+C2Ln (Fn is the nth fibonacci number and Ln is the nth Lucas number)
//O(2^n)

public int bunnyEars(int bunnies) {
  if(bunnies==0){ //T(n)=C1=2
    return 0; //T(n)=C2=1
  }
  return  bunnyEars(bunnies-1) +2; //T(n)=T(n-1)+C3 (C3=3)
}
//T(n)=T(n-1)+C (donde n es la cantidad de conejos)
//T(n)=Cn+C1
//O(n)

public int bunnyEars2(int bunnies) {
  if(bunnies==0){ //T(n)=C1=2
    return 0; //T(n)=C2=1
  }
  if(bunnies%2 == 1){ //T(n)=C3=2
    return bunnyEars2(bunnies-1)+2; //T(n)= T(n-1)+C4 (C4=3)
  }
  else{
    return bunnyEars2(bunnies-1)+3; //T(n)= T(n-1)+C5 (C4=4)
  }
}
//T(n)=T(n-1)+C (donde n es la cantidad de conejos)
//T(n)=Cn+C1
//O(n)

public int triangle(int rows) {
  if(rows==0){ //T(n)=C1=2
    return 0; //T(n)=C2=1
  }
  return triangle(rows-1)+rows; //T(n)=T(n-1)+C3 (C3=3)
}
//T(n)=T(n-1)+C (donde n es la cantidad de filas del triángulo)
//T(n)=Cn+C1
//O(n)

public int sumDigits(int n) {
  if(n<=0){ //T(n)=C1=2
    return 0; //T(n)=C2=1
  }
  return n%10 + sumDigits(n/10); //T(n)=T(n/10)+C3 (C3=4)
}
//T(n)=T(n/10)+C (donde n es el número al que se le quieren sumar los dígitos)
//T(n)=Clog10(n)+C1
//O(log10n)
