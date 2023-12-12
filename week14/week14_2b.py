#偶數要對戰 n//2 場, 奇數則是 (n-1)//2 場
#持續比, 直到冠軍出來
#因為是淘汰賽,n隊的話,只要比n-1場,就淘汰其他隊, 就得冠暈了
class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n-1 