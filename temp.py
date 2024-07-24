def binary_search(num, l):
    list = sorted(l)
    print(f"\n\nSorted - {list}\n\n")
    lo = 0
    hi = len(list) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        print(
            f"""
\n\nSearching between {list[lo]} and {list[hi]} and median is {list[mid]}\n\n
"""
        )
        if num > list[mid]:
            lo = mid + 1
        elif num < list[mid]:
            hi = mid - 1
        else:
            print(f"\n\n{num} is in the list\n\n")
            break


n = 12
l = [1, 23, 54, 753, 357, 377, 22, 23, 12, 325, 264, 37, 35, 78, 46, 48, 46]
print(f"\n\n{l}\n\n")
binary_search(n, l)
