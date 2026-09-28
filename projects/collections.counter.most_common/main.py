#https://leetcode.com/problems/top-k-frequent-elements

import collections
nums = [1,1,1,2,2,3]
k = 2
# Optimized C implementation that uses heapq.nlargest
print(collections.Counter(nums).most_common(k))