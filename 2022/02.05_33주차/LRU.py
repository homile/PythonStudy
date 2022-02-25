# LRU 알고리즘

Number = [1, 4, 5, 8, 3, 4, 3]
cache_size = 3
cache = []
for data in Number:
    if data not in cache:
        # cache miss
        if len(cache) < cache_size:
            cache.append(data)
        else:
            cache.pop(0)
            cache.append(data)
    # cache hit
    else:
        cache.remove(data)
        cache.append(data)
    print(cache)

# [1]
# [1, 4]
# [1, 4, 5]
# [4, 5, 8]
# [5, 8, 3]
# [8, 3, 4]
# [8, 4, 3]