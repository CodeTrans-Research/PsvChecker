  int f_gold ( int n ) {
  int count = 0 ;
  while (n){
    n &= ( n - 1 ) ;
    count ++ ;
  }
  return count ;
}

