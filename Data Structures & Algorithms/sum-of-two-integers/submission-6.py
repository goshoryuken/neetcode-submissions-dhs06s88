class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF

        while b != 0:

            add_without_carry = (a ^ b) & mask
            carry_out = ((a & b) << 1) & mask

            a = add_without_carry
            b = carry_out

        if a <= 0x7FFFFFFF:
            return a
        else:
            return ~(a ^ mask)