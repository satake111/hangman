import random


def hangman():
    wordlist = ["dog","cat","rat","rabbit","lion",
            "micky","mouse","octopus","cow",
            "tiger","snake","horse","monkey","sheep",
            "chicken","boar","doragon"]
    length = len(wordlist)
    rr = random.randint(0, length + 1)
    word = wordlist[rr]
    wrong = 0
    stages = ["",
              "_______        ",
              "|              ",
              "|       |      ",
              "|       O      ",
              "|      /|\     ",
              "|      / \     ",
              "|              "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You win! The word was:")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You lose! The word was {}.".format(word))


hangman()
