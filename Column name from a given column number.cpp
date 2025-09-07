class Solution{
    public:
    string colName (long long int n)
    {   string str = "";
        while(n > 0){
            int d = n % 26 ;
            
            if(d == 0) {str = "Z" + str; n--;}
            // "Z " and 'A' gives its ASCII value afer  render
            else str = (char)('A' + d - 1) + str;
            n = n/26;
        }
        return str;
        // your code here
    }
};
