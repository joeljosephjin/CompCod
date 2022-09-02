
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def lst_to_ll(lst=[1,2,3]):
    cur = dummy = ListNode()
    for e in lst:
        cur.next = ListNode(val=e, next=None)
        cur = cur.next
    return dummy.next
  
dummy_ll = lst_to_ll()

def ll_to_lst(ll=dummy_ll):
    lst = []
    while ll:
      lst.append(ll.val)
      ll = ll.next
    return lst
  
dummy_lst = ll_to_lst()

print(dummy_lst)

if dummy_lst != [1,2,3]:
    raise Exception("Something wrong!")
