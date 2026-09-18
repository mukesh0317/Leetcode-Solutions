class Solution {
    public int tribonacci(int n) {
        if (n == 0) return 0;
        if (n == 1 || n == 2) return 1;
        int[] dp = new int[n + 1];
        Arrays.fill(dp, -1);
        return helper(n, dp);

    }
    int helper(int n, int[]dp){
        if (dp[n] != -1) return dp[n];
        if(n==0)return 0;
        if(n==1 || n==2)return 1;
        return dp[n] = helper(n - 1, dp) + helper(n - 2, dp) + helper(n - 3, dp);

    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna