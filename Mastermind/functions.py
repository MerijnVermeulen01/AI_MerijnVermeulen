class core:
    def __init__(self, combination, randomCode, countRounds):
        self.lst = combination
        self.scorePlayer = 0
        self.scoreAI = 0
        self.random = randomCode
        self.rounds = countRounds
        print(randomCode)

    def checkWhichPlayStyle(self): #TODO: zet hier vast commentaar, ook als het nog niet is geimplementeerd!
        return

    def checkColors(self):
        '''Deze functie is er om de kijken of de combinatie's gelijk zijn aan de combinatie die de computer heeft gemaakt'''
        if self.random == self.lst:
            self.scorePlayer += 1
            return True
        elif self.rounds <= 9:
            self.feedbackBlackColor()
            self.feedbackWhiteColor()
        else:
            self.scoreAI += 1

    def feedbackWhiteColor(self):
        '''Deze functie kijkt of de goede getallen zijn aan gegeven maar niet op de goede plek staan'''
        return

    def feedbackBlackColor(self):
        '''Deze functie kijkt of de getallen op de correcte plek staan en of ze het goede nummer zijn'''
        correctLst = []
        count = 0
        for i in self.lst:
            if self.lst[count] == self.random[count]:
                correctLst.append(self.lst[count])
            count += 1
        print('Je hebt de ' + str(len(correctLst)) + ' goed op de goede plek') #TODO: deze regel hoort hier volgens mij niet!

    def saveScore(self):
        '''Deze functie is om bij te houden wat de score is'''
        lstPlayer = []
        lstPlayer.append(self.scorePlayer)
        print(len(lstPlayer))
        return [self.scorePlayer, self.scoreAI]