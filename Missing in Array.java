// User function Template for Java
class Solution {

    // Note that the size of the array is n-1
    int missingNumber(int n, int arr[]) {

        // Your Code Here
            int sum=(n*(n+1))/2;
            int res=0;
            for(int i=0;i<n-1;i++){
                res+=arr[i];
            }
            int mn=sum-res;
            return mn;
    }
}    
