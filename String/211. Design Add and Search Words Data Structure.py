class WordDictionary:

    def __init__(self):
        self.dic = defaultdict(set)
        

    def addWord(self, word: str) -> None:
        self.dic[len(word)].add(word)
        

    def search(self, word: str) -> bool:
        if '.' not in word:
            return word in self.dic[len(word)]
        for c in self.dic[len(word)]:
            for index, ch in enumerate(word):
                if ch != c[index] and ch != '.':
                    break
            else:
                return True

        return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
