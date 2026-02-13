import random



# Function to check if the guessed letter is in the word
# Updates the word_completion list and correct_guess flag accordingly
def update_completion(word, guess, word_completion):

    for index, letter in enumerate(word):
        if guess == letter:
            word_completion = word_completion[:index] + letter + word_completion[index + 1:]

    return word_completion



def guess_letter(guess_list):
    letter = input("Guess a letter: ")
    #verify if letter was already guessed
    while letter in guessed_letters:
        print("You already guessed the letter. Try again.")
        letter = input("Guess a letter: ")

    letter = letter.lower()
    guess_list.append(letter)
    return letter

def word_completion_show (word_completion):
    printable = ""
    for letter in word_completion:
        printable += f"{letter} "

    print(printable)



#Ascci art
from hangman_art import stages, logo

#word library
from hangman_words import word_list


word = random.choice(word_list)
guessed_letters = []
lives = 6
word_completion = "_" * len(word)

print(logo)
word_completion_show(word_completion)

while lives > 0 and word_completion != word:

    guess = guess_letter(guessed_letters)

    clear()

    #Guessing the whole word
    if len(guess) > 1:
        if guess == word:
            word_completion = word
            break
        else:
            lives -= 1
            print(f"Wrong guess! You lose a life.")
            print(f"You have {lives} lives left.")
            continue

    if(guess in word):
        #Correct guess
        word_completion = update_completion(word, guess, word_completion)
        print(f"Good job! Letter {guess} is in the word.")


    else:
        #Incorrect guess
        lives -= 1
        print(f"Letter {guess} is not in the word. You lose a life.")
        print(f"You have {lives} lives left.")


    word_completion_show(word_completion)
    print(stages[lives])

#Game ended
if lives == 0:
    print(f"You lost! The word was {word}.")
else:
    print("Congratulations! You guessed the word: {word}.")