import random

class SecretWord:
    def __init__(self, word):
        self.word = word.lower()

    def contains(self, letter):
        return letter.lower() in self.word

    def masked(self, guessed_letters):
        display = []
        for char in self.word:
            if char in guessed_letters:
                display.append(char)
            else:
                display.append("_")
        return " ".join(display)

    def is_revealed(self, guessed_letters):
        for char in self.word:
            if char not in guessed_letters:
                return False
        return True


class HangmanGame:
    def __init__(self, secret_word, max_errors=6):
        self.secret_word = secret_word
        self.max_errors = max_errors
        self.guessed_letters = []
        self.errors = 0

    def guess(self, letter):
        letter = letter.lower()
        if letter in self.guessed_letters:
            return "repeated"
        
        self.guessed_letters.append(letter)

        if self.secret_word.contains(letter):
            return "correct"
        else:
            self.errors += 1
            return "wrong"

    def is_won(self):
        return self.secret_word.is_revealed(self.guessed_letters)

    def is_lost(self):
        return self.errors >= self.max_errors


class Game:
    def __init__(self, words_list):
        self.words_pool = list(set(words_list))

    def start_round(self):
        if not self.words_pool:
            return None
        word = self.words_pool.pop(random.randrange(len(self.words_pool)))
        secret = SecretWord(word)
        return HangmanGame(secret)


def main():
    words = ["banana", "apple", "letter", "orange", "python", "window", "computer", "puzzle"]
    game_manager = Game(words)

    playing = True
    while playing:
        current_game = game_manager.start_round()
        if current_game is None:
            print("All words have been played!")
            break

        while not current_game.is_won() and not current_game.is_lost():
            print(f"Word: {current_game.secret_word.masked(current_game.guessed_letters)}")
            print(f"Errors remaining: {current_game.max_errors - current_game.errors}")
            
            raw_input = input("Enter a letter: ")
            cleaned_input = raw_input.strip()

            if len(cleaned_input) != 1 or not cleaned_input.isalpha():
                print("Invalid input. Please enter a single letter.")
                continue

            result = current_game.guess(cleaned_input)

            if result == "correct":
                print("The letter is in the word!")
            elif result == "wrong":
                print("The letter is not in the word.")
            elif result == "repeated":
                print("You have already guessed this letter.")

        print(f"Word: {current_game.secret_word.masked(current_game.guessed_letters)}")
        
        if current_game.is_won():
            print(f"You won! The word was {current_game.secret_word.word}.")
        else:
            print(f"You lost! The word was {current_game.secret_word.word}.")

        choice = input("Would you like to play another round? (y/n): ").strip().lower()
        if choice != 'y':
            playing = False

if __name__ == "__main__":
    main()
