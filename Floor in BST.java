class Solution {
    public static int floor(Node root, int x) {
     Node tmp=root;
     int op=-1;
      while(tmp!=null){
         
          if(tmp.data<x){  
op=tmp.data;
tmp=tmp.right;
          }
  else  if(tmp.data>x){
   tmp=tmp.left;
  }
     else 
     return tmp.data;
      }
   
 return op;
    }
}
