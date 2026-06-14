class Solution:
    
    # dic = {}
    def encode(self, strs: List[str]) -> str:
        ens = ""
        for s in strs:
            ens += str(len(s)) + "#" + s
        print(ens)
        return ens

    def decode(self, s: str) -> List[str]:
        strs, i = [], 0
        print("input string: ", s)
        while i < len(s):
            j = i
            # if i >= len(s):
            #     break
            print(i, j)
            print(s[0])
            while j < len(s) and s[j] != "#":
                print("In loop:", s[0])
                j += 1
            print(i, j)
            length = int(s[i:j])
            print(length)
            i = j + 1
            j = length + i
            strs.append(s[i:j])
            i = j
        return strs