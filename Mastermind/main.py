"""
..:: Code Review ::..

1) Functionele decompositie

Hier is nog wel wat te winnen; ik waardeer het dat de code inderdaad opgedeeld is in verschillende functies met
verschillende gebruiken, maar er wordt bijvoorbeeld in meerdere functies hieronder om invoer van de gebruiker gevraagd.
Hierbij is het risico dat iemand (expres/per ongeluk) verkeerde invoer geeft. Het beste kun je een aparte, flexibele
functie schrijven (bijv. toonMenu) die antwoorden blijft vragen tot er een geldige optie wordt gegeven. Dan zal je
opvallen hoeveel je kunt vervangen in je functies, en hoeveel ruimte je dat scheelt!
Dito zo met uitvoer naar de GUI; er staat nu bijvoorbeeld een print-regel in de core-module, die daar eigenlijk niet
thuishoort (dat is immers uitvoer naar de buitenwereld).

2) Onderverdeling in modules

Hier wordt, denk ik, nog aan gewerkt; de module "core" lijkt alle variabelen, inclusief de globals, te bevatten die in
dit bestand worden gebruikt, maar dan in een klasse. Je kunt beter een klasse genaamd bijv. spelregels aanmaken die
alles bijhoudt, en die strikt gescheiden houden van de GUI, zoals voorgenoemd. Tevens is "functions.py" een iets te
algemene naam. Voor testing kun je ook eens kijken naar de unittest library, maar dat is een wat te vergevorderd
onderwerp.

3) Commentaar

In het algemeen heb je commentaar in je functies staan dat beknopt beschrijft wat de functies doen; wel zou ik je
aanraden om overal kort bij op te nemen hoe de functies dat doel bereiken. Neem bijvoorbeeld de functie rules();
hier zou ik bij zetten
    '''Deze functie legt de regels van het spel uit, door vaste geschreven instructies naar de console af te drukken.'''
Wat, maar ook hoe. Zeker bij lastigere functies is dat handig!

5) Werking van de code

Bezijdens dat zijn de strings waarmee de gebruiker om invoer gevraagd wordt niet helder, dus ik weet niet goed hoe ik de applicatie moet gebruiken.

"""

import random
from functions import core

def rules():
    '''This function is to explain the rules of the game'''
    print(f'\n Welcome to the rules of Mastermind:'
          f'\n 1. You have to use the numbers 1 up to including 6, four times to guess the right code')

def startUp():
    '''
    This function is to start the game.
    By the player input they can then choose which game mode they want to play
    '''
    print(f'Welcome to mastermind! '
          f'\n This is the menu: '
          f'\n 1. PvP   (This is work in progress) '
          f'\n 2. PvC '
          f'\n 3. CvC   (This is work in progress)')
    playStyle = int(input('What do you want to play?: '))
    print('')
    if playStyle == 1 or playStyle == 3:
        startUp()
    #     rule = input('Do you want to read the rules?: ')
    #     if rule.lower() == 'ja' or rule.lower() == 'yes':
    #         rules()
    #     startGame(playStyle)
    if playStyle == 2:
        print(f'1. De codecracker'
              f'\n2. De codemaker  (This is work in progress)')
        playStyleVSAI = int(input('Who do you want to be?: '))
        print('')
        if playStyleVSAI == 1 or playStyleVSAI == 2:
            rule = input('Do you want to read the rules?: ')
            if rule.lower() == 'ja' or rule.lower() == 'yes':
                rules()
            startGame(3+playStyleVSAI)


def resetGame(playStyle, score):
    '''
    This function makes its so you can play mutiple times
    It just does not work at the moment
    '''
    print(f"Do you want to play again with the same settings?:"
          f"\n 1. Yes, I want to play with the same settings"
          f"\n 2. No, I want to play with other settings"
          f"\n 3. No, I don't want to play anymore")
    resetGameState = input('What do you choose?: ')
    print('')
    if resetGameState == '1':
        startGame(playStyle)
        randomColorCombination()
    elif resetGameState == '2':
        startUp()
        randomColorCombination()
    else:
        print('Thank you for playing. The score was P1: ' + str(score[0]) + ' against AI: ' + str(score[1]))

def randomColorCombination():
    '''This function is to make the random code combination'''
    global randomCodeGen
    randomCodeGen = []
    for i in range(0,4):
        randomCode = random.randint(1, 6)
        randomCodeGen.append(randomCode)
    return randomCodeGen

'''These variable are the core to the game'''
global randomCode
randomCode = randomColorCombination()
countRounds = 0

def startGame(playStyle):
    '''This function makes sure the game can be played'''
    global countRounds
    playerCombination = []
    coreFunctions = core(playerCombination, randomCode, countRounds)
    count = 1
    if countRounds <= 9:
        while count <= 4:
            combination = int(input('What is number ' + str(count) + ' of the 4-digit code?: '))
            if combination >= 7 or combination <= 0:
                print('You can only use 1 up to inluding 6')
                startGame(playStyle)
            playerCombination.append(combination)
            count += 1
        checkForFinish = coreFunctions.checkColors()
        countRounds += 1
        if checkForFinish != True:
            feedback = coreFunctions.feedbackBlack()
            print(coreFunctions.algorimte)
            print(feedback)
            startGame(playStyle)
            if countRounds == 10:
                score = coreFunctions.saveScore()
                resetGame(playStyle, score)
        else:
            score = coreFunctions.saveScore()
            resetGame(playStyle, score)

startUp()