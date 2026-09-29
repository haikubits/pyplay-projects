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
        