class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.word_count = 0  # Лічильник слів, що закінчуються на даному вузлі

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def put(self, word, index):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.word_count += 1  # Інкрементуємо лічильник на кінцевому вузлі

    def get(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
        return node if node.is_end_of_word else None

class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:
        if not strings:
            return ""
        
        # Перевірка чи всі елементи масиву рядки
        if any(not isinstance(s, str) for s in strings):
            raise ValueError("All elements of the input list must be strings.")
        
        # Пошук спільного префікса
        prefix = strings[0]
        for string in strings[1:]:
            # Поступово обрізаємо префікс, поки він не збігається з поточним словом
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix


# Тестування класу LongestCommonWord
if __name__ == "__main__":
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""
