# Leetcode 1486: XOR Operations in an Array
def xorOperation(self, n, start):
    """
    :type n: int
    :type start: int
    :rtype: int
    """
    numList = []
    for i in range(n):
      numList.append(start + 2 * i)

    return reduce(lambda acc, cum: acc ^ cum, numList, 0)
