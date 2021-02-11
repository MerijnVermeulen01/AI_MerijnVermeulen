"""

..:: Code Review ::..

Ik heb mijn voorgestelde aanpassingen bij de betreffende code gezet met TODO's;
uiteraard rest jou de keuze hoeveel je hiermee wilt doen. Hier even centraal een paar opmerkingen.
Onderzochte aspecten:

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

4) Naamgeving variabelen

De naamgeving van je variabelen is qua formaat prima, en goed consistent Engels. Wel denk ik dat het onhandig is om
variabelen een naam te geven die aanneemt wat er wordt ingevuld. Denk aan startOver hieronder!

5) Werking van de code

De code werkt helaas nog niet volledig; ik heb gepoogd te spelen, maar loop al snel tegen een error aan
(startGame missing 1 required positional argument). Bezijdens dat zijn de strings waarmee de gebruiker om invoer gevraagd
wordt niet helder, dus ik weet niet goed hoe ik de applicatie moet gebruiken.

"""

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

def resetGame(playStyle, score): #TODO: commentaar aanleveren!
    print('Wilt je nog een keer met dezelfde instellingen spelen?:')
    print('1. Ja, ik wil met dezelfde instellingen spelen')
    print('2. Nee, ik wil met andere instellingen spelen')
    print('3. Nee, ik wil niet meer spelen')
    startOver = input('Wat kies je?: ')
    print('')
    if startOver == '1': #TODO: de speler kiest niet per definitie "start over", dus dit is geen handige variabelenaam!
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
if countRounds <= 9: #TODO: wanneer gaat dit gebeuren?
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