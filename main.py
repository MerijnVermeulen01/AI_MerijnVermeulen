countRounds = 0
if countRounds == 10:
    countRounds = 0

def rules():
    print('')
    print('Welkom bij de regels van Mastermind dit zijn alle regels:')
    print('1. Je moet de nummers 1 tot en met 6, vier keer gebruiken om het goede antwoord te krijgen')

def startUp():
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

def startGame(playStyle):
    from functions import core
    global countRounds
    count = 0
    playerCombination = []
    coreFunctions = core(playerCombination)
    while countRounds <= 9:
        while count <= 3:
            combination = int(input('Wat zijn de nummer?: '))
            if combination >= 7 or combination <= 0:
                print('Je kan alleen de nummers 1 tot en met 6 gebruiken')
                startGame()
            playerCombination.append(combination)
            count += 1
        coreFunctions.checkColors()
        countRounds += 1
        print('')
        startGame(playStyle)

startUp()