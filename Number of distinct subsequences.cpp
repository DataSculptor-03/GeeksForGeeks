

//User function template for C++

/*class Solution{
  public:	
	int distinctSubsequences(string s)
	{
	    // Your code goes heint mod=1e9+7;
        int n=s.size();
        unordered_map<char,int>m;
        vector<int>dp(n+1);
        dp[0]=1;
        for(int i=1;i<=n;i++){
            dp[i]= (2*dp[i-1])%mod;
            char ch=s[i-1];
            if(m[ch]){
                int j=m[ch];
                dp[i]=(dp[i]-dp[j-1]+mod)%mod;
            }
            m[ch]=i;
        }
        return dp[n];re
	}
};*/

class Solution{
  public:
int distinctSubsequences(string s)
{
    int n = s.size();
    int dp[n + 1];
    
    int mod = 1e9 + 7;
    dp[0] = 1;
    
    // Space : O(n)
    unordered_map <char, int> mp;
    
    // Time : O(n)
    for(int i = 1;i <= n;i++){
        
        dp[i] = (dp[i - 1] * 2) % mod;
        
        
        char c = s[i - 1];
        
        if(mp.find(c) != mp.end()){
            dp[i] = (dp[i] - dp[mp[c] - 1] + mod) % mod;
        }
        mp[c] = i;
    }
    
    return dp[n] % mod;
}


};
