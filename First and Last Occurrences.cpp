class Solution
{
    private:
    int firstOccurence(int arr[], int n, int x) {
        int low = 0;
        int high = n-1;
        int first = -1;
        while(low<=high) {
            int mid = (low + high) / 2;
            if(arr[mid] == x) {
                first = mid;
                high = mid - 1;
            }
            else if(arr[mid] < x) low = mid + 1;
            else high = mid - 1;
        }
        return first;
    }
    
    int lastOccurence(int arr[], int n, int x){
        int low = 0, high = n-1;
        int last = -1;
        while(low <= high) {
            int mid = (low+high) / 2;
            if(arr[mid] == x) {
                last = mid;
                low = mid + 1;
            }
            else if(arr[mid] < x) low = mid + 1; 
            else high = mid - 1;
        }
        return last ;
    }
    public:
    vector<int> find(int arr[], int n , int x )
    {
        int first = firstOccurence(arr, n, x);
	    if(first == -1) return {-1, -1};
    	int last = lastOccurence(arr, n, x);
	    return {first, last};
    }
};
