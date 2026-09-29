# Sliding window real time VWAP calculator

from collections import deque, defaultdict
from typing import Optional

class SlidingWindowVWAP:
    
    def __init__(self, window_ms: int):
        self.window_ms = window_ms
        
        self._symbols_queues: dict[str, deque] = defaultdict(deque)
        self._rolling_dollar_volume: dict[str, float] = defaultdict(float)
        self._rolling_volume: dict[str, int] = defaultdict(int)
        
    def _evict_stale_ticks(self, symbol: str, current_ts: int) -> None:
        q = self._symbols_queues[symbol]
        cutoff = current_ts - self.window_ms
        
        while q and q[0][0] <= cutoff:
            ts, price, volume = q.popleft()
            self._rolling_dollar_volume -= price*volume
            self._rolling_volume -= volume
        
        if not q:
            del self._symbols_queues[symbol]
            del self._rolling_dollar_volume[symbol]
            del self._volume[symbol]
    
    def add_tick(self, timestamp_ms: int, symbol: str, price: float, volume: int) -> None:
        if volume <= 0:
            return
        
        # First evict stale ticks, then add the new tick
        self._evict_stale_ticks(symbol, timestamp_ms)
        
        self._symbols_queues[symbol].append((timestamp_ms, price, volume))
        self._rolling_dollar_volume += price*volume
        self._rolling_volume += volume
    
    def get_vwap(self, symbol: str, current_time_ms: int) -> Optional[float]:
        if symbol not in self._symbols_queues:
            return None
        
        self._evict_stale_ticks(symbol, current_time_ms)
        total_volume = self._rolling_volume.get(symbol, 0)
        if total_volume == 0:
            return None
        return self._rolling_dollar_volume[symbol] / total_volume

# --- Toy Simulation Test Harness ---
if __name__ == "__main__":
    # 5-second sliding window (5000 ms)
    vwap_tracker = SlidingWindowVWAP(window_ms=5000)

    ticks = [
        (1000, "AAPL", 150.0, 100),   # 1000ms: AAPL @ 150 (vol: 100) -> $15,000
        (2000, "AAPL", 152.0, 200),   # 2000ms: AAPL @ 152 (vol: 200) -> $30,400
        (3000, "MSFT", 400.0, 50),    # 3000ms: MSFT tick
        (6500, "AAPL", 155.0, 100),   # 6500ms: AAPL @ 155 (vol: 100) -> $15,500
                                      # At 6500ms, tick at 1000ms (1000 <= 6500 - 5000 = 1500) has expired.
    ]

    for ts, sym, px, vol in ticks:
        vwap_tracker.add_tick(ts, sym, px, vol)
        current_vwap = vwap_tracker.get_vwap(sym, ts)
        print(f"Time: {ts}ms | {sym} Tick: {vol} @ ${px:.2f} | Running VWAP: ${current_vwap:.2f}")

    # Query after idle time has passed
    query_time = 7500  # 7500 - 5000 = 2500 -> Tick at 2000ms is now also expired
    aapl_vwap = vwap_tracker.get_vwap("AAPL", query_time)
    print(f"\nTime: {query_time}ms | AAPL Late Query VWAP: ${aapl_vwap:.2f} (Only tick at 6500 remains)")
        
            