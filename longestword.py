class WordFinder:
    def find_longest_word(self, sentence: str) -> tuple[str, int]:
        """
        Finds and returns the longest word and its length from a given sentence.
        """
        # Clean special characters if needed, or split directly by whitespace
        words = sentence.split()

        if not words:
            return "", 0

        # Find word with maximum length
        longest_word = max(words, key=len)

        return longest_word, len(longest_word)


# --- Example Usage ---
if __name__ == "__main__":
    finder = WordFinder()

    text = "The quick brown fox jumps over the lazy dog"
    word, length = finder.find_longest_word(text)

    print(f"Sentence: '{text}'")
    print(f"Longest Word: '{word}'")
    print(f"Length: {length}")
