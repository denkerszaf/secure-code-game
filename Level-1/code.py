'''
////////////////////////////////////////////////////////////
///                                                      ///
///   0. tests.py is passing but the code is vulnerable  /// 
///   1. Review the code. Can you spot the bug?          ///
///   2. Fix the code but ensure that tests.py passes    ///
///   3. Run hack.py and if passing then CONGRATS!       ///
///   4. If stucked then read the hint                   ///
///   5. Compare your solution with solution.py          ///
///                                                      ///
////////////////////////////////////////////////////////////
'''

from collections import namedtuple

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

MAX_QUANTITY = 1000
MAX_PAYMENT = 10e6
MAX_AMOUNT = 100000

def validorder(order: Order):
    net = 0.0
    
    for item in order.items:
        if item.type == 'payment':
            net += max(min(item.amount,MAX_PAYMENT),-1 * MAX_PAYMENT) 
        elif item.type == 'product':
            if (item.quantity < MAX_QUANTITY and item.amount < MAX_AMOUNT):
                net -= item.amount * item.quantity
        else:
            return("Invalid item type: %s" % item.type)
    
    if net != 0.0:
        return("Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net))
    else:
        return("Order ID: %s - Full payment received!" % order.id)
