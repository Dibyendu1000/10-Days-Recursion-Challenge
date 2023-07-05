def combinationsHelper(s, keyboard, res, temp):
    if (len(s) == 0):
        res.append(temp)
        return

    val = int(s[0])
    for i in range(len(keyboard[val])):
        combinationsHelper(s[1:], keyboard, res, temp+keyboard[val][i])


def combinations(s):

    # Write your code here
    keyboard = ['0', '1', 'abc', 'def', 'ghi',
                'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    res = []
    combinationsHelper(s, keyboard, res, '')
    return res
