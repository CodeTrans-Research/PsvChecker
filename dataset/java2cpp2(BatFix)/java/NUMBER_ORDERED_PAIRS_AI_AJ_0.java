int f_gold ( int a [ ], int n ) {
  int count = 0;
  for ( int i = 0;
  i < n;
  i ++ ) {
    for ( int j = i + 1;
    j < n;
    j ++ ) if ( ( a [ i ] & a [ j ] ) == 0 ) count += 2;
  }
  return count;
}