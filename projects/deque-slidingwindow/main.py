from collections import deque

# Fixed-size sliding window (drops oldest items automatically)
rolling_window = deque(maxlen=3)
for tick in [100.1, 100.2, 100.3, 100.4]:
    rolling_window.append(tick)
# rolling_window now holds: deque([100.2, 100.3, 100.4], maxlen=3)
print(rolling_window)

# O(1) Queue processing
q = deque([(0, "START")])
q.append((1, "PROCESS"))
timestamp, event = q.popleft()  # O(1) amortized, never O(N)
print("timestamp:", timestamp, ", event:", event)