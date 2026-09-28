def merge_intervals(intervals: list[list[int]]) ->  list[list[int]]:
    if not intervals:
        return []
    
    intervals.sort(key = lambda x: x[0])
    merged = [intervals[0]]
    
    for start, end in intervals[1:]:
        last_end = merged[-1][1]
        if start < last_end:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])    
    return merged

input_intervals = [[2, 6], [1, 3], [7, 10], [9, 11], [14, 20]]
print(merge_intervals(input_intervals))

