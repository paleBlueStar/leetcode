class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0; head = ListNode(None)
        p = head                        #初始化变量，head新链表头，p哨兵指针，carry记录进位
        while l1 or l2:
                if l1== None: l1val = 0 #如果l1或者l2先用尽，用零填充
                else:
                    l1val = l1.val
                if l2 == None:l2val = 0
                else:
                    l2val = l2.val
                sum = l1val + l2val + carry 
                carry = 0
                if sum >= 10:         #判断是否需要进位
                    carry = 1
                    sum -= 10
                p.next = ListNode(sum)
                p = p.next
                if l1 != None:l1 = l1.next
                if l2 != None:l2 = l2.next 
        if carry == 1:              #可能会出现相加多一位的情况  比如99+99 = 1,98的情况
            p.next = ListNode(1)
        return head.next
