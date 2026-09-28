import heapq

# 1. Min-Heap for live order processing (earliest timestamp / lowest price)
orders = [(10.50, 101), (10.25, 102), (10.75, 103)]
heapq.heapify(orders)  # O(N) in-place
best_price, order_id = heapq.heappop(orders)
print(best_price, order_id)

max_heap = []
for val in [5, 1, 9, 3]:
    heapq.heappush(max_heap, -val)
largest = -heapq.heappop(max_heap)
print(largest)


# 3. K-Way Stream Merge: Merge multiple sorted trade logs
feed_a = [(1, "AAPL"), (5, "AAPL")]
feed_b = [(2, "GOOG"), (4, "GOOG"), (4, "AAPL")]
merged = list(heapq.merge(feed_a, feed_b, key=lambda x: x[0]))
print("merged", merged)
