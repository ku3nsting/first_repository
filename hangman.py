# Rebecca Kuensting
# Hangman Project
# June 3, 2016
import linecache
import random
import string
gameNumber = 1


while (exit != "x"):

    stars = "*******************************"
    space = " "
    spaceBlock = "\n \n \n \n \n \n"
    spaceStarsSpace = space+" \n "+stars+" \n "+space
    
    print stars
    print "*********** HANGMAN ***********"
    print stars
    print space

    print "How many players?"
    numberOfPlayers = raw_input("Type 1 or 2, then press ENTER to continue. \n")
    while (numberOfPlayers != "1" and numberOfPlayers != "2"):
        numberOfPlayers = raw_input("Oops! Make sure to type only \"1\" or \"2\" and then press ENTER \n")
    if (numberOfPlayers == "1"):

        print spaceStarsSpace
        
        singlePlayerName =  raw_input("What is your name? \n")

        print spaceStarsSpace
        computerOpponentName = raw_input(singlePlayerName+ ", who is your opponent? (input any name and press ENTER)\n")

        print spaceStarsSpace
        
        print (computerOpponentName+ " will select a word 3 to 10 letters long. \n" +singlePlayerName+ ", you will get 7 wrong guesses before you are hanged... \nTO DEATH!")

        print spaceStarsSpace

        raw_input("Press ENTER to continue")
    
        print spaceStarsSpace

        print "On a bright summer day, " +singlePlayerName+ ", who had \ncomitted the grievous crime of tomfoolery,\nwas led to the gallows by a crowd of angry onlookers. \n"
        print computerOpponentName+ " stood among the mob, looking troubled. \n"
        print "\"My friends!\" shouted " +computerOpponentName+ " to the mob, \n\"Should we not give this poor soul one final chance at redemption?\"\n"
        print "Even as " +singlePlayerName+ " was being forced up the steps of the scaffold \ntoward certain doom, a murmur of mercy rippled through the crowd. \n"
        print singlePlayerName+ " stood alone atop the scaffold \nand looked pleadingly into " +computerOpponentName+ "\'s thoughtful eyes. \n\n\"What can I do to prove my innocence?\" " +singlePlayerName+ " asked. \n"
        print "There was a dark gleam in " +computerOpponentName+ "\'s eyes. \n\"Guess a letter.\""

        print spaceStarsSpace
        print spaceBlock
        print spaceBlock
        
        wordChoices = (["APPLE", "ORANGE", "GIRAFFE", "GORILLA", "PEACHES", "WINTER", "SUMMER", "ABOUT", "WHY", "CAN", "CAT", "JUMP", "BEAN", "COOLER", "PEANUT", "HAPPENING", "BUTTERFLY", "PIVOT", "JAM",
                       "PINEAPPLE", "SHIP", "MUSTARD", "COTTON", "FISHY", "MYSTERY", "MAGIC", "PERHAPS", "WILLING", "HORSE", "COUNTER", "SKY", "GAMES", "FLOWERS", "KNIGHT", "DIAMONDS", "AUTHORITY", "PERSON",
                        "LYING", "SPEED", "PREJUDICE", "WISH", "THAT", "YES", "PILLORY", "EGGS", "WHISPER", "NICER", "ASSUME", "SARCASM", "JOVIAL", "ECLIPSE", "POUT", "LIPS", "BUTTER", "MESS", "HEARD", "SPROCKET"])
        maxChoice = (len(wordChoices) - 1)
        opponentWord = wordChoices[random.randrange(0, maxChoice)]


        raw_input("Press ENTER to continue.")
        print spaceBlock

        discard = "Wrong letters: "
        reveal = " "
        gallows = (["\n\n\t||\n\t||\n\t||\n\t||\n\t||\n\t||\n\t||\n\t||\n\t||\n\t||",
            "\n\n\t||======\n\t||\n\t||\n\t||\n\t||\n\t||\n\t||\n\t||\n\t||\n\t||",
            "\n\n\t||======\n\t||\t |\n\t||\t |\n\t||\t |\n\t||\n\t||\n\t||\n\t||\n\t||\n\t||",
            "\n\n\t||======\n\t||\t |\n\t||\t |\n\t||\t |\n\t||\t(O)\n\t||\n\t||\n\t||\n\t||\n\t||",
            "\n\n\t||======\n\t||\t |\n\t||\t |\n\t||\t |\n\t||\t(O)\n\t||\t |\n\t||\n\t||\n\t||\n\t||",
            "\n\n\t||======\n\t||\t |\n\t||\t |\n\t||\t |\n\t||\t(O)\n\t||\t\|/\n\t||\n\t||\n\t||\n\t||",
            "\n\n\t||======\n\t||\t |\n\t||\t |\n\t||\t |\n\t||\t(O)\n\t||\t\|/\n\t||\t |\n\t||\n\t||\n\t||",
            "\n\n\t||======\n\t||\t |\n\t||\t |\n\t||\t |\n\t||\t(O)\n\t||\t\|/\n\t||\t |\n\t||\t/ \\\n\t||\n\t||"])
        scaffold = "_________________________\n|_s__c__a__f__f__o__l__d_|\n_________________________\n\n\n"
        letterSpace = "-"
        x = 1
        while (x < len(opponentWord)):
            letterSpace += "-"
            reveal += " "
            x = (x+1)
        print "--- GAME "+str(gameNumber)+": "+computerOpponentName+" vs. "+singlePlayerName+ ". ---"
        print spaceStarsSpace
        print gallows[0]
        print scaffold
        print reveal
        print letterSpace
        print spaceBlock

        tries = 0
        while (tries < 100):
            guess = raw_input("\n\n"+singlePlayerName+ ", guess a letter. (Input your choice in CAPS)\n\n")
            result = (opponentWord.find(guess))
            if (result <= len(opponentWord) and result > -1):
                numberOfTimes = opponentWord.count(guess)
                if (numberOfTimes == 2):
                    print "\nCorrect!"+guess+" appears "+str(numberOfTimes)+" times in "+computerOpponentName+" \'s word!"
                    result2 = (opponentWord.rfind(guess))
                    reveal = reveal[:result] +guess+ reveal [result + 1:]
                    reveal = reveal[:result2] + guess + reveal [result2 + 1:]
                print "\nCorrect! "+guess+" is the " +str(result+1)+"th letter in "+computerOpponentName+"\'s word!\n\n"
                reveal = reveal[:result] + guess + reveal [result + 1:]
            else:
                print "\nSorry! "+computerOpponentName+"\'s word does not contain the letter "+guess+".\n\n"
                discard += " "+guess+" "
                tries = (tries+1)

            print gallows[tries]
            print scaffold
            print discard
            print space
            print "Correct guesses:"
            print reveal
            if reveal == opponentWord:
                print singlePlayerName+ " wins! \n\n" +singlePlayerName+ " walks safely down from the scaffold and lives a long and prosperous life"
                tries = 101
            if tries == 7:
                print ("Oh no, "+singlePlayerName+" has died on the gallows! "+computerOpponentName+"\'s word was "+opponentWord+" .")
                tries = 101
            print letterSpace

        print stars
        print stars
        print "********** GAME OVER **********"
        gameNumber = (gameNumber + 1)
        print stars
        print stars
        print space

        
        exit = raw_input("Press ENTER to restart game, or x then ENTER to exit.\n\n\n")
#END SINGLEPLAYER CODE
        
#BEGIN TWO-PLAYER CHOICE
    if(numberOfPlayers == "2"):
        player1Name = raw_input("Player 1, what is your name?\n ")
        print space
        player2Name = raw_input("Player 2, what is your name?\n ")

        print spaceStarsSpace

        print (player1Name+ " will guess \na word 3-10 letters in length. \n"
       +player2Name+ " will get 7 wrong guesses before they are hanged... \nTO DEATH!")

        print spaceStarsSpace

        raw_input("Press ENTER to continue")
    
        print spaceStarsSpace

        wordApproval = "x"

        while (wordApproval == "x"):
            player1Word = (raw_input(player1Name+ ", without letting " +player2Name+ " see, \nplease input your word in ALL CAPS: \n"))
            if(len(player1Word) > 10 or len(player1Word) < 3):
                player1Word = raw_input(player1Name+ ", please choose a word no shorter than \n3 letters and no longer than 10: \n")
            print space
            print "You have chosen the word " +player1Word+ ". Is that correct, " +player1Name+ "?"
            wordApproval = raw_input("Press ENTER to accept this word, \nor type x, then ENTER to try again \n")

        print spaceBlock
        print spaceBlock
        print spaceStarsSpace

        print "On a bright summer day, " +player2Name+ ", who had \ncomitted the grievous crime of tomfoolery,\nwas led to the gallows by a crowd of angry onlookers. \n"
        print player1Name+ " stood among the mob, looking troubled. \n"
        print "\"My friends!\" shouted " +player1Name+ " to the mob, \n\"Should we not give this poor soul one final chance at redemption?\"\n"
        print "Even as " +player2Name+ " was being forced up the steps of the scaffold \ntoward certain doom, a murmur of mercy rippled through the crowd. \n"
        print player2Name+ " stood alone atop the scaffold \nand looked pleadingly into " +player1Name+ "\'s thoughtful eyes. \n\n\"What can I do to prove my innocence?\" " +player2Name+ " asked. \n"
        print "There was a dark gleam in " +player1Name+ "\'s eyes. \n\"Guess a letter.\""

        print spaceStarsSpace
        print spaceBlock
        print spaceBlock

        raw_input("Press ENTER to continue.")
        print spaceBlock
        print spaceBlock

        discard = "Wrong letters: "
        reveal = " "
        gallows = (["\n\n\t||\n\t||\n\t||\n\t||\n\t||\n\t||\n\t||\n\t||\n\t||\n\t||",
            "\n\n\t||======\n\t||\n\t||\n\t||\n\t||\n\t||\n\t||\n\t||\n\t||\n\t||",
            "\n\n\t||======\n\t||\t |\n\t||\t |\n\t||\t |\n\t||\n\t||\n\t||\n\t||\n\t||\n\t||",
            "\n\n\t||======\n\t||\t |\n\t||\t |\n\t||\t |\n\t||\t(O)\n\t||\n\t||\n\t||\n\t||\n\t||",
            "\n\n\t||======\n\t||\t |\n\t||\t |\n\t||\t |\n\t||\t(O)\n\t||\t |\n\t||\n\t||\n\t||\n\t||",
            "\n\n\t||======\n\t||\t |\n\t||\t |\n\t||\t |\n\t||\t(O)\n\t||\t\|/\n\t||\n\t||\n\t||\n\t||",
            "\n\n\t||======\n\t||\t |\n\t||\t |\n\t||\t |\n\t||\t(O)\n\t||\t\|/\n\t||\t |\n\t||\n\t||\n\t||",
            "\n\n\t||======\n\t||\t |\n\t||\t |\n\t||\t |\n\t||\t(O)\n\t||\t\|/\n\t||\t |\n\t||\t/ \\\n\t||\n\t||"])
        scaffold = "_________________________\n|_s__c__a__f__f__o__l__d_|\n_________________________\n\n\n"
        letterSpace = "-"
        x = 1
        while (x < len(player1Word)):
            letterSpace += "-"
            reveal += " "
            x = (x+1)
        print "--- GAME "+str(gameNumber)+": "+player1Name+" vs. "+player2Name+ ". ---"
        print spaceStarsSpace
        print gallows[0]
        print scaffold
        print reveal
        print letterSpace
        print spaceStarsSpace

        tries = 0
        while (tries < 100):
            guess = raw_input("\n\n"+player2Name+ ", guess a letter. (Input your choice in CAPS)\n\n")
            result = (player1Word.find(guess))
            if (result <= len(player1Word) and result > -1):
                numberOfTimes = player1Word.count(guess)
                if (numberOfTimes == 2):
                    print "\nCorrect!"+guess+" appears "+str(numberOfTimes)+" times in "+player1Name+" \'s word!"
                    result2 = (player1Word.rfind(guess))
                    reveal = reveal[:result] +guess+ reveal [result + 1:]
                    reveal = reveal[:result2] + guess + reveal [result2 + 1:]
                print "\nCorrect! "+guess+" is the " +str(result+1)+"th letter in "+player1Name+"\'s word!\n\n"
                reveal = reveal[:result] + guess + reveal [result + 1:]
            else:
                print "\nSorry! "+player1Name+"\'s word does not contain the letter "+guess+".\n\n"
                discard += " "+guess+" "
                tries = (tries+1)

            print gallows[tries]
            print scaffold
            print discard
            print space
            print "Correct guesses:"
            print reveal
            if reveal == player1Word:
                print player2Name+ " wins! \n\n" +player2Name+ " walks safely down from the scaffold and lives a long and prosperous life"
                tries = 101
            if tries == 7:
                print ("Oh no, "+player2Name+" has died on the gallows! "+player1Name+"\'s word was "+player1Word+" .")
                tries = 101
            print letterSpace

        print stars
        print stars
        print "********** GAME OVER **********"
        gameNumber = (gameNumber + 1)
        print stars
        print stars
        print space

        exit = raw_input("Press ENTER to restart game, or x then ENTER to exit.\n\n\n")













    
