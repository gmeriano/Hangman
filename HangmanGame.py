import random

three_word = ["cat", "dog", "key", "urn", "arm","hey","her","bop","zap","qis"]   
four_word = ["hawk","helm", "kilt", "legs", "ears", "fire","dent","turd","evil","than"]
five_word = ["chair", "chalk", "glove", "shard", "hairs","chase","field","cheat","guard"]
board_three = [["_"], ["_"], ["_"]]
le_word = [["_"], ["_"], ["_"]]
board_four = [["_"], ["_"], ["_"], ["_"]]
lm_word = [["_"], ["_"], ["_"], ["_"]]
board_five = [["_"], ["_"], ["_"], ["_"], ["_"]]
lh_word = [["_"], ["_"], ["_"], ["_"], ["_"]]

print "  WELCOME TO HANGMAN!"
print "  Game made by Gabriel Meriano"

def drawBoard(lives):

    if lives == 6:
        print ""
        print "  +---+"
        print "  |   |"
        print "      |"
        print "      |"
        print "      |"
        print "      |"
        print"  ========"
        print ""

    if lives == 5:
        print ""
        print "  +---+"
        print "  |   |"
        print "  O   |"
        print "      |"
        print "      |"
        print "      |"
        print"  ========"
        print ""

    if lives == 4:
        print ""
        print "  +---+"
        print "  |   |"
        print "  O   |"
        print "  |   |"
        print "      |"
        print "      |"
        print"  ========"
        print ""

    if lives == 3:
        print ""
        print "  +---+"
        print "   |  |"
        print "   O  |"
        print "  /|  |"
        print "      |"
        print "      |"
        print"  ========"
        print ""

    if lives == 2:
        print ""
        print "  +---+"
        print "   |  |"
        print "   O  |"
        print "  /|\ |"
        print "      |"
        print "      |"
        print"  ========"
        print ""

    if lives == 1:
        print ""
        print "  +---+"
        print "   |  |"
        print "   O  |"
        print "  /|\ |"
        print "  /   |"
        print "      |"
        print"  ========"
        print ""

    if lives == 0:
        print ""
        print "  +---+"
        print "   |  |"
        print "   X  |"
        print "  /|\ |"
        print "  / \ |"
        print "      |"
        print"  ========"
        print ""

difficulty = raw_input("  Select Difficulty! Easy, Medium, or Hard:  ")
if difficulty == "Easy":
    lives = 6
    drawBoard(lives)
    print "  The word you are trying to guess is below"
    print ""
    for row in board_three:
        print "  " + " ".join(row)
    e_word = random.choice(three_word)
    le_word[0] = e_word[0]
    le_word[1] = e_word[1]
    le_word[2] = e_word[2]

    def e_game():
        lives = 6
        turns = 6
        guessed = []
        correct = []
        incorrect = []
        while turns > 0:

            print ""
            char = raw_input("  Select a letter:  ")
            guessed.append(char)

            if char == e_word[0]:
                correct.append(char)
                board_three[0] = char
                print "  You guessed a letter!"
                print "  You have", turns, "turns left"
                print "  You have guessed", guessed
                print "  Correct guesses so far are", correct
                print "  Incorrect guesses so far are", incorrect
                print "  Your word is below"
                print ""
                for row in board_three:
                    print "  " + " ".join(row)

                drawBoard(lives)

                if board_three == le_word:
                    print ""
                    print "  YOU WIN!"
                    break
                
            elif char == e_word[1]:
                correct.append(char)
                board_three[1] = char
                print "  You guessed a letter!"
                print "  You have", turns, "turns left"
                print "  You have guessed", guessed
                print "  Correct guesses so far are", correct
                print "  Incorrect guesses so far are", incorrect
                print "  Your word is below"
                print ""

                drawBoard(lives)

                for row in board_three:
                    print "  " + " ".join(row)

                if board_three == le_word:
                    print ""
                    print "  YOU WIN!"
                    break
                    
            elif char == e_word[2]:
                correct.append(char)
                board_three[2] = char
                print "  You guessed a letter!"
                print "  You have", turns, "turns left"
                print "  You have guessed", guessed
                print "  Correct guesses so far are", correct
                print "  Incorrect guesses so far are", incorrect
                print "  Your word is below"
                print ""

                drawBoard(lives)

                for row in board_three:
                    print "  " + " ".join(row)

                if board_three == le_word:
                    print ""
                    print "  YOU WIN!"
                    break
                    
            else:
                incorrect.append(char)
                print "  You guessed incorrectly, you lose a life"
                turns = turns - 1
                lives = lives -1
                print "  You have", turns, "turns left"
                print "  You have guessed", guessed
                print "  Incorrect guesses so far are", incorrect
                print "  Correct guesses so far are", correct
                print "  Your word is below"
                print ""

                drawBoard(lives)

                for row in board_three:
                    print "  " + " ".join(row)
        else:
            print ""
            print "  You LOSE!"
            print "  The correct word was", e_word
    e_game()
            
            
        
elif difficulty == "Medium":
     lives = 6
     drawBoard(lives)

     print "  The word you are trying to guess is below"
     print ""
     for row in board_four:
        print "  " + " ".join(row)
     m_word = random.choice(four_word)
     lm_word[0] = m_word[0]
     lm_word[1] = m_word[1]
     lm_word[2] = m_word[2]
     lm_word[3] = m_word[3]
    
     def m_game():
        lives = 6
        turns = 6
        guessed = []
        correct = []
        incorrect = []
        while turns > 0:

            print ""
            char = raw_input("  Select a letter:  ")
            guessed.append(char)

            if char == m_word[0]:
                correct.append(char)
                board_four[0] = char
                print "  You guessed a letter!"
                print "  You have", turns, "turns left"
                print "  You have guessed", guessed
                print "  Correct guesses so far are", correct
                print "  Incorrect guesses so far are", incorrect
                print "  Your word is below"
                print ""

                drawBoard(lives)

                for row in board_four:
                    print "  " + " ".join(row)
                if board_four == lm_word:
                    print ""
                    print "  YOU WIN!"
                    break
                
            elif char == m_word[1]:
                correct.append(char)
                board_four[1] = char
                print "  You guessed a letter!"
                print "  You have", turns, "turns left"
                print "  You have guessed", guessed
                print "  Correct guesses so far are", correct
                print "  Incorrect guesses so far are", incorrect
                print "  Your word is below"
                print ""

                drawBoard(lives)

                for row in board_four:
                    print "  " + " ".join(row)
                if board_four == lm_word:
                    print ""
                    print "  YOU WIN!"
                    break
                    
            elif char == m_word[2]:
                correct.append(char)
                board_four[2] = char
                print "  You guessed a letter!"
                print "  You have", turns, "turns left"
                print "  You have guessed", guessed
                print "  Correct guesses so far are", correct
                print "  Incorrect guesses so far are", incorrect
                print "  Your word is below"
                print ""

                drawBoard(lives)

                for row in board_four:
                    print "  " + " ".join(row)
                if board_four == lm_word:
                    print ""
                    print "  YOU WIN!"
                    break
            elif char == m_word[3]:
                correct.append(char)
                board_four[3] = char
                print "  You guessed a letter!"
                print "  You have", turns, "turns left"
                print "  You have guessed", guessed
                print "  Correct guesses so far are", correct
                print "  Incorrect guesses so far are", incorrect
                print "  Your word is below"
                print ""

                drawBoard(lives)

                for row in board_four:
                    print "  " + " ".join(row)
                if board_four == lm_word:
                    print ""
                    print "  YOU WIN!"
                    break
                    
            else:
                incorrect.append(char)
                print "  You guessed incorrectly, you lose a life"
                turns = turns - 1
                lives = lives -1
                print "  You have", turns, "turns left"
                print "  You have guessed", guessed
                print "  Incorrect guesses so far are", incorrect
                print "  Correct guesses so far are", correct
                print "  Your word is below"
                print ""

                drawBoard(lives)

                for row in board_four:
                    print "  " + " ".join(row)
        else:
            print ""
            print "  You LOSE!"
            print "  The correct word was", m_word
     m_game()
elif difficulty == "Hard":
    lives = 6
    drawBoard(lives)
    print "  The word you are trying to guess is below"
    print ""
    for row in board_five:
        print "  " + " ".join(row)
    h_word = random.choice(five_word)
    lh_word[0] = h_word[0]
    lh_word[1] = h_word[1]
    lh_word[2] = h_word[2]
    lh_word[3] = h_word[3]
    lh_word[4] = h_word[4]

    def h_game():
        turns = 6
        lives = 6
        guessed = []
        correct = []
        incorrect = []
        while turns > 0:

            print ""
            char = raw_input("  Select a letter:  ")
            guessed.append(char)

            if char == h_word[0]:
                correct.append(char)
                board_five[0] = char
                print "  You guessed a letter!"
                print "  You have", turns, "turns left"
                print "  You have guessed", guessed
                print "  Correct guesses so far are", correct
                print "  Incorrect guesses so far are", incorrect
                print "  Your word is below"
                print ""

                drawBoard(lives)

                for row in board_five:
                    print "  " + " ".join(row)
                if board_five == lh_word:
                    print ""
                    print "YOU WIN!"
                    break
                
            elif char == h_word[1]:
                correct.append(char)
                board_five[1] = char
                print "  You guessed a letter!"
                print "  You have", turns, "turns left"
                print "  You have guessed", guessed
                print "  Correct guesses so far are", correct
                print "  Incorrect guesses so far are", incorrect
                print "  Your word is below"
                print ""

                drawBoard(lives)

                for row in board_five:
                    print "  " + " ".join(row)
                if board_five == lh_word:
                    print ""
                    print "  YOU WIN!"
                    break
                    
            elif char == h_word[2]:
                correct.append(char)
                board_five[2] = char
                print "  You guessed a letter!"
                print "  You have", turns, "turns left"
                print "  You have guessed", guessed
                print "  Correct guesses so far are", correct
                print "  Incorrect guesses so far are", incorrect
                print "  Your word is below"
                print ""

                drawBoard(lives)

                for row in board_five:
                    print "  " + " ".join(row)
                if board_five == lh_word:
                    print ""
                    print "  YOU WIN!"
                    break
            elif char == h_word[3]:
                correct.append(char)
                board_five[3] = char
                print "  You guessed a letter!"
                print "  You have", turns, "turns left"
                print "  You have guessed", guessed
                print "  Correct guesses so far are", correct
                print "  Incorrect guesses so far are", incorrect
                print "  Your word is below"
                print ""

                drawBoard(lives)

                for row in board_five:
                    print "  " + " ".join(row)
                if board_five == lh_word:
                    print ""
                    print "  YOU WIN!"
                    break
            elif char == h_word[4]:
                correct.append(char)
                board_five[4] = char
                print "  You guessed a letter!"
                print "  You have", turns, "turns left"
                print "  You have guessed", guessed
                print "  Correct guesses so far are", correct
                print "  Incorrect guesses so far are", incorrect
                print "  Your word is below"
                print ""

                drawBoard(lives)

                for row in board_five:
                    print "  " + " ".join(row)
                if board_five == lh_word:
                    print ""
                    print "  YOU WIN!"
                    break
                    
            else:
                incorrect.append(char)
                print "  You guessed incorrectly, you lose a life"
                turns = turns - 1
                lives = lives -1
                print "  You have", turns, "turns left"
                print "  You have guessed", guessed
                print "  Incorrect guesses so far are", incorrect
                print "  Correct guesses so far are", correct
                print "  Your word is below"
                print ""

                drawBoard(lives)

                for row in board_five:
                    print "  " + " ".join(row)
        else:
            print ""

            drawBoard(lives)

            print "  You LOSE!"
            print "  The correct word was", h_word
    h_game()




    

          



