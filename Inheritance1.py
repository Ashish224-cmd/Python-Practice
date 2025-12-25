class Person:
    def printData(self):
        print(self.name)
        
class Singer(Person):
    def __init__(self,nameVal, songscountVal):
        super().__init__()
        self.name = nameVal
        self.songsCount = songscountVal
        
    def printData(self):
        return super().printData()
    
singer = Singer("Arina",26)
print(singer.name)    