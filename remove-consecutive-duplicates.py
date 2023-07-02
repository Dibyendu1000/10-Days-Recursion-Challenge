def removeDuplicateHelper(n, sList, i):
    if (i == n-1):
        # Since this is performed only once, Time Complexity remains O(n)
        nullRemovedS = [i for i in sList if (i != None)]
        return ''.join(nullRemovedS)

    if (sList[i] == sList[i+1]):
        # Could have used slicing here, but that would be O(n)
        # So we do it at end result, to prevent repeated O(n) operations
        sList[i] = None

    return removeDuplicateHelper(n, sList, i+1)


def removeDuplicate(n, s):
    # As 0 or 1 length strings can't have duplicates
    res = s
    if (len(s) > 1):
        # Since string is immutable and Lists are mutable, so assignment in Lists
        # can be done in O(1) Time Complexity
        sList = list(s)
        res = removeDuplicateHelper(n, sList, 0)
    return res
