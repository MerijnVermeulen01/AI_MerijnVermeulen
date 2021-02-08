import random

class core:
    def __init__(self, combination):
        self.lst = combination
        self.score = 0

    def checkWhichPlayStyle(self):
        return

    def randomColorCombination(self):
        '''Deze functie is er om een random combinatie te maken'''
        global randomCodeGen
        randomCodeGen = []
        for i in range(0,4):
            randomCode = random.randint(1, 6)
            randomCodeGen.append(randomCode)
        return randomCodeGen

    def checkColors(self):
        '''Deze functie is er om de kijken of de combinatie's gelijk zijn aan de combinatie die de computer heeft gemaakt'''
        print(self.randomColorCombination())
        if randomCodeGen == self.lst:
            self.score += 1
        else:
            self.feedbackBlackColor()
            self.feedbackWhiteColor()

    def feedbackWhiteColor(self):
        '''Deze functie kijkt of de goede getallen zijn aan gegeven maar niet op de goede plek staan'''
        return

    def feedbackBlackColor(self):
        '''Deze functie kijkt of de getallen op de correcte plek staan en of ze het goede nummer zijn'''
        correctLst = []
        count = 0
        for i in self.lst:
            if self.lst[count] == randomCodeGen[count]:
                correctLst.append(self.lst[count])
            count += 1
        print('Je hebt de ' + str(len(correctLst)) + ' goed op de goede plek')

    def saveScore(self):
        '''Deze functie is om bij te houden wat de score is'''
        return self.score