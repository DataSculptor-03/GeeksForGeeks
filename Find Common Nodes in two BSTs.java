

//User function Template for Java


/*class Solution
{
    //Function to find the nodes that are common in both BST.
	public static ArrayList<Integer> findCommon(Node root1,Node root2)
    {
        //code here
    }
}*/


class Solution
{
    private static HashSet<Integer> hset; //used to store values from bst
    private static ArrayList<Integer> list;//it store coommon values
    private static boolean traverse;
    
    public static ArrayList<Integer> findCommon(Node root1,Node root2)
    {
        //code here
        hset = new HashSet<>(); //initialize the hashset
        list = new ArrayList<>();//initialize the arraylist
        traverse = false ;
        inorder(root1);//traverse the first bst
        traverse = true;
        inorder(root2); // traverse the second bst
        return list;//return the list of common values
        
    }
    //helper function to perform an in-order traversa; of bst
    private static void inorder(Node root){
        if(root == null){
            return;
        }
        inorder(root.left);
        
        if(!traverse){
            hset.add(root.data); //add values to the hashset from first bst
        }else{
            if(hset.contains(root.data)){
                list.add(root.data);
                //if value is in hashset ,it's a coommon value ,so add it to the list
            }
        }
        inorder(root.right);
        return;
    }
}
