boolean f_gold ( int set [ ], int n, int sum ) {
  boolean subset [ ] [ ] = new boolean [ sum + 1 ] [ n + 1 ];
  for ( int i = 0;
  i <= n;
  i ++ ) subset [ 0 ] [ i ] = true;
  for ( int i = 1;
  i <= sum;
  i ++ ) subset [ i ] [ 0 ] = false;
  for ( int i = 1;
  i <= sum;
  i ++ ) {
    for ( int j = 1;
    j <= n;
    j ++ ) {
      subset [ i ] [ j ] = subset [ i ] [ j - 1 ];
      if ( i >= set [ j - 1 ] ) subset [ i ] [ j ] = subset [ i ] [ j ] || subset [ i - set [ j - 1 ] ] [ j - 1 ];
    }
  }
  return subset [ sum ] [ n ];
}