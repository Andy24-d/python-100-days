import random

# Function to check if the guessed letter is in the word
# Updates the word_completion list and correct_guess flag accordingly
def update_completion(word, guess, word_completion):

    for index, letter in enumerate(word):
        if guess == letter:
            word_completion = word_completion[:index] + letter + word_completion[index + 1:]

    return word_completion





def guess_letter():
    letter = input("Guess a letter: ")
    #verify if letter was already guessed
    while letter in guessed_letters:
        print("You already guessed the letter. Try again.")
        letter = input("Guess a letter: ")

    letter = letter.lower()
    guessed_letters.append(letter)
    return letter

def word_completion_show (word_completion):
    for letter in word_completion:
        printable = letter + " "

    print(printable)



list = ["python", "java", "kotlin", "javascript"]

word = random.choice(list)
guessed_letters = []
lives = 6
word_completion = "_" * len(word)

while lives > 0 and word_completion != word:

    guess = guess_letter()

    if(guess in word):
        #Correct guess
        word_completion = update_completion(word, guess, word_completion)
        print(f"Good job! Letter {guess} is in the word.")


    else:
        #Incorrect guess
        lives -= 1
        print(f"Letter {guess} is not in the word. You lose a life.")
        print(f"You have {lives} lives left.")

    print(word_completion)
    word_completion_show(word_completion)

#Game ended
if lives == 0:
    print(f"You lost! The word was {word}.")
else:
    print("Congratulations! You guessed the word.")