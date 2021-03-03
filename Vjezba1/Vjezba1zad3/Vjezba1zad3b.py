def vrijemeDolaska():
    vrijemePolaska = input(
        "Unesite vrijeme polaska aviona u obliku dd:mm:gg:hh:mm:ss:zona ")
    vrijemePolaska = vrijemePolaska.split(":")

    vrijemeLeta = input(
        "Unesite vrijeme trajanja leta u obliku dd:mm:gg:hh:mm:ss:"
    )
    vrijemeLeta = vrijemeLeta.split(":")

    vremenskaZonaKrajnjeTocke = input(
        "Unesite vremensku zonu u kojoj se nalazi odredišni aerodrom")
    vremenskaZonaKrajnjeTocke = int(vremenskaZonaKrajnjeTocke)

    ZavrsnoVrijeme = []
    brojac = [0, 0, 0, 0, 0, 0]

    for i in range(0, len(vrijemePolaska)):
        vrijemePolaska[i] = int(vrijemePolaska[i])
        if(i != 6):
            vrijemeLeta[i] = int(vrijemeLeta[i])

        if(i == 0):
            ZavrsnoVrijeme.append(vrijemePolaska[i]+vrijemeLeta[i])
            if(ZavrsnoVrijeme[i] > 30):
                ZavrsnoVrijeme[i] = ZavrsnoVrijeme[i]-30
                brojac[i] = 1
                # dodat brojac posli
            print(ZavrsnoVrijeme[i])

        if(i == 1):
            ZavrsnoVrijeme.append(vrijemePolaska[i]+vrijemeLeta[i])
            if(ZavrsnoVrijeme[i] > 12):
                ZavrsnoVrijeme[i] = ZavrsnoVrijeme[i]-12
                brojac[i] = 1
            if brojac[i-1] != 0:
                ZavrsnoVrijeme[i] = ZavrsnoVrijeme[i]+1
                if ZavrsnoVrijeme[i] > 12:
                    brojac[i] = 1
                    ZavrsnoVrijeme[i] = ZavrsnoVrijeme[i]-12

            print(ZavrsnoVrijeme[i])

        if(i == 2):
            ZavrsnoVrijeme.append(vrijemePolaska[i]+vrijemeLeta[i])
            if brojac[i-1] != 0:
                ZavrsnoVrijeme[i] = ZavrsnoVrijeme[i]+1
            print(ZavrsnoVrijeme[i])

        if (i == 3):
            ZavrsnoVrijeme.append(vrijemePolaska[i]+vrijemeLeta[i])
            if(ZavrsnoVrijeme[i] > 24):
                ZavrsnoVrijeme[i] = ZavrsnoVrijeme[i]-24
                # uvjet zavrsnovrijeme[0]>0 ????
                ZavrsnoVrijeme[0] = ZavrsnoVrijeme[0]+1

            print(ZavrsnoVrijeme[i])

        if (i == 4):
            ZavrsnoVrijeme.append(vrijemePolaska[i]+vrijemeLeta[i])
            if(ZavrsnoVrijeme[i] > 60):
                ZavrsnoVrijeme[i] = ZavrsnoVrijeme[i]-60
                ZavrsnoVrijeme[3] = ZavrsnoVrijeme[3]+1
            print(ZavrsnoVrijeme[i])

        if (i == 5):
            ZavrsnoVrijeme.append(vrijemePolaska[i]+vrijemeLeta[i])
            if(ZavrsnoVrijeme[i] > 60):
                ZavrsnoVrijeme[i] = ZavrsnoVrijeme[i]-60
                ZavrsnoVrijeme[4] = ZavrsnoVrijeme[4]+1
            print(ZavrsnoVrijeme[i])

        if (i == 6):
            if(vrijemePolaska[i] < 0 or vremenskaZonaKrajnjeTocke < 0):
                ZavrsnoVrijeme.append(
                    abs(vrijemePolaska[i])+abs(vremenskaZonaKrajnjeTocke))
                ZavrsnoVrijeme[3] = ZavrsnoVrijeme[3]+ZavrsnoVrijeme[6]
            elif(vrijemePolaska[i] > vremenskaZonaKrajnjeTocke):
                ZavrsnoVrijeme.append(
                    vrijemePolaska[i]-vremenskaZonaKrajnjeTocke)
                ZavrsnoVrijeme[3] = ZavrsnoVrijeme[3]-ZavrsnoVrijeme[6]
            else:
                ZavrsnoVrijeme.append(
                    vremenskaZonaKrajnjeTocke-vrijemePolaska[i])
                ZavrsnoVrijeme[3] = ZavrsnoVrijeme[3]+ZavrsnoVrijeme[6]
            print(ZavrsnoVrijeme[i])

    if(ZavrsnoVrijeme[3] > 24):
        ZavrsnoVrijeme[3] = ZavrsnoVrijeme[3]-24
        ZavrsnoVrijeme[0] = ZavrsnoVrijeme[0]+1
    if(ZavrsnoVrijeme[3] > 48):
        ZavrsnoVrijeme[3] = ZavrsnoVrijeme[3]-48
        ZavrsnoVrijeme[0] = ZavrsnoVrijeme[0]+2

    print(ZavrsnoVrijeme)


vrijemeDolaska()
