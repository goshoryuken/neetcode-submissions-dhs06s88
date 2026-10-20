class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF

        while b != 0:
            add_no_carry = (a ^ b) & mask
            carry = ((a & b) << 1) & mask

            a = add_no_carry
            b = carry

        if a <= 0x7FFFFFFF:
            return a
        else:
            return ~(a ^ mask)
        