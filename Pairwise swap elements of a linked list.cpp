

/*
  Pairwise swap a linked list
  The input list will have at least one element
  node is defined as

struct Node
{
    int data;
    struct Node* next;

    Node(int x){
        data = x;
        next = NULL;
    }

}*head;
*/
/*class Solution
{
    public:
    Node* pairWiseSwap(struct Node* head) 
    {
        // The task is to complete this method
    }
};*/

class Solution {
public:
    Node* pairWiseSwap(Node* head) 
    {
        if (head == nullptr || head->next == nullptr) 
        {
            return head; 
        }

        Node* newHead = head->next;
        Node* prev = nullptr;

        while (head != nullptr && head->next != nullptr) 
        {
            Node* first = head;
            Node* second = head->next;

            first->next = second->next;
            second->next = first;

            if (prev != nullptr) 
            {
                prev->next = second;
            }

            prev = first;
            head = first->next;
        }

        return newHead;
    }
};
