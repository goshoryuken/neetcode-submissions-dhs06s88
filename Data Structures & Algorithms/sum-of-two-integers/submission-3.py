class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF  # 32-bit mask
        
        while b != 0:
            # XOR adds without carries, masked to 32 bits
            sum_without_carry = (a ^ b) & MASK
            # AND finds the carries, shifted left, masked to 32 bits
            carry = ((a & b) << 1) & MASK
            
            a = sum_without_carry
            b = carry
            
        # If 'a' is a negative number in 32-bit terms, 
        # convert it back to Python's signed integer format
        if a <= 0x7FFFFFFF:
            return a
        else:
            return ~(a ^ MASK)