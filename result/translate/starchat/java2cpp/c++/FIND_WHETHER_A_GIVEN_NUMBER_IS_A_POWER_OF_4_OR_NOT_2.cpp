bool f_gold(int n) {
        return (n & (n - 1)) == 0 && (n & 0xAAAAAAAA) == 0;
    }