def isEquationSolvable(words, charToDig, digToChar, totalRows, totalCols, r=0, c=0, bal=0):
    # All chars have been visited
    if (c == totalCols):
        return bal == 0

    # First char of every word has been visited
    if (r == totalRows):
        # And last letter of equation is 0, i.e., satisfies equation. So we progress to next letter of first word
        # with balance divided by 10, to check for previous digit of balance's validity
        return (bal % 10 == 0 and isEquationSolvable(words, charToDig, digToChar, totalRows, totalCols, 0, c+1, bal//10))

    # Get the word at rth index
    word = words[r]

    # If there are no more chars left in current word
    if (c >= len(word)):
        # We progress to move to same position of next word
        return isEquationSolvable(words, charToDig, digToChar, totalRows, totalCols, r+1, c, bal)

    # We start checking with last character of each word, since we check validity of balance from last digit to
    # first digit trying to check if they are zero, and this satisfying equation
    char = word[len(word)-1-c]
    sign = 0

    # If substract the value from balance only if we are at the last word, i.e., the result,
    # since that is to be substracted from left hand sum to make it zero
    if (r < totalRows - 1):
        sign = 1
    else:
        sign = -1

    if ((char in charToDig) and (charToDig[char] != 0 or (charToDig[char] == 0 and len(word) == 1) or c != len(word)-1)):
        return isEquationSolvable(words, charToDig, digToChar, totalRows, totalCols, r+1, c, bal+sign*charToDig[char])
    else:
        for i in range(10):
            if ((digToChar[i] == None) and (i != 0 or (i == 0 and len(word) == 1) or c != len(word)-1)):
                digToChar[i] = char
                charToDig[char] = i

                x = isEquationSolvable(
                    words, charToDig, digToChar, totalRows, totalCols, r+1, c, bal + sign*charToDig[char])
                if (x):
                    return x
                digToChar[i] = None
                if (char in charToDig):
                    del charToDig[char]
        return False


def isSolvable(m, words, result):
    # Write your code here.
    words.append(result)
    totalRows = len(words)
    totalCols = len(max(words, key=lambda x: len(x)))
    charToDig = dict()
    digToChar = [None]*10

    return isEquationSolvable(words, charToDig, digToChar, totalRows, totalCols)
