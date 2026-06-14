class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = []

        mape = {}
        for s in strs:
            # print(f"the string is: {s}")
            alpha = [0] * 26
            for c in s:
                alpha[ord(c) - ord("a")] += 1
            # print(f"the alphabet string is: {alpha}")
            if tuple(alpha) not in mape:
                mape[tuple(alpha)] = [s]
            else:
                mape[tuple(alpha)].append(s)
            # print(f"the hash map would be: {mape}")

        for values in mape.values():
            ret.append(values)
            # print(f"the return array is: {ret}")
        return ret