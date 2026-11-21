def findMode(items: list):
    if not items:
        return 0

    freq = {}
    sort_items = sorted(items)
    for item in sort_items:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    max_count = max(freq.values())

    if max_count == 1:
        return 0  # ​No Mode
    else:
        modes = [key for key, count in freq.items() if count == max_count]

        if len(modes) == 1:
            return modes[0]  # Single Mode
        else:
            return modes     # Multi Mode