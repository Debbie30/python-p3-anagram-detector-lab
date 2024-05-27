class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, possible_anagrams):
        def are_anagrams(word1, word2):
            return sorted(word1) == sorted(word2)
        
        matches = [anagram for anagram in possible_anagrams if are_anagrams(self.word, anagram)]
        return matches
# your code goes here!