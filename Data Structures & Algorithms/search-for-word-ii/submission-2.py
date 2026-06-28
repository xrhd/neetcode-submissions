class TrieNode:
    def __init__(self):
        self.child = {}
        self.word = None

    def insert(self, word):
        curr = self
        for c in word:
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
        curr.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.insert(word)


        def inbound(i, j):
            return (
                0 <= i and i < len(board) and 
                0 <= j and j < len(board[0])
            )

        res = set()
        def dfs(i: int, j: int, node, path: set):
            nonlocal res
            if not inbound(i, j) or (i, j) in path:
                return

            char = board[i][j]
            if char not in node.child:
                return

            path.add((i, j)) # visted
            node = node.child[char]
            if node.word:
                res.add(node.word)

            options = (
                (0, -1),
                (0, 1),
                (1, 0),
                (-1, 0),
            )
            for p, q in options:
                dfs(i + p, j + q, node, path)
            
            path.remove((i, j))

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, root, set())
        
        return list(set(res))
