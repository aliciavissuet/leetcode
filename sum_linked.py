#1-2-3 + 4-5-6 = 321 + 654
#naive solution
def sum_linked(node1, node2):
    num1 = ''
    num2 = ''
    while node1:
        num1 = node1.val + num1
        node1 = node1.next
    while node2:
        num2 =node2.val + num2
        node2 = node2.next
    num1 = int(num1)
    num2 = int(num2)
    return sum(num1, num2)
# node1 will be the top value in the addition
def linked_sum(node1, node2):
    total = ''
    while node1 or node2:
        if node1 and node2:
            sum_of_curr_nodes = node1.val + node2.val
            if sum_of_curr_nodes < 10:
                total = str(sum_of_curr_nodes) + total
            else:
                #only take ones digit
                total = str(sum_of_curr_nodes % 10) + total
                # add the carry over to the next node1
                node1.next.val += sum_of_curr_nodes // 10
            node1 = node1.next
            node2 = node2.next
        else if node1:
            sum_of_curr_nodes = node1.val 
            if sum_of_curr_nodes < 10:
                total = str(sum_of_curr_nodes) + total
            else:
                #only take ones digit
                total = str(sum_of_curr_nodes % 10) + total
                # add the carry over to the next node1
                node1.next.val += sum_of_curr_nodes // 10
            node1 = node1.next
        else if node2:
            sum_of_curr_nodes = node2.val 
        
            if sum_of_curr_nodes < 10:
                total = str(sum_of_curr_nodes) + total 
            else:
                #only take ones digit
                total = str(sum_of_curr_nodes % 10) + total 
                # add the carry over to the next node1
                node2.next.val += sum_of_curr_nodes //10 
            node2 = node2.next
    return int(total)

def recurse_linked_sum(node1, node2, carry=0):
    value = carry
    if not node1 and not node2:
        return None
    else if node1.val is not None:
        value += node1.val 
    else if node2.val is not None:
        value += node2.val
    else if value > 9:
        carry = value //10
        value = value % 10
        
    return recurse_linked_sum(node1.next ? node1.next: None, node2.next ? node2.next: None, carry) + str(value)
    
    
def recurse_link_forward(node1, node2, carry):
    #padding to shorter number first
    length_1 = 0
    length_2 = 0

    while(node1):
        length_1 +=1
        node1 = node1.next
    while(node2):
        length_2 +=1
        node2 = node2.next 
    
    if length_1 < length_2:
        diff = length_2 - length_1 - 1
        # add nodes with 0 to beginning of node1
        
        newHead = new Node(0)
        newHead1 = newHead
        while diff > 0:
            newHead1.next = new Node(0)
            newHead1 = newHead1.next
        newHead1.next = node1
        node1 = newHead
    if length_2 < length_1:
        diff = length_1 - length_2 - 1
        # add nodes with 0 to beginning of node1
        
        newHead = new Node(0)
        newHead1 = newHead
        while diff > 0:
            newHead1.next = new Node(0)
            newHead1 = newHead1.next
        newHead1.next = node2
        node2 = newHead


def recurse_linked_sum_helper(node1, node2, carry=0):
    value = carry
    if not node1 and not node2:
        return None
    else if node1.val is not None:
        value += node1.val
    else if node2.val is not None:
        value += node2.val
    else if value > 9:
        carry = value // 10
        value = value % 10

    return str(value) + recurse_linked_sum(node1.next ? node1.next: None, node2.next ? node2.next: None, carry)
