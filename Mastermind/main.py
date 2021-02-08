import random
from functions import core

def rules():
    '''Deze functie is er om de regels van het spel uit te leggen'''
    print('')
    print('Welkom bij de regels van Mastermind dit zijn alle regels:')
    print('1. Je moet de nummers 1 tot en met 6, vier keer gebruiken om het goede antwoord te krijgen')

def startUp():
    '''Deze functie is er om het spel op te starten'''
    print('Welkom bij mastermind!')
    print('Dit het menu:')
    print('1. PvP')
    print('2. PvC')
    print('3. CvC')
    playStyle = int(input('Wat wilt je doen?: '))
    print('')
    if playStyle == 1 or playStyle == 3:
        rule = input('Wilt u de regels zien?: ')
        if rule == 'ja' or rule == 'Ja' or rule == 'JA':
            rules()
        startGame(playStyle)
    if playStyle == 2:
        print('Wat wilt je zijn?:')
        print('1. De codekraker')
        print('2. De codemaker')
        playStyleVSAI = int(input('Wat wilt u doen?: '))
        print('')
        if playStyleVSAI == 1 or playStyleVSAI == 2:
            rule = input('Wilt u de regels zien?: ')
            if rule == 'ja' or rule == 'Ja' or rule == 'JA':
                rules()
            startGame(3+playStyleVSAI)

def resetGame(playStyle, score):
    print('Wilt je nog een keer met dezelfde instellingen spelen?:')
    print('1. Ja, ik wil met dezelfde instellingen spelen')
    print('2. Nee, ik wil met andere instellingen spelen')
    print('3. Nee, ik wil niet meer spelen')
    startOver = input('Wat kies je?: ')
    print('')
    if startOver == '1':
        startGame(playStyle)
        randomColorCombination()
    elif startOver == '2':
        startUp()
        randomColorCombination()
    else:
        print('Dank je wel voor het spelen de score was P1: ' + str(score[0]) + ' tegen AI: ' + str(score[1]))

def randomColorCombination():
    '''Deze functie is er om een random combinatie te maken'''
    global randomCodeGen
    randomCodeGen = []
    for i in range(0,4):
        randomCode = random.randint(1, 6)
        randomCodeGen.append(randomCode)
    return randomCodeGen

'''Deze variable zijn de core van de game'''
global randomCode
randomCode = randomColorCombination()
countRounds = 0
if countRounds <= 9:
    countRounds = 0

def startGame(playStyle):
    '''Deze functie laat de core van het spel op gang lopen'''
    global countRounds
    playerCombination = []
    coreFunctions = core(playerCombination, randomCode, countRounds)
    count = 0
    if countRounds <= 9:
        while count <= 3:
            combination = int(input('Wat zijn de nummer?: '))
            if combination >= 7 or combination <= 0:
                print('Je kan alleen de nummers 1 tot en met 6 gebruiken')
                startGame()
            playerCombination.append(combination)
            count += 1
        checkForFinish = coreFunctions.checkColors()
        countRounds += 1
        print('')
        if checkForFinish != True:
            startGame(playStyle)
        else:
            score = coreFunctions.saveScore()
            resetGame(playStyle, score)


print(randomColorCombination())
startUp()