int f_gold(int arr[], int n) {
    sort(arr, arr + n);
    return arr[n - 1];
}