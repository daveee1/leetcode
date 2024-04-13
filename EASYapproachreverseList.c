/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    if (head==NULL){
        return head;
    }
    struct ListNode* h=head; //look for number of all the elements in the list
    int first,last,temp;
    last=0;
    while(h!=NULL){
        h=h->next;
        last++;
    }
    //add all elements
    int arr[last];         //array to be inverted
    first=0;
    h=head;
    while (h!=NULL){
        arr[first]=h->val;
        h=h->next;
        first++;
    }

    //arr inverted
    first=0;
    last=last-1;
    while (first<last){
        temp=arr[first];
        arr[first]=arr[last];
        arr[last]=temp;
        first++;
        last--;
    }
    //add the elements to a reverse list
    first=0;
    h = head;
    while (h != NULL) {
        h->val = arr[first];
        h = h->next;
        first++;
    }
    return head; 
}
