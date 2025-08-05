



/*class Solution
{   
    public:
    //Function to return sum of upper and lower triangles of a matrix.
    vector<int> sumTriangles(const vector<vector<int> >& matrix, int n)
    {
        // code here
    }
};*/

class Solution
{   
    public:
    //Function to return sum of upper and lower triangles of a matrix.
    vector<int> sumTriangles(const vector<vector<int> >& matrix, int n)
    {
        // code here
        int ut = 0, lt = 0;
        
        for(int i=0; i<n; i++){
            for(int j=i; j<n; j++){
                ut += matrix[i][j];
            }
        }
        
        for(int i=0; i<n; i++){
            for(int j=i; j<n; j++){
                lt += matrix[j][i];
            }
        }
        
        return {ut, lt};
    }
};
