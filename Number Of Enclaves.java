class Solution {
    
    
    void dfs(int i,int j,int arr[][]){
        
        if( i<0 || j<0 || i>=arr.length || j>=arr[0].length || arr[i][j]==0 )return;
        arr[i][j]=0;
        dfs(i-1,j,arr);
        dfs(i,j+1,arr);
        dfs(i+1,j,arr);
        dfs(i,j-1,arr);
        
    }
    

    int numberOfEnclaves(int[][] arr) {
        int n=arr.length;
        int m=arr[0].length;
        if(n==1 || m==1 || n==2 || m==2)return 0;  

       
        for(int j=0;j<m;j++){
            if(arr[0][j]==1)dfs(0,j,arr);   
        }
        
        for(int i=1;i<n;i++){
            if(arr[i][0]==1)dfs(i,0,arr);   
        }
        
        
        for(int j=1;j<m;j++){
            if(arr[n-1][j]==1)dfs(n-1,j,arr);   
        }
        
        for(int i=n-1;i>=1;i--){
            if(arr[i][m-1]==1)dfs(i,m-1,arr); 
        }
                    
                int cnt=0;
                  for(int i=0;i<n;i++){
                      for(int j=0;j<m;j++){
                          if(arr[i][j]==1){
                            cnt+=1;  
                          }
                      }
                  }
      
      return cnt;
        
        
    }
    
   
    
}
