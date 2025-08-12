

//User function teamplate for C++

/*class Solution{
  public:
    vector<int> printClosest(int arr[], int brr[], int n, int m, int x) {
        //code here
    }
};*/


class Solution{
  public:
    vector<int> printClosest(int arr[], int brr[], int n, int m, int x) {
        int i=0,j=m-1;
        int diff=INT_MAX;
        vector<int>ans;
        while(i<n and j>=0){
            int currSum = arr[i]+brr[j];
            if(diff>abs(x-currSum)){
                diff = abs(x-currSum);
                ans = {arr[i],brr[j]};
            }
            if(currSum>x){
                j--;
            }
            else{
                i++;
            }
        }
        return ans;
    }
};
