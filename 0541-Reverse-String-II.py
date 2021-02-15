class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        size = len(s)
        output_str = ""
        i = 0
        while size - i*2*k >= 2*k:
            
            output_str += s[ i*2*k : i*2*k+k ][::-1] + s[ i*2*k+k : (i+1)*2*k ]
            i += 1
        if size - i*2*k < k:
            output_str += s[ i*2*k : ][::-1]
        else:
            output_str += s[ i*2*k : i*2*k+k ][::-1] + s[ i*2*k+k : ]
        return output_str
