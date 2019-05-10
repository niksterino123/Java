import random,time



class Xili:
    res = time.localtime(random.randrange(1, 99999999))
    fasebi = {1: "1 GEL", 2: "1 GEL", 3: "1 GEL", 4: "90 Tetri", 5: "50 Tetri", 6: "20 Tetri", 7: "20 Tetri", 8: "30 Tetri", 9: "40 Tetri", 10: "50 Tetri", 11: "70 Tetri", 12: "80 Tetri"}

    sezonebi = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July",
              8: "August", 9: "September", 10: "October", 11: "7November", 12: "December"}

    def __init__(self,saxeli, sezoni, fasi):
        self.saxeli = saxeli
        self.sezoni = sezoni
        self.fasi = fasi


    def info(self):
        print("xili aris",self.saxeli,"da girs",self.fasi,self.sezoni + "-shi" )

    def damwifeba(self):
        print(self.saxeli,"mwifdeba or tveshi")


sazamtro = Xili("Sazamtro", Xili.sezonebi[Xili.res.tm_mon],Xili.fasebi[Xili.res.tm_mon])

sazamtro.info()
sazamtro.damwifeba()

