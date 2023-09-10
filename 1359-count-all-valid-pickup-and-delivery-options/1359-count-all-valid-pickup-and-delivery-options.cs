public class Solution {
    private const int MOD = 1000000007;

    public int CountOrders(int n) {
        long count = 1;
        for (int i = 2; i <= n; i++) {
            count = (count * (2 * i - 1) * i) % MOD;
        }
        return (int)count;
    }

}