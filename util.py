class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a if len(a) >= len(b) else ('0'*(len(b) - len(a))) + a
        b = b if len(b) >= len(a) else ('0'*(len(a) - len(b))) + b

        print(a, b)

        i = len(a)-1
        carry = '0'
        out = ''
        while i > -1:
            if carry == '1':
                if a[i]=='1' and b[i]=='1':
                    out = '1' + out
                    carry = '1'
                elif a[i]=='1' or b[i]=='1':
                    out = '0' + out
                    carry = '1'
                else:
                    out = '1' + out
                    carry = '0'
                print('------',out)
            else:
                if a[i]=='1' and b[i]=='1':
                    out = '0' + out
                    carry = '1'
                elif a[i]=='1' or b[i]=='1':
                    out = '1' + out
                    carry = '0'
                else:
                    out = '0' + out
                    carry = '0'
                print('======',out)
            i -= 1

        return carry + out if carry == '1' else out

obj = Solution()
a = "1010" 
b = "1011"
x = obj.addBinary(a, b)
print(x)