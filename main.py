import spellchecker

sc = spellchecker.SpellChecker()

while(True):
    sc.printMenu()

    txtIn = input()
    # Add input control here!

    if int(txtIn) == 1:
        print("Inserisci  la tua frase in Italiano\n")
        txtInInput = input().lower()
        parole_errate, time,parole_errate_linear, time1,parole_errate_dichotomic, time2=sc.handleSentence(txtInInput,"italian")
        print("-----------------------------------------------\nUsing Contains")
        for parola in parole_errate:
            print(f"{parola}")
        print(f"Time elapsed: {time}")
        print("-----------------------------------------------\nUsing Linear search")
        for parola in parole_errate_linear:
            print(f"{parola}")
        print(f"Time elapsed: {time1}")
        print("-----------------------------------------------\nUsing Dichotomic search")
        for parola in parole_errate_dichotomic:
            print(f"{parola}")
        print(f"Time elapsed: {time2}")

    if int(txtIn) == 2:
        print("Inserisci la tua frase in Inglese\n")
        txtInInput = input().lower()
        parole_errate, time,parole_errate_linear, time1,parole_errate_dichotomic, time2=sc.handleSentence(txtInInput,"english")
        print("-----------------------------------------------\nUsing Contains")
        for parola in parole_errate:
            print(f"{parola}")
        print(f"Time elapsed: {time}")
        print("-----------------------------------------------\nUsing Linear search")
        for parola in parole_errate_linear:
            print(f"{parola}")
        print(f"Time elapsed: {time1}")
        print("-----------------------------------------------\nUsing Dichotomic search")
        for parola in parole_errate_dichotomic:
            print(f"{parola}")
        print(f"Time elapsed: {time2}")

    if int(txtIn) == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        txtInInput = input().lower()
        parole_errate, time,parole_errate_linear, time1,parole_errate_dichotomic, time2=sc.handleSentence(txtInInput,"spanish")
        print("-----------------------------------------------\nUsing Contains")
        for parola in parole_errate:
            print(f"{parola}")
        print(f"Time elapsed: {time}")
        print("-----------------------------------------------\nUsing Linear search")
        for parola in parole_errate_linear:
            print(f"{parola}")
        print(f"Time elapsed: {time1}")
        print("-----------------------------------------------\nUsing Dichotomic search")
        for parola in parole_errate_dichotomic:
            print(f"{parola}")
        print(f"Time elapsed: {time2}")

    if int(txtIn) == 4:
        break


