class Node(object):
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

class Solution:
  def mergeTwoLists(self, a, b):
    if a is None:
        return b
    elif b is None:
        return a
    elif a.val<b.val:
        #ha az a kisebb mint a b akkor az a van előbb tehát a-t adom vissza
        #aztán megnézem, hogy a következő a hol helyezkedik el
        a.next=self.mergeTwoLists(a.next,b)
        return a
    elif a.val>b.val:
        b.next=self.mergeTwoLists(a,b.next)
        return b
            
      

a = Node(1)
a.next = Node(3)
a.next.next = Node(5)

b = Node(2)
b.next = Node(4)
b.next.next = Node(6)

c = Solution().mergeTwoLists(a, b)
while c:
  print(c.val)
  c = c.next