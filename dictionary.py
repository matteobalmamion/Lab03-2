class Dictionary:
    def __init__(self):
        self._dict=[]

    def loadDictionary(self,path):
        try:
            file=open(path,"r",encoding="utf-8")
        except FileNotFoundError:
            print("File not found")
        for word in file:
            self._dict.append(word.strip())

    def printAll(self):
        return self._dict

    @property
    def dict(self):
        return self._dict