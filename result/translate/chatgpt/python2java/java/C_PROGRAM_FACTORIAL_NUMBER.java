public static int f_gold(int n) {
    if (n == 1 || n == 0) {
        return 1;
    } else {
        return n * f_gold(n - 1);
    }
}