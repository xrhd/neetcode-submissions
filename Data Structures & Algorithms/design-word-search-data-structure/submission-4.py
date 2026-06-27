class Node():
    def __init__(self):
        self.chars = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.chars:
                curr.chars[c] = Node()
            curr = curr.chars[c]
        curr.is_word = True
        

    def search(self, word: str) -> bool:
        def dfs(word, root):
            curr = root
            for i, c in enumerate(word):
                # print(curr.chars)
                if c == '.':
                    for node in curr.chars.values():
                        if dfs(word[i+1:], node):
                            return True
                    return False      
                elif c not in curr.chars:
                    return False
                else:
                    curr = curr.chars[c]
            return curr.is_word
        
        return dfs(word, self.root)