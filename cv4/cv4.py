class Hrac(object):
    def __init__(self, jmeno):
        self.__jmeno = jmeno
        self.__zapasy = 0
        self.__goly = 0

    def get_jmeno(self):
        return self.__jmeno

    def get_zapasy(self):
        return self.__zapasy

    def get_goly(self):
        return self.__goly

    def hral_zapas(self):
        self.__zapasy += 1

    def dal_gol(self):
        self.__goly += 1

    def info(self):
        return str("{0} Z:{1} G:{2}".format(self.__jmeno, self.__zapasy, self.__goly))

class Tym(object):
    dres = 0
    def __init__(self, jmeno):
        self.__jmeno = jmeno
        self.__seznam_hracu = {}

    def pridej_hrace(self, Hrac):
        dres =+ 1
        self.__seznam_hracu[dres] = Hrac

    def zapas(self, *dresy):
        for hraci in self.__seznam_hracu.items():
            hraci[1].hral_zapas()        
            
        for i in dresy:
            if(hraci[0] == i):
                hraci[1].dal_gol()
        
    def filtruj_hrace(self, pocet_golu):
        pass

    def info(self):
        print(self.__jmeno)
        for i in self.__seznam_hracu.items():
            print(str(i[0]) + ": " + i[1].info())
                        
def main():
    Typek = Hrac("Jarda Bagr")
    druhy = Hrac("nekdo")
    print(Typek.get_jmeno())
    print(Typek.get_zapasy())
    print(Typek.get_goly())
    Typek.hral_zapas()
    Typek.dal_gol()
    Typek.dal_gol()
    Typek.dal_gol()
    print(Typek.info())
    Nasi = Tym("Delostrelci Bukovec")
    Nasi.pridej_hrace(Typek)
    Nasi.pridej_hrace(druhy)
    Nasi.zapas(1)
    Nasi.info()


if __name__=='__main__':
    main()
