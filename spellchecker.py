import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.multiDict=md.MultiDictionary()

    def handleSentence(self, txtIn, language):
        txtIn=replaceChars(txtIn)
        parole=txtIn.split(" ")
        start_time=time.time()
        parole_errate=self.multiDict.searchWord(parole,language)
        end_time=time.time()
        start_time1=time.time()
        parole_errate_linear=self.multiDict.searchWordLinear(parole,language)
        end_time1=time.time()
        start_time2=time.time()
        parole_errate_dichotomic=self.multiDict.searchWordDichotomic(parole,language)
        end_time2=time.time()
        return parole_errate, end_time-start_time, parole_errate_linear,end_time1-start_time1,parole_errate_dichotomic, end_time2-start_time2

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
        chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
        for c in chars:
            text = text.replace(c, "")
        return text