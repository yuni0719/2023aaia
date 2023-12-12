#把字串.join()起來, 看他們是否相同
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        a = ''.join(word1) #課本第2章的字串, 有教 .split() 和 .join()
        b = ''.join(word2) #單單.join(word2)

        if a==b: return True #兩字相同, 就True成功了
        else: return False #否則, 就失敗  