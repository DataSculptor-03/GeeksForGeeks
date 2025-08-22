



/*class Solution
{   
    public:
    //Function to modify the matrix such that if a matrix cell matrix[i][j]
    //is 1 then all the cells in its ith row and jth column will become 1.
    void booleanMatrix(vector<vector<int> > &matrix)
    {
        // code here 
    }
};*/

class Solution
{   
    public:
    //Function to modify the matrix such that if a matrix cell matrix[i][j]
    //is 1 then all the cells in its ith row and jth column will become 1.
    void booleanMatrix(vector<vector<int> > &matrix)
    {
        // code here 
int n = matrix.size();
        int m = matrix[0].size();
  
       vector<int> visR(n,0);
       vector<int> visC(m,0);
       for(int i = 0; i<n; i++){
           for(int j= 0; j<m; j++){
               if(matrix[i][j] == 1){
                   visR[i] = 1;
                   visC[j] = 1;
                
               }
           }
       }
       for(int i = 0; i<n; i++){
           for(int j = 0; j<m; j++){
               if(visR[i] == 1 || visC[j] == 1){
                   matrix[i][j] = 1;
               }
           }
       }
    }
};
