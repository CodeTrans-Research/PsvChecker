int f_gold ( int [ ] arr, int n ) {
  Map < Integer, Integer > myMap = new HashMap < > ( );
  int sum = 0;
  int count = 0;
  for ( int i = 0;
  i < n;
  i ++ ) {
    if ( arr [ i ] == 0 ) arr [ i ] = - 1;
    sum += arr [ i ];
    if ( sum == 0 ) count ++;
    if ( myMap . containsKey ( sum ) ) count += myMap . get ( sum );
    if ( ! myMap . containsKey ( sum ) ) myMap . put ( sum, 1 );
    else myMap . put ( sum, myMap . get ( sum ) + 1 );
  }
  return count;
}