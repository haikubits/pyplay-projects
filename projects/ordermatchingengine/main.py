import heapq
from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class Trade:
    buyer_id: str
    seller_id: str
    price: float
    quantity: int

class OrderMatchingEngine:
    
    def __init__(self):
        self.asks: List[Tuple] = []
        self.bids: List[Tuple] = []
        
        self.order_sequence = 0
        self.active_orders = {}
    
    def add_order(self, client_id: str, side: str, price: float, quantity: int) -> Tuple[int, List[Trade]]:
        self.order_sequence += 1
        order_id = self.order_sequence
        self.active_orders[order_id] = True
        trades: List[Trade] = []
        
        if side.upper() == "BUY":
            # check for any matching orders on top of the heap, (first purge inactive orders) if found, match quantities and execute it fully or partially. Add Trade object to the trades list. If order book ask was completely covered by this order, then boot it out of the heap and also mark it as inactive, otherwise simply subtract the quantity. Also if the incoming order couldn't fully execute, then push it on the BUY heap i.e. bids.