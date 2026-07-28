class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = 0

        i = 0 
        while (i < len(chars)):
            count = 1
            # a a a b b b b
            # a 3 b 4 
            while (i + count < len(chars) and chars[i+count] == chars[i]):
                count += 1

            chars[ans] = chars[i]
            ans += 1
            if count != 1:
                for c in str(count):
                    chars[ans] = c
                    ans +=1
            i+= count
        return ans




        