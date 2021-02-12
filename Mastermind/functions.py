import random
class core:
    def __init__(self, combination, randomCode, countRounds):
        '''This is the constructor of the class'''
        self.lst = combination
        self.scorePlayer = 0
        self.scoreAI = 0
        self.random = randomCode
        self.rounds = countRounds
        self.correctLst = []
        self.feedbackList = []
        print(self.feedbackList)
        print(randomCode)

    def checkWhichPlayStyle(self): #TODO: zet hier vast commentaar, ook als het nog niet is geimplementeerd!
        ''''''
        return

    def checkColors(self):
        '''This function is to look if the random combination is the same as the guessed combination'''
        if self.random == self.lst:
            self.scorePlayer += 1
            return True
        elif self.rounds <= 9:
            self.feedbackBlack()
        else:
            self.scoreAI += 1

    def feedbackBlack(self):
        '''This fucntion looks if all/some of the numbers are on the same location and the same value'''
        for i in range(0, 3):
            if self.lst[i] == self.random[i]:
                self.correctLst.append(self.lst[i])
                self.feedbackList.append('B')
            else:
                self.correctLst.append(None)
        self.feedbackWhite()
        # return self.feedbackWhite()

    def feedbackWhite(self):
        '''This function looks if all/some of the numbers are in the random combination'''
        for i in range(0, 3):
            if self.correctLst[i] == None:
                if self.lst[i] in self.random:
                    self.feedbackList.append('W')
        random.shuffle(self.feedbackList)
        print(self.feedbackList)

    def saveScore(self):
        '''This function keeps the score'''
        lstPlayer = []
        lstPlayer.append(self.scorePlayer)
        return [self.scorePlayer, self.scoreAI]

    def algorimte(self):
        while self.feedbackList != ['B', 'B', 'B', 'B']:
            return 'yeetus'