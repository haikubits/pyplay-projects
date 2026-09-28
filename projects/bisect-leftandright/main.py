import bisect

# Lookup closest historical quote <= query_time
timestamps = [100, 200, 300, 400]
query_time = 200

idx_left = bisect.bisect_left(timestamps, query_time)
idx = bisect.bisect_right(timestamps, query_time) - 1
if idx >= 0:
    matched_ts_right = timestamps[idx]  # 200
if idx_left >= 0:
    matched_ts_left = timestamps[idx_left]

print("matched_ts_left:", matched_ts_left)
print("matched_ts_right:", matched_ts_right)