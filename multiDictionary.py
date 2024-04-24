import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
        self._dic_ita=d.Dictionary()
        self._dic_ing=d.Dictionary()
        self._dic_spa=d.Dictionary()
        self._dic_ita.loadDictionary("resources/Italian.txt")
        self._dic_ing.loadDictionary("resources/English.txt")
        self._dic_spa.loadDictionary("resources/Spanish.txt")

    def printDic(self, language):
        if language == 'Italiano':
            return self._dic_ita.printAll()
        elif language == 'Inglese':
            return self._dic_ing.printAll()
        elif language == 'Spagnolo':
            return self._dic_spa.printAll()

    def searchWord(self, words, language):
        parole=[]
        if language == 'italian':
            for parola in words:
                if parola in self._dic_ita.dict:
                    word= rw.RichWord(parola)
                    word.corretta=True
                    parole.append(word)
                else:
                    word=rw.RichWord(parola)
                    word.corretta=False
                    parole.append(word)
        elif language == 'english':
            for parola in words:
                if parola in self._dic_ing.dict:
                    word= rw.RichWord(parola)
                    word.corretta=True
                    parole.append(word)
                else:
                    word=rw.RichWord(parola)
                    word.corretta=False
                    parole.append(word)
        elif language == 'spanish':
            for parola in words:
                if parola in self._dic_spa.dict:
                    word= rw.RichWord(parola)
                    word.corretta=True
                    parole.append(word)
                else:
                    word=rw.RichWord(parola)
                    word.corretta=False
                    parole.append(word)
        ans=[]
        for rich in parole:
            if rich.corretta==False:
                ans.append(rich)
        return ans
    def searchWordLinear(self, words, language):
        parole=[]
        if language == 'italian':
            for parola in words:
                cond=False
                for word in self._dic_ita.dict:
                    if word==parola:
                        parola_trovata=rw.RichWord(parola)
                        parola_trovata.corretta=True
                        parole.append(parola_trovata)
                        cond=True
                if cond==False:
                    parola_trovata = rw.RichWord(parola)
                    parola_trovata.corretta = False
                    parole.append(parola_trovata)
        elif language == 'english':
            for parola in words:
                cond = False
                for word in self._dic_ing.dict:
                    if word == parola:
                        parola_trovata = rw.RichWord(parola)
                        parola_trovata.corretta = True
                        parole.append(parola_trovata)
                        cond = True
                if cond == False:
                    parola_trovata = rw.RichWord(parola)
                    parola_trovata.corretta = False
                    parole.append(parola_trovata)
        elif language == 'spanish':
            for parola in words:
                cond=False
                for word in self._dic_spa.dict:
                    if word==parola:
                        parola_trovata=rw.RichWord(parola)
                        parola_trovata.corretta=True
                        parole.append(parola_trovata)
                        cond=True
                if cond==False:
                    parola_trovata = rw.RichWord(parola)
                    parola_trovata.corretta = False
                    parole.append(parola_trovata)
        ans=[]
        for rich in parole:
            if rich.corretta==False:
                ans.append(rich)
        return ans
    def searchWordDichotomic(self, words, language):
        parole=[]
        if language == 'italian':
            for parola in words:
                cond=False
                val_max=len(self._dic_ita.dict)
                val_min=0
                val=len(self._dic_ita.dict)//2
                while val!=val_min and val!=val_max:
                    parola_media=self._dic_ita.dict[val]
                    if parola_media<parola:
                        val_min = val
                        val=(val_max+val)//2
                    elif parola_media == parola:
                        word = rw.RichWord(parola)
                        word.corretta = True
                        parole.append(word)
                        cond=True
                        val=val_min
                        break
                    elif parola_media>parola:
                        val_max=val
                        val = (val_min + val) // 2
                if cond==False:
                    word = rw.RichWord(parola)
                    word.corretta = False
                    parole.append(word)
        elif language == 'english':
            for parola in words:
                cond=False
                val_max=len(self._dic_ing.dict)
                val_min=0
                val=len(self._dic_ing.dict)//2
                while val!=val_min and val!=val_max:
                    parola_media=self._dic_ing.dict[val]
                    if parola_media<parola:
                        val_min = val
                        val=(val_max+val)//2
                    elif parola_media == parola:
                        word = rw.RichWord(parola)
                        word.corretta = True
                        parole.append(word)
                        cond=True
                        break
                    elif parola_media>parola:
                        val_max=val
                        val = (val_min + val) // 2
                if cond==False:
                    word = rw.RichWord(parola)
                    word.corretta = False
                    parole.append(word)
        elif language == 'spanish':
            for parola in words:
                cond=False
                val_max=len(self._dic_spa.dict)
                val_min=0
                val=len(self._dic_spa.dict)//2
                while val!=val_min and val!=val_max:
                    parola_media=self._dic_spa.dict[val]
                    if parola_media<parola:
                        val_min = val
                        val=(val_max+val)//2
                    elif parola_media == parola:
                        word = rw.RichWord(parola)
                        word.corretta = True
                        parole.append(word)
                        cond=True
                        break
                    elif parola_media>parola:
                        val_max=val
                        val = (val_min + val) // 2
                if cond==False:
                    word = rw.RichWord(parola)
                    word.corretta = False
                    parole.append(word)
        ans=[]
        for rich in parole:
            if rich.corretta==False:
                ans.append(rich)
        return ans