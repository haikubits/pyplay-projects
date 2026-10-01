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
        # Min-Heap for Asks: (price, timestamp, order_id, quantity, client_id)
        self.asks: List[Tuple] = []
        
        # Max-Heap for Bids: (-price, timestamp, order_id, quantity, client_id)
        self.bids: List[Tuple] = []
        
        self.order_sequence = 0
        self.active_orders = {}
    
    def _purge_inactive(self, heap: List[Tuple]) -> None:
        while heap and not self.active_orders.get(heap[0][2], False):
            heapq.heappop(heap)

    def add_order(self, client_id: str, side: str, price: float, quantity: int) -> Tuple[int, List[Trade]]:
        self.order_sequence += 1
        order_id = self.order_sequence
        self.active_orders[order_id] = True
        trades: List[Trade] = []
        
        if side.upper() == "BUY":
            # check for any matching orders on top of the heap, (first purge inactive orders) if found, match quantities and execute it fully or partially. Add Trade object to the trades list. If order book ask was completely covered by this order, then boot it out of the heap and also mark it as inactive, otherwise simply subtract the quantity. Also if the incoming order couldn't fully execute, then push it on the BUY heap i.e. bids.
            while self.asks and quantity>0:
                self._purge_inactive(self.asks)
                if not self.asks:
                    break
                
                best_ask_price, _, ask_order_id, ask_order_quantity, ask_order_client_id = self.asks[0]
                
                if price < best_ask_price:
                    break
                qty_filled = min(quantity, ask_order_quantity)
                quantity -= qty_filled
                trades.append(Trade(client_id, ask_order_client_id, best_ask_price, qty_filled))
                if qty_filled == ask_order_quantity:
                    heapq.heappop(self.asks)
                    self.active_orders[ask_order_id] = False
                else:
                    self.asks[0][3] -= qty_filled
            
            # if no qualifying asks remain that can completely fill the order, push the remaining quantity on the bids heap
            if quantity > 0:
                heapq.heappush(self.bids, (-price, self.order_sequence, order_id, quantity, client_id))
        elif side.upper() == "SELL":
            while self.bids and quantity > 0:
                self._purge_inactive(self.bids)
                if not self.bids:
                    break
                
                best_bid_price, _, bid_order_id, bid_order_qty, bid_order_client_id = self.bids[0]
                
                if price > -best_bid_price:
                    break
                
                qty_filled = min(quantity, bid_order_qty)
                quantity -= qty_filled
                trades.append(Trade(bid_order_client_id, client_id, -best_bid_price, qty_filled))
                if qty_filled == bid_order_qty:
                    heapq.heappop(self.bids)
                    self.active_orders[bid_order_id] = False
                else:
                    self.bids[0][3] -= qty_filled
            if quantity > 0:
                heapq.heappush(self.asks, (price, self.order_sequence, order_id, quantity, client_id))
        
        return order_id, trades
    
    def cancel_order(self, order_id: int) -> bool:
        if order_id in self.active_orders and self.active_orders[order_id]:
            self.active_orders[order_id] = False
            return True
        return False

# --- Toy Simulation Test Harness ---
if __name__ == "__main__":
    engine = OrderMatchingEngine()

    print("Submitting Resting Limit Orders:")
    # Ask: Sell 100 @ $10.50
    id1, _ = engine.add_order("Trader_A", "SELL", 10.50, 100)
    print(f"  Order {id1}: Trader_A rests SELL 100 @ $10.50")

    # Ask: Sell 50 @ $10.45 (Better price than A)
    id2, _ = engine.add_order("Trader_B", "SELL", 10.45, 50)
    print(f"  Order {id2}: Trader_B rests SELL 50 @ $10.45")

    # Cancel Trader_B's order to test tombstone handling
    engine.cancel_order(id2)
    print(f"  Order {id2} (Trader_B) cancelled.")

    # Aggressive Bid: Buy 120 @ $10.55 (Crosses the spread)
    print("\nSubmitting Aggressive Order Crossing Spread:")
    id3, fills = engine.add_order("Trader_C", "BUY", 10.55, 120)
    print(f"  Order {id3}: Trader_C attempts BUY 120 @ $10.55")

    for trade in fills:
        print(f"  >>> EXECUTION: {trade.quantity} shares @ ${trade.price:.2f} "
              f"(Buyer: {trade.buyer_id}, Seller: {trade.seller_id})")

    # Examine remaining book: Trader_C should have 20 shares remaining on Bid side
    print(f"\nRemaining Resting Top Bid: {-engine.bids[0][0]} Qty: {engine.bids[0][3]} by {engine.bids[0][4]}")