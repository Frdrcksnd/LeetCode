def merge(intervals):
    intervals.sort(key=lambda x: x[0])

    result = []

    start, end = intervals[0]

    for s, e in intervals[1:]:
        if s <= end:
            end = max(end, e)
        else:
            result.append([start, end])
            start, end = [s, e]
    result.append([start, end])

    return result


"""
Time Complexity => O(n)
Space Complexity => O(n)
"""
