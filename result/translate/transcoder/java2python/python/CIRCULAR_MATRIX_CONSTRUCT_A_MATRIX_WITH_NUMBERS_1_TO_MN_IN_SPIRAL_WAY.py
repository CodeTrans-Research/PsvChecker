def f_gold ( m , n , a ) :
    val = 1
    k , l = 0 , 0
    while k < m and l < n :
        for i in range ( l , n ) :
            a [ k ] [ i ] = val ++
        k += 1
        for i in range ( k , m ) :
            a [ i ] [ n - 1 ] = val ++
        n -= 1
        if k < m :
            for i in range ( n - 1 , l , - 1 ) :
                a [ m - 1 ] [ i ] = val ++
            m -= 1
        if l < n :
            for i in range ( m - 1 , k , - 1 ) :
                a [ i ] [ l ] = val ++
            l += 1