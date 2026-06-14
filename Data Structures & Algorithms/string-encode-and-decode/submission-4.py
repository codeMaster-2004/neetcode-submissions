class Solution:
    
    def encode(self, strs: List[str]) -> str:
        st = ""
        for s in strs:
            st += f"{len(s)}$%{s}"
        return st
        
    def decode(self, s: str) -> List[str]:
        print(f"decode string: {s}")
        ret = []
        while s:
            count = 0
            if s[0].isdigit():
                pos = s.find("$%")
                count = int(s[0:pos])
                st = s[pos+2: pos+2+count]
                ret.append(st)
                s = s[pos+2+count:]
                print(f"count is: {count}")
                print(f"pos is: {pos}")
                print(f"st is: {st}")
                print(f"ret is: {ret}")
            else:
                return s
        return ret
        # for i in range(len(s)):
            
                