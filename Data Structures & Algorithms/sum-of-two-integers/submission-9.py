class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF

        while b != 0:
            add_without_carry = (a ^ b) & MASK
            carry = ((a & b) << 1) & MASK

            a = add_without_carry
            b = carry

        if a < 0x7FFFFFFF:
            return a
        else:
            return ~(a ^ MASK)

        

        