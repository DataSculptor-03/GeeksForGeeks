

/*class Solution{
  public:
    vector<int> duplicates(int arr[], int n) {
        // code here
    }
};*/

class Solution{
  public:
    vector<int> duplicates(int arr[], int n) {
        // code here
        sort(arr ,arr+n);
        vector<int> ans;
        for(int i = 0 ; i< n-1; i++){
            if(arr[i] == arr[i+1]){
                ans.push_back(arr[i]);
                int j = i;
                while(j < n && arr[j] == arr[i]){
                    j++;
                }
                i = j-1;
            }
        }
        if(ans.size() == 0){
            return {-1};
        }
        return ans;
    }
};
