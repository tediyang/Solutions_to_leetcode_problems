#include <stdio.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2)
{
    struct ListNode* result, *dummy;
    result = malloc(sizeof(struct ListNode));
    dummy = result;
    result->val = 0;
    result->next = NULL;

    int remain = 0;

    while (l1 != NULL || l2!=NULL || remain !=0)
    {
        int a = (l1 == NULL) ? 0 : l1->val;
        int b = (l2 == NULL) ? 0 : l2->val;
        dummy->val = a + b + remain;
        remain = dummy->val / 10;
        dummy->val = dummy->val %10;

        if(l1!=NULL)
            l1 = (l1->next ==NULL)? NULL: l1->next;

        if(l2 !=NULL)
            l2 = (l2->next !=NULL)? l2->next: NULL;

        if(l1 != NULL || l2!=NULL || remain !=0)
        {
            dummy->next = malloc(sizeof(struct ListNode));
            dummy->next->next = NULL;
            dummy = dummy->next;
        }
    }
    return result;
}
