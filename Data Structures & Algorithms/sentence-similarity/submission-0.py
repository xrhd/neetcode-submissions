class Solution:
    def areSentencesSimilar(
        self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]
    ) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        sim = set()
        for a, b in similarPairs:
            sim.add((a, b))
            sim.add((b, a))

        for a, b in zip(sentence1, sentence2):
            if a == b:
                continue
            if (a, b) not in sim:
                return False

        return True
