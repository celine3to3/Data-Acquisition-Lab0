class Output:
    def __init__(self, database):
        self.database = database
        self.dict = database.getDict()

    def displayDict(self):
        print(" Fossil CO2 Emissions\n")
        print(" Country".ljust(45), "2017 (% of world)".rjust(20))
        for key in self.dict:
            print(key.ljust(45), self.dict[key].rjust(20))