def kthChildNthGeneration(n, k):
    # If we need the 1st child or 1st Gen child, it is always Male, given the family structure
    if (n == 1 or k == 1):
        return 'Male'

    # To find the parent of ith child
    parent = (k+1)//2

    if (kthChildNthGeneration(n-1, parent) == 'Male'):
        # If Parent is Male, first child is male & second child is female
        if (k & 1):
            return 'Male'
        else:
            return 'Female'
    else:
        # If Parent is Female, first child is female & second child is male
        if (k & 1):
            return 'Female'
        else:
            return 'Male'
