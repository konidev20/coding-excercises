/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {

    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        ListNode p1 = l1;
        ListNode p2 = l2;
        
        ListNode result = null;
        
        int carry = 0;
        
        while (p1 != null || p2 != null || carry > 0)
        {
            int d1 = 0;
            int d2 = 0;
            
            if(p1 != null){
                d1 = p1.val;
                p1 = p1.next;
            }
            
            if(p2 != null){
                d2 = p2.val;
                p2 = p2.next;
            }
            
            int sum = d1 + d2 + carry;
            
            if(sum < 10)
            {
                result = AddNode(result, sum);
                carry = 0;
            }
            else
            {
                result = AddNode(result, sum%10);
                carry = sum / 10;
            }
        }
        
        return result;
    }
    
    public static ListNode AddNode(ListNode head, int value){
        if(head == null)
        {
            head = new ListNode(value);
        }
        else
        {
            ListNode pointer = head;
            while(pointer.next != null)
            {
                pointer = pointer.next;
            }
            pointer.next = new ListNode(value);
        }
        return head;
    }
}