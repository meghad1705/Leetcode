class Solution(object):
    def divide(self, dividend, divisor):
        # Handle overflow edge case
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)
        
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine sign of result
        negative = (dividend < 0) != (divisor < 0)
        
        # Work with positive values
        a = abs(dividend)
        b = abs(divisor)
        
        result = 0
        
        while a >= b:
            temp = b
            multiple = 1
            
            # Double temp until it exceeds a
            while a >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            
            a -= temp
            result += multiple
        
        if negative:
            return -result
        return min(result, INT_MAX)
