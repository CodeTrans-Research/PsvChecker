// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <fstream>
#include <iomanip>
#include <bits/stdc++.h>
using namespace std;
int f_gold ( int a [ ], int n ) {
  unordered_map < int, int > cnt;
  int ans = 0, pre_sum = 0;
  for ( int i = 0;
  i < n;
  i ++ ) {
    ans += ( i * a [ i ] ) - pre_sum;
    pre_sum += a [ i ];
    if ( cnt [ a [ i ] - 1 ] ) ans -= cnt [ a [ i ] - 1 ];
    if ( cnt [ a [ i ] + 1 ] ) ans += cnt [ a [ i ] + 1 ];
    cnt [ a [ i ] ] ++;
  }
  return ans;
}


int f_filled ( int a [ ] , int n ) {
  map < int , int > cnt ;
  int ans = 0 , pre_sum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    ans += ( i * a [ i ] ) - pre_sum ;
    pre_sum += a [ i ] ;
    if ( cnt . count ( a [ i ] - 1 ) ) {
      ans -= cnt [ a [ i ] - 1 ] ;
    }
    if ( cnt . count ( a [ i ] + 1 ) ) {
      ans += cnt [ a [ i ] + 1 ] ;
    }
    if ( cnt . count ( a [ i ] ) ) {
      cnt [ a [ i ] ] = cnt [ a [ i ] ] + 1 ;
    }
    else {
      cnt [ a [ i ] ] = 1 ;
    }
  }
  return ans ;
}

int main() {
    int n_success = 0;
    vector<vector<int>> param0 {{2,8,12,19,23,23,26,39,54,56,57,57,73,78,83,83,89,91},{62,-34,10,-28,-42,-12,4,20,-20,-84,-76,-16,-44,26,-78,-40,50,-10,-56,76,-88,24,64,10,64,-8,-68,-42,26,24,62,36,-68,8,-68,-2,8,38,-18},{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1},{23,14,44,29,93,56,22,29,97,71,43,72,74,8,92,40,18,34,78,79,93,63,79,44,35,72,88,83,40,89,66,66,54,56,44,62,72,94,79,79,24,55,72,37,27,55,16,58,83},{-96,-94,-90,-90,-86,-82,-80,-80,-58,-48,-40,-32,-32,-20,-20,-20,-12,-12,-6,-6,-2,0,4,16,16,16,42,48,58,64,68,76,76,76,78,80,82,88,88,88,92,94,96,98},{1,1,1,1,0,0,0,1,1,0,0,1,0,0,1,1,0,0,0,0,1,1,0,0,1,1,1,0,1,0,0,0,1,1,1,0,0,1,1,1,1},{3,4,4,8,10,10,11,15,19,19,20,24,25,25,27,30,41,43,44,45,47,55,59,59,61,63,63,67,67,69,72,73,75,77,77,78,81,81,83,84,92,94,99},{94,-86,94,54,-52,86,68,64,98,54,-14,-60,-60,-92,80,-16,28,16,-74,68,32,-54,58,-16,-2,-52,-92,-36,96,-18,14,76,16},{0,0,0,0,1,1,1,1},{10,28,63,2,78,12,51,82,89,65,99}};
    vector<int> param1 {15,20,18,25,27,34,31,26,7,8};
    for(int i = 0; i < param0.size(); ++i)
    {
        if(f_filled(&param0[i].front(),param1[i]) == f_gold(&param0[i].front(),param1[i]))
        {
            n_success+=1;
        }
    }
    cout << "#Results:" << " " << n_success << ", " << param0.size();
    return 0;
}