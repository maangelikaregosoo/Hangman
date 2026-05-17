# Ma. Angelika C. Regoso, 204255
# March 18, 2024

# I/we certify that this submission complies with the DISCS Academic Integrity
# Policy.

# If I/we have discussed my/our Python language code with anyone other than
# my/our instructor(s), my/our groupmate(s), the teaching assistant(s),
# the extent of each discussion has been clearly noted along with a proper
# citation in the comments of my/our program.

# If any Python language code or documentation used in my/our program
# was obtained from another source, either modified or unmodified, such as a
# textbook, website, or another individual, the extent of its use has been
# clearly noted along with a proper citation in the comments of my/our program.

################################################################################

# cite your sources here, if any

################################################################################

# your python code starts here

import random

def initializeVars():
    upper_case_letters= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_case_Letters='abcdefghijklmnopqrstuvwxyz'
    lower_case_list=list(lower_case_Letters)
    upper_case_list=list(upper_case_letters)
    guessed_letters=[]
    return upper_case_letters, lower_case_Letters, lower_case_list, upper_case_list, guessed_letters

def intro():
    print("\nLET'S PLAY HANGMAN!")
    print("")

def randomizer():
    wordList = ['DOG', 'CAT', 'ELEPHANT', 'GIRAFFE', 'LION', 'TIGER', 'ZEBRA', 'RABBIT', 'FROG', 'SNAKE', 'APPLE', 'BANANA', 'ORANGE', 'GRAPE', 'KIWI', 'PEACH', 'PEAR', 'MELON', 'RED', 'BLUE', 'GREEN', 'YELLOW', 'PURPLE', 'ORANGE', 'PINK', 'BLACK', 'WHITE', 'BROWN', 'USA', 'CANADA', 'BRAZIL', 'INDIA', 'CHINA', 'JAPAN', 'FRANCE', 'GERMANY', 'AUSTRALIA', 'RUSSIA', 'SOCCER', 'BASKETBALL', 'TENNIS', 'BASEBALL', 'VOLLEYBALL', 'SWIMMING', 'BOXING', 'GOLF', 'CRICKET','JOHNNY','ANGEL']
    random_index = int((random.random()) * len(wordList) - 1)
    random_word = wordList[random_index]
    print(f'\nHere is the word to be guessed by your opponent: {random_word}')
    return random_word

def setting_num_Guess():
    print('\nPlease enter the number of guesses allowed:')
    num_guesses_allowed=int(input())
    return num_guesses_allowed

def SettingWordToGuess():
    print("Would you like the program to choose a random word? (Yes/No)")
    randomness=input()
    if randomness == 'yes' or randomness == 'Yes':
        wordGuess = randomizer()
    elif randomness == 'no' or randomness == 'No':
        print('\nPlease enter a word for the other player to guess:')
        wordGuess = input()
    else:
        print('Invalid Input.')
        print('\n')
        wordGuess=SettingWordToGuess()
    return wordGuess

def wordToList(word):
    wordGuessArr = list(word)
    return wordGuessArr
    
def HideCharsInWord(word):
    dashOfWord = []
    for letter in word:
        if letter == ' ':
            dashOfWord.append(' ')
        else:
            dashOfWord.append('-')
    return dashOfWord

def listToString(list):
    string=""
    for item in list:
        string += item +''
    return string

def lookinList(Char, list):
    for index in  range(0, len(list)):
        if Char == list[index]: 
            return index
    
def comparingGuessAndWord(Char, list):
    indices=[]
    for index in  range(0, len(list)):
        if Char == list[index]:
            indices.append(index)
    if len(indices)==0:
        return None
    else:
        return indices

def checkingValidityInput(character):
    lowerCaseIndex = lookinList(character, list(lower_case_Letters))
    upperCaseIndex=lookinList(character,list(upper_case_letters))
    if lowerCaseIndex == None and upperCaseIndex == None:
        print('\nPlease choose a valid letter.\n')
        return False
    else:
        return True

def checkingRepeatedInput(character,guessed_list):
    guessed_index=lookinList(character,guessed_list)
    if guessed_index != None:
        print('\nYou have already used that letter.\n')
        return True
    else: 
        return False

def eliminatingCharInput(character):
    index = lookinList(character, lower_case_list) 
    if index == None: 
        upperCaseLetter = character 
        index = lookinList(character, upper_case_list) 
    else:
        upperCaseLetter = upper_case_list[index]
    new_upper_case_list = [letter for letter in upper_case_list if (letter!=upperCaseLetter)]
    new_lower_case_list = [letter for letter in lower_case_list if (letter!=lower_case_list[index])]
    return new_upper_case_list,new_lower_case_list

def GameStatus(guesses_left, hiddenWord, UpperCaseLettersList):
    print(f'\nGuess the word, {guesses_left} guess(es) left: {hiddenWord}')
    print(f'Unused letters: {listToString(UpperCaseLettersList)}')

def appendingGuessedLetters(character):
    lowerCaseIndex = lookinList(character, list(lower_case_Letters))
    upperCaseIndex=lookinList(character,list(upper_case_letters))
    if lowerCaseIndex == None:
        guessed_letters.append(character)
        guessed_letters.append((list(lower_case_Letters))[upperCaseIndex])
    elif upperCaseIndex == None:
        guessed_letters.append(character)
        guessed_letters.append((list(upper_case_letters))[lowerCaseIndex])
    return guessed_letters

def equivalentWord(wordCharsList, lower_case_Letters,upper_case_letters):
    equivalent_Word_chars=[]
    for char in wordCharsList:
        if char == ' ':
            equivalent_Word_chars.append(' ')
            continue
        lower_case_index=lookinList(char,list(lower_case_Letters))
        if lower_case_index!=None:
            equivalent_Word_chars.append((list(upper_case_letters))[lower_case_index])
        else: 
            upper_case_index=lookinList(char, list(upper_case_letters))
            equivalent_Word_chars.append((list(lower_case_Letters))[upper_case_index])
    return equivalent_Word_chars

def revealLetter(index_list, WordCharsList, hiddenWordCharsList):
    for i in index_list:
                revealed_letter=WordCharsList[i]
                hiddenWordCharsList[i]=revealed_letter
                hiddenWordString=listToString(hiddenWordCharsList)
    return hiddenWordString

#Hangman Figure Functions
def initialStickmanParts():
    upperbody='''  _ _ _ _ \n |       |\n |       0\n |      /|\\\n '''
    lowerbody='''|      / \\\n[_]'''
    bodypart_added='|       |'+'\n'+' '
    return upperbody, lowerbody, bodypart_added

def StickManFigureAdjusted(input_guesses, upperbody, lowerbody, bodypart_added):
    if input_guesses>6:
        difference=input_guesses-6
        for i in range(0, difference):
            upperbody+=bodypart_added
        wholeman_str=upperbody+lowerbody
    else:
        wholeman_str=upperbody+lowerbody
    return wholeman_str

def IndexPositionStickmanParts(wholeman_str, input_guesses):
    head_index=31
    left_arm_index=41
    main_body_index=42
    right_arm_index=43
    left_leg_index=len(list(wholeman_str))-7
    right_leg_index=len(list(wholeman_str))-5
    pole_index_before_leg=len(list(wholeman_str))-14
    headtobody_indices=[head_index,left_arm_index,main_body_index,right_arm_index]
    if input_guesses>6:
        [headtobody_indices.append(x) for x in range(54,pole_index_before_leg,11)]
    headtolegs_indices=headtobody_indices
    headtolegs_indices.append(left_leg_index)
    headtolegs_indices.append(right_leg_index)
    return headtolegs_indices


def HideStickmanPartsLs(wholeman_str,headtolegs_indices):
    hidden_wholeman_ls=list(wholeman_str)
    hidden_wholemanparts_ls=[]
    for i in headtolegs_indices:
        hidden_wholemanparts_ls.append(hidden_wholeman_ls[i])
        hidden_wholeman_ls[i]=' '
    return hidden_wholemanparts_ls, hidden_wholeman_ls

def HideStickmanPartsStr(hidden_wholeman_ls):
    hidden_wholeman_str=''
    for item in hidden_wholeman_ls:
        hidden_wholeman_str+=item
    return hidden_wholeman_str, hidden_wholeman_str


def GroupedIndicesPartsForLessThanSixInputs(input_guesses, headtoleg_indices, hidden_wholemanparts_ls):
    grouped_headtoleg_indices=[]
    grouped_hiddenman_parts_list=[]
    cutoff_index=input_guesses-1
    for i in range(0,cutoff_index):
        grouped_headtoleg_indices.append(headtoleg_indices[i])
        grouped_hiddenman_parts_list.append(hidden_wholemanparts_ls[i])
    grouped_headtoleg_indices.append(headtoleg_indices[cutoff_index:])
    grouped_hiddenman_parts_list.append(hidden_wholemanparts_ls[cutoff_index:])
    return grouped_headtoleg_indices, grouped_hiddenman_parts_list


def revealBodyPart_for_6_or_more_inputs(index,headlegindices,hiddenmanlist,hiddenpartslist):
    index_to_reveal=headlegindices[index]
    hiddenmanlist[index_to_reveal]=hiddenpartslist[index]
    updatedhiddenman=''
    for parts in hiddenmanlist:
        updatedhiddenman+=parts
    print("State of Hangman Stick Figure:")
    print(updatedhiddenman)
    index+=1
    return index,hiddenmanlist,updatedhiddenman

def revealBodyPart_for_less_6_inputs(input,index,grpHeadLegIndices,hiddenmanlist,grphiddenpartslist):
    indices_to_reveal=grpHeadLegIndices[index]
    indexpart=0
    if index==input-1:
        for index_to_reveal in indices_to_reveal:
            hiddenmanlist[index_to_reveal]=(grphiddenpartslist[input-1])[indexpart]
            indexpart+=1
    else:
        hiddenmanlist[indices_to_reveal]=grphiddenpartslist[index]
    updatedhiddenman=''
    for parts in hiddenmanlist:
        updatedhiddenman+=parts
    print("State of Hangman Stick Figure:")
    print(updatedhiddenman)
    index+=1
    return index,hiddenmanlist,updatedhiddenman

#End of Hangman Figure Functions

def checkingGuessedLetter(character, numGuessesLeft, WordCharsList,EquiWordCharsList, hiddenWordCharsList, hiddenWordString):
    indices_in_given_word=comparingGuessAndWord(character, WordCharsList)
    indices_in_equi_word=comparingGuessAndWord(character, EquiWordCharsList)
    if indices_in_given_word != None and indices_in_equi_word != None:
        hiddenWordString=revealLetter(indices_in_given_word, WordCharsList, hiddenWordCharsList)
        hiddenWordString=revealLetter(indices_in_equi_word, WordCharsList, hiddenWordCharsList)
        error=False
    elif indices_in_given_word != None:
        hiddenWordString=revealLetter(indices_in_given_word, WordCharsList, hiddenWordCharsList)
        error=False
    elif indices_in_equi_word !=None:
        hiddenWordString=revealLetter(indices_in_equi_word, WordCharsList, hiddenWordCharsList)
        error=False
    else:
        numGuessesLeft-=1
        error=True
    return(numGuessesLeft,hiddenWordCharsList,hiddenWordString,error)

def WinOrLoseStatus(wins,hidden_chars_word_list, guessesLeft):
    indices=[]
    for i in range(0, len(hidden_chars_word_list)):
        if hidden_chars_word_list[i] == '-' :
            indices.append(i)
    if len(indices)==0:
        print('CONGRATULATIONS! YOU WIN!')
        wins+=1
        return True, wins
    elif len(indices)!=0 and guessesLeft==0:
        print('SORRY, YOU ARE HANGED')
        return True, wins
    else:
        return None, wins

def PlayAgain():
    print('\nWould you like to play again? (Yes/No)')
    playAgainAns=input()
    if playAgainAns=='Yes' or playAgainAns=='yes':
        return True
    elif playAgainAns=='No' or playAgainAns=='no':
        return False
    else:
        print('Invalid Input!')
        playAgainAns=PlayAgain()

def StartOfGame():
    intro()
    word=SettingWordToGuess()
    no_of_guesses=setting_num_Guess()
    original_guesses=no_of_guesses
    word_to_list=wordToList(word)
    upper_case_letters, lower_case_Letters, lower_case_list, upper_case_list, guessed_letters = initializeVars()
    equivalent_word_to_list=equivalentWord(word_to_list, lower_case_Letters,upper_case_letters)
    hidden_chars_word=HideCharsInWord(word)
    hidden_word=listToString(hidden_chars_word)
    index_hangman=0
    return index_hangman, original_guesses, no_of_guesses, word_to_list, equivalent_word_to_list, hidden_chars_word, hidden_word, upper_case_letters, lower_case_Letters, lower_case_list, upper_case_list, guessed_letters

def GameProper():
    index_hangman, original_guesses, no_of_guesses, word_to_list, equivalent_word_to_list, hidden_chars_word, hidden_word, upper_case_letters, lower_case_Letters, lower_case_list, upper_case_list, guessed_letters = StartOfGame()
    man_in_gallows_upper, man_in_gallow_lower, body_part_to_be_added_=initialStickmanParts()
    man_in_gallows_str=StickManFigureAdjusted(no_of_guesses, man_in_gallows_upper, man_in_gallow_lower, body_part_to_be_added_)
    head_to_legs_indices=IndexPositionStickmanParts(man_in_gallows_str,no_of_guesses)
    hiddenManParts_Gallows_list, hiddenMan_Gallows_list=HideStickmanPartsLs(man_in_gallows_str, head_to_legs_indices)
    hiddenMan_Gallows_str, revealed_hidden_man=HideStickmanPartsStr(hiddenMan_Gallows_list)
    return index_hangman, original_guesses, no_of_guesses, word_to_list, equivalent_word_to_list, hidden_chars_word, hidden_word, upper_case_letters, lower_case_Letters, lower_case_list, upper_case_list, guessed_letters, man_in_gallows_upper, man_in_gallow_lower, body_part_to_be_added_, man_in_gallows_str, head_to_legs_indices, hiddenManParts_Gallows_list, hiddenMan_Gallows_list, hiddenMan_Gallows_str, revealed_hidden_man

index_hangman, original_guesses, no_of_guesses, word_to_list, equivalent_word_to_list, hidden_chars_word, hidden_word, upper_case_letters, lower_case_Letters, lower_case_list, upper_case_list, guessed_letters, man_in_gallows_upper, man_in_gallow_lower, body_part_to_be_added_, man_in_gallows_str, head_to_legs_indices, hiddenManParts_Gallows_list, hiddenMan_Gallows_list, hiddenMan_Gallows_str, revealed_hidden_man = GameProper()
wins=0
totalgame=1
if original_guesses<6:
    grouped_head_to_leg_indices, grouped_hiddenManParts_Gallows_list = GroupedIndicesPartsForLessThanSixInputs(original_guesses, head_to_legs_indices, hiddenManParts_Gallows_list)

while True:
    GameStatus(no_of_guesses,hidden_word,upper_case_list)
    endOfOneGame, wins = WinOrLoseStatus(wins,hidden_word, no_of_guesses)
    if endOfOneGame == True:
        print(f'Total Wins for All Games Played:{wins}/{totalgame}')
        if PlayAgain()==False:
            break
        else:
            totalgame+=1
            index_hangman, original_guesses, no_of_guesses, word_to_list, equivalent_word_to_list, hidden_chars_word, hidden_word, upper_case_letters, lower_case_Letters, lower_case_list, upper_case_list, guessed_letters, man_in_gallows_upper, man_in_gallow_lower, body_part_to_be_added_, man_in_gallows_str, head_to_legs_indices, hiddenManParts_Gallows_list, hiddenMan_Gallows_list, hiddenMan_Gallows_str, revealed_hidden_man = GameProper()
            if original_guesses<6:
                grouped_head_to_leg_indices, grouped_hiddenManParts_Gallows_list = GroupedIndicesPartsForLessThanSixInputs(original_guesses, head_to_legs_indices, hiddenManParts_Gallows_list)
            GameStatus(no_of_guesses,hidden_word,upper_case_list)
    char=input()
    if checkingValidityInput(char)== True:
        if checkingRepeatedInput(char, guessed_letters) == False:
            upper_case_list, lower_case_list = eliminatingCharInput(char)
            guessed_letters=appendingGuessedLetters(char)
            no_of_guesses, hidden_chars_word, hidden_word, isItError = checkingGuessedLetter(char, no_of_guesses, word_to_list, equivalent_word_to_list, hidden_chars_word, hidden_word)
            if isItError == True:
                if original_guesses>=6:
                    index_hangman, hiddenMan_Gallows_list,revealed_hidden_man=revealBodyPart_for_6_or_more_inputs(index_hangman,head_to_legs_indices,hiddenMan_Gallows_list,hiddenManParts_Gallows_list)
                else:
                    index_hangman, hiddenMan_Gallows_list,revealed_hidden_man=revealBodyPart_for_less_6_inputs(original_guesses,index_hangman,grouped_head_to_leg_indices,hiddenMan_Gallows_list,grouped_hiddenManParts_Gallows_list)
            else:
                print("State of Hangman Stick Figure:")
                print(revealed_hidden_man)
        else:
            print("State of Hangman Stick Figure:")
            print(revealed_hidden_man)
    else:
        print("State of Hangman Stick Figure:")
        print(revealed_hidden_man)