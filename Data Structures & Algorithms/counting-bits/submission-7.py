class Solution:
    def countBits(self, n: int) -> List[int]:
        #range is [0, n]
        #makes a list of n + 1 zeros
        output = [0] * (n + 1)
        #loops thru arr
        for i in range(1, n + 1):
            # i >> 1 is i with its last bit dropped
            # output[i >> 1] loops up smaller number's count
            # i & 1 is the bit you dropped 1 or 0
            # add them, and thats the count for i
            output[i] = output[i >> 1] + (i & 1)
        return output
        