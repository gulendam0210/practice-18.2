K = {       101: {"ady":"Perman","awtory":"A.Govshudov","sany":"8"},
            102: {"ady":"Saylanan eserler","awtory":"G.Ezizov","sany":"12"},
            103: {"ady":"Ykbal","awtory":"H.Deryayev","sany":"6"},
            104: {"ady":"Leyli - Mejnun","awtory":"N.Andalyp","sany":"4"},
            105: {"ady":"Oylanma bayry","awtory":"K.Gurbannepesov","sany":"9"},
    }
def gormek():
    for i,j in K.items():
        print(i, "-" ,j)
def almak():
    kitap = int(input("kitap belgisi: "))
    sany = int(input("kitap sany: "))
    K[kitap]['sany'] -= sany
    print("Siz kitaby aldynyz!")
def tabshyrmak():
    kitap = int(input("kitap belgisi: "))
    sany = int(input("kitap sany: "))
    K[kitap]['sany'] += sany
    print("Siz kitaby tabshyrfynyz!")
def cykmak():
    print("Sagbolun :)")

while True:

        print("""KITAPHANA:
            1. Kitap gormek
            2. Kitap almak
            3. Kitap tabshyrmak
            4. Cykmak
           """)
        hyzmat = int(input("Hyzmat görnüşini saýlaň (1, 2, 3): "))
        if hyzmat == 1:
            gormek()
        elif hyzmat == 2:
            almak()
        elif hyzmat == 3:
            tabshyrmak()
        elif hyzmat == 4:
            cykmak()
            break
        else:
            print("1-4 cenli belgi saylan.")
