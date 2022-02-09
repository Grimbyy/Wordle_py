import random

global word_list
word_list = []

with open('words.txt', 'r') as words:
    word_list = words.read().split('\n')
    #print(word_list)

def todays_seed():
    from datetime import datetime
    return (datetime.now().year*10000)+(datetime.now().month*100)+(datetime.now().day)

if __name__ == '__main__':

    winner = False

    random.seed(todays_seed())

    selection = int(random.random() * len(word_list))
    selection = word_list[selection]

    answer_builder = ['', '', '', '', '', '']
    while not winner:
        guess = input('Guess the word: ')
        if guess == "exit":
            print("UNLUCKY word was:", selection)
            break
        if len(guess) != len(selection):
            print('6 letters please')
            continue
        if guess == selection:
            print("Correct")
            winner = True
        else:
            letters_correct = 0
            correct_letters_list = []

            correct_positioned_letters = []
            for index, letter in enumerate(guess):
                if selection[index] == letter:
                    correct_positioned_letters.append(letter)
                    answer_builder[index] = letter
                    continue
                if letter in selection:
                    correct_letters_list.append(letter)
                    letters_correct+=1
            print("orange letters:", correct_letters_list,"green letters:", correct_positioned_letters)
            print("built answer: ", answer_builder)

    if winner: print("YOU'RE A WINNER THANKS FOR PLAYING!")