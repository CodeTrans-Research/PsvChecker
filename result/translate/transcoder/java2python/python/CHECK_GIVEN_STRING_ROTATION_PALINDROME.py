def f_gold ( str ) :
    l = 0
    h = len ( str ) - 1
    while h > l :
        if str [ l ] != str [ h -- ] :
            return False
    return True
