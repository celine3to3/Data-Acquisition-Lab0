class Database:
    def __init__(self, dictionary):
        self.dict = dictionary

    def load_dict(self, firstList, secondList):
        for i in range(len(firstList)):
            self.dict[firstList[i]] = secondList[i]

    def getDict(self):
        return self.dict