


/*class Solution
{   
    public:
    //Function to return list of integers that form the boundary 
    //traversal of the matrix in a clockwise manner.
    vector<int> boundaryTraversal(vector<vector<int> > matrix, int n, int m) 
    {
        // code here
    }
};*/

/*#include <iostream>
#include <vector>

using namespace std;

class MatrixTraversal {
private:
    vector<vector<int>> matrix;
    int n, m;

public:
    MatrixTraversal(vector<vector<int>>& mat) {
        matrix = mat;
        n = matrix.size();
        m = matrix[0].size();
    }

    void traverseBoundary() {
        if (n == 0 || m == 0) return;

        for (int i = 0; i < m; i++) {
            cout << matrix[0][i] << " ";
        }

        for (int i = 1; i < n; i++) {
            cout << matrix[i][m - 1] << " ";
        }

        if (n > 1) {
            for (int i = m - 2; i >= 0; i--) {
                cout << matrix[n - 1][i] << " ";
            }
        }

        if (m > 1) {
            for (int i = n - 2; i > 0; i--) {
                cout << matrix[i][0] << " ";
            }
        }
    }
};

int main() {
    vector<vector<int>> mat = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    MatrixTraversal mt(mat);
    mt.traverseBoundary();

    return 0;
}*/


class Solution
{   
    public:
    vector<int> boundaryTraversal(vector<vector<int> > matrix, int n, int m) 
    {
        vector<int> ans;
        
        for(int i=0; i<m; i++) ans.push_back(matrix[0][i]);
        if(n == 1) return ans;
        
        for(int i=1; i<n; i++) ans.push_back(matrix[i][m-1]);
        if(m == 1) return ans;
        
        for(int i=m-2; i>=0; i--) ans.push_back(matrix[n-1][i]);
        
        for(int i=n-2; i>=1; i--) ans.push_back(matrix[i][0]);
        
        return ans;
    }
};
